import os
import json
from datetime import datetime
from functools import wraps
from calculate_anything.constants import CURRENCY_DATA_FILE
from calculate_anything import logging
from calculate_anything.currency.data import CurrencyData
from calculate_anything.utils.loaders import CurrencyCacheLoader


__all__ = ['CurrencyCache']


logger = logging.getLogger(__name__)


def preload(func):
    @wraps(func)
    def _wrapper(self, *args, **kwargs):
        self.load()
        return func(self, *args, **kwargs)
    return _wrapper


class CurrencyCache:
    def __init__(self, update_frequency=0):
        self._update_frequency = update_frequency
        self._data = {
            'provider': '',
            'exchange_rates': {},
            'last_update_timestamp': 0
        }
        self._loaded = False
        self._use_only_memory = False

    def load(self):
        return self._load()

    def _load(self):
        if self._loaded or self._use_only_memory:
            return True
        if not self.enabled:
            return False

        loader = CurrencyCacheLoader(CURRENCY_DATA_FILE)
        loaded = loader.load()
        self._data = loader.data
        self._loaded = True
        return loaded

    @property
    @preload
    def provider(self):
        return self._data.get('provider', '')

    @property
    @preload
    def last_update_timestamp(self):
        return self._data.get('last_update_timestamp', 0)

    @preload
    def get_rates(self, *currencies) -> CurrencyData:
        if currencies:
            return {
                currency: self._data['exchange_rates'][currency]
                for currency in currencies
                if currency in self._data['exchange_rates']
            }
        return self._data['exchange_rates']

    def enable(self, update_frequency):
        logger.info('Enabling cache every {}s'.format(update_frequency))
        self._update_frequency = update_frequency

    def disable(self):
        logger.info('Disabling cache')
        self._update_frequency = 0

    @property
    def enabled(self):
        return self._update_frequency > 0

    def next_update_seconds(self):
        return max(0.0, self._data['last_update_timestamp'] +
                   self._update_frequency - datetime.now().timestamp())

    def should_update(self):
        return datetime.now().timestamp() - self.last_update_timestamp > \
            self._update_frequency

    def clear(self):
        logger.info('Clearing cache {}'.format(self._use_only_memory))
        self._data = {
            'exchange_rates': {},
            'last_update_timestamp': 0
        }
        if self._use_only_memory:
            logger.info('Using only memory, not deleting file')
            return
        if os.path.isfile(CURRENCY_DATA_FILE):
            try:
                os.remove(CURRENCY_DATA_FILE)
            except Exception as e:  # pragma: no cover
                logger.exception(
                    'Could not remove data file {}: {}'
                    .format(CURRENCY_DATA_FILE, e))

    def save(self, exchange_rates, provider):
        if not self.enabled:
            logger.warning('Cache not enabled, not saving')
            return
        if not exchange_rates:
            logger.warning('Empty exchange rates, not saving')
            return
        self._data = {
            'provider': provider,
            'exchange_rates': exchange_rates,
            'last_update_timestamp': datetime.now().timestamp()
        }
        if self._use_only_memory:
            logger.info('Using only memory, not writing to file')
            return
        logger.info('Writing currency data to file')
        try:
            with open(CURRENCY_DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(json.dumps(self._data))
        except Exception as e:  # pragma: no cover
            logger.exception('Could not save cache data {}: {}'
                             .format(CURRENCY_DATA_FILE, e))
