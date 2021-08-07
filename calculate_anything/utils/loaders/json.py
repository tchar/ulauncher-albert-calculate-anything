from typing import Dict, TYPE_CHECKING
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict
if TYPE_CHECKING:
    from calculate_anything.currency.data import CurrencyData
import os
import shutil
import json
from calculate_anything.utils.loaders.loader import Loader
from calculate_anything import logging


__all__ = ['JsonLoader', 'CurrencyCacheLoader']


logger = logging.getLogger(__name__)


class JsonLoader(Loader):
    def __init__(
        self, filepath: str, default_data: Dict, mode: Loader.Mode = 0
    ) -> None:
        super().__init__(Loader.Status.PENDING, mode)
        self.filepath = filepath
        self.default_data = default_data
        self._data = None

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    def _pre_load(self) -> None:
        self._file_exists = os.path.exists(self.filepath)
        if not self._file_exists:
            self._mode |= Loader.Mode.FALLBACK
        else:
            self._mode |= Loader.Mode.LOAD

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    @Loader.Decorators.with_mode(Loader.Mode.LOAD)
    def _load(self) -> None:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self._data = f.read()
        except Exception as e:
            self._mode |= Loader.Mode.REMOVE
            msg = 'Cannot read file {}: {}'.format(self.filepath, e)
            logger.exception(msg)
            return
        try:
            self._data = json.loads(self._data)
            self._mode |= Loader.Mode.VALIDATE
        except Exception as e:
            self._mode |= Loader.Mode.REMOVE
            msg = 'Cannot parse file as json {}: {}'.format(self.filepath, e)
            logger.exception(msg)

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    @Loader.Decorators.without_mode(Loader.Mode.NO_REMOVE)
    @Loader.Decorators.with_mode(Loader.Mode.REMOVE)
    def _remove(self) -> None:
        if os.path.isdir(self.filepath):
            self._status |= Loader.Status.FILE_IS_DIR
            try:
                shutil.rmtree(self.filepath)
                self._mode |= Loader.Mode.FALLBACK
            except Exception as e:  # pragma: no cover
                msg = 'Could not remove directory {}: {}'
                msg = msg.format(self.filepath, e)
                logger.exception(msg)
                self._status |= Loader.Status.FAIL
                self._status |= Loader.Status.CANNOT_REMOVE_FILE
        else:
            try:
                os.remove(self.filepath)
                self._mode |= Loader.Mode.FALLBACK
            except Exception as e:  # pragma: no cover
                msg = 'Could not remove file {}: {}'
                msg = msg.format(self.filepath, e)
                logger.exception(msg)
                self._status |= Loader.Status.FAIL
                self._status |= Loader.Status.CANNOT_REMOVE_FILE

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    @Loader.Decorators.with_mode(Loader.Mode.VALIDATE)
    def _validate(self) -> None:
        self._status |= Loader.Status.SUCCESS

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    @Loader.Decorators.with_mode(Loader.Mode.FALLBACK)
    def _fallback(self) -> None:
        if self.default_data is None:
            self._status |= Loader.Status.FAIL
            return
        try:
            data = json.dumps(self.default_data)
            with open(self.filepath, 'w', encoding='utf-8') as f:
                f.write(data)
            self._data = self.default_data.copy()
            self._status |= Loader.Status.SUCCESS
            self._status |= Loader.Status.DEFAULT_DATA
        except Exception as e:
            msg = 'Could not write default data {}: {}'
            msg = msg.format(self.filepath, e)
            logger.exception(msg)
            self._status |= Loader.Status.FAIL
            self._status |= Loader.Status.CANNOT_WRITE_FILE

    @property
    def data(self) -> Dict:
        return self._data

    def load(self) -> None:
        self._pre_load()
        self._load()
        self._remove()
        self._validate()
        self._fallback()

        # Some cleanup
        self._status &= ~Loader.Status.PENDING
        if self._mode & Loader.Mode.NO_REMOVE:
            self._mode &= ~Loader.Mode.REMOVE
        if not (self.status & Loader.Status.SUCCESS):
            self._status |= Loader.Status.FAIL
        return self.status & Loader.Status.SUCCESS == 1


class JsonCurrencyData(TypedDict):
    provider: str
    exchange_rates: 'CurrencyData'
    last_update_timestamp: float


class CurrencyCacheLoader(JsonLoader):
    def __init__(self, filepath: str) -> None:
        default_data = {'exchange_rates': {}, 'last_update_timestamp': 0}
        super().__init__(filepath, default_data, mode=0)

    def _validate_exchange_rate(
        self, currency: str, currency_data: JsonCurrencyData
    ) -> None:
        if not isinstance(currency_data, dict):
            msg = 'Rate for "{}" is not a dict {}'
            msg = msg.format(currency, currency_data)
            raise Exception(msg)
        if not isinstance(currency_data.get('rate'), (int, float)):
            raise Exception('Currency rate is not a number')
        if not isinstance(
            currency_data.get('timestamp_refresh'), (int, float, type(None))
        ):
            raise Exception('timestamp_refresh is not a number or None')

    def _validate_cache(self) -> None:
        data = self.data
        if not isinstance(data, dict):
            raise Exception('data is not a dict')
        if not isinstance(data.get('exchange_rates'), dict):
            raise Exception('exchange rates is not a dict')
        for currency, currency_data in data['exchange_rates'].items():
            self._validate_exchange_rate(currency, currency_data)
        if not isinstance(data.get('last_update_timestamp'), (int, float)):
            raise Exception('last_update_timestamp is not a number')
        self._status |= Loader.Status.SUCCESS

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    @Loader.Decorators.with_mode(Loader.Mode.VALIDATE)
    def _validate(self) -> None:
        try:
            self._validate_cache()
        except Exception as e:
            self._data = None
            self._mode |= Loader.Mode.FALLBACK
            self._status |= Loader.Status.INVALID_DATA
            logger.exception(e)
