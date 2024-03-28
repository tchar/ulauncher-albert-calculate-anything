import os
import json
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional, TypeVar
from calculate_anything.constants import CURRENCY_DATA_FILE
from calculate_anything import logging
from calculate_anything.currency.data import CurrencyData
from calculate_anything.utils.loaders import CurrencyCacheLoader


__all__ = ['CurrencyCache']


logger = logging.getLogger(__name__)


RT = TypeVar('RT')


class CurrencyCache:
    class Decorators:
        @staticmethod
        def preload(func: Callable[..., RT]) -> Callable[..., RT]:
            @wraps(func)
            def _wrapper(
                self: 'CurrencyCache', *args: Any, **kwargs: Any
            ) -> Any:
                self.load()
                return func(self, *args, **kwargs)

            return _wrapper

    def __init__(self, update_frequency: int = 0) -> None:
        self._update_frequency = update_frequency
        self._data = {
            'provider': '',
            'exchange_rates': {},
            'last_update_timestamp': 0,
        }
        self._loaded = False
        self._use_only_memory = False

    def load(self) -> Optional['CurrencyCache']:
        return self._load()

    def _load(self) -> Optional['CurrencyCache']:
        if self._loaded or self._use_only_memory:
            return self
        if not self.enabled:
            return None

        loader = CurrencyCacheLoader(CURRENCY_DATA_FILE)
        loader.load()
        self._data = loader.data
        self._loaded = True
        return self

    @property
    @Decorators.preload
    def provider(self) -> str:
        return self._data.get('provider', '')

    @property
    @Decorators.preload
    def last_update_timestamp(self) -> float:
        return self._data.get('last_update_timestamp', 0.0)

    @Decorators.preload
    def get_rates(self, *currencies: str) -> CurrencyData:
        if currencies:
            return {
                currency: self._data['exchange_rates'][currency]
                for currency in currencies
                if currency in self._data['exchange_rates']
            }
        return self._data['exchange_rates']

    def enable(self, update_frequency: float) -> 'CurrencyCache':
        logger.info('Enabling cache every {}s'.format(update_frequency))
        self._update_frequency = update_frequency
        return self

    def disable(self) -> 'CurrencyCache':
        logger.info('Disabling cache')
        self._update_frequency = 0
        return self

    @property
    def enabled(self) -> bool:
        return self._update_frequency > 0

    def next_update_seconds(self) -> float:
        return max(
            0.0,
            self._data['last_update_timestamp']
            + self._update_frequency
            - datetime.now().timestamp(),
        )

    def should_update(self) -> bool:
        return (
            datetime.now().timestamp() - self.last_update_timestamp
            > self._update_frequency
        )

    def clear(self) -> 'CurrencyCache':
        logger.info('Clearing cache {}'.format(self._use_only_memory))
        self._data = {'exchange_rates': {}, 'last_update_timestamp': 0}
        if self._use_only_memory:
            logger.info('Using only memory, not deleting file')
            return self
        if os.path.isfile(CURRENCY_DATA_FILE):
            try:
                os.remove(CURRENCY_DATA_FILE)
            except Exception as e:  # pragma: no cover
                logger.exception(
                    'Could not remove data file {}: {}'.format(
                        CURRENCY_DATA_FILE, e
                    )
                )
        return self

    def save(
        self, exchange_rates: CurrencyData, provider: str
    ) -> 'CurrencyCache':
        if not self.enabled:
            logger.warning('Cache not enabled, not saving')
            return self
        if not exchange_rates:
            logger.warning('Empty exchange rates, not saving')
            return self
        self._data = {
            'provider': provider,
            'exchange_rates': exchange_rates,
            'last_update_timestamp': datetime.now().timestamp(),
        }
        if self._use_only_memory:
            logger.info('Using only memory, not writing to file')
            return self
        logger.info('Writing currency data to file')
        try:
            with open(CURRENCY_DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(json.dumps(self._data))
        except Exception as e:  # pragma: no cover
            logger.exception(
                'Could not save cache data {}: {}'.format(CURRENCY_DATA_FILE, e)
            )
        return self
