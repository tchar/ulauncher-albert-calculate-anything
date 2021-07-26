import os
import shutil
import json
from datetime import datetime
from functools import wraps
from calculate_anything.utils.misc import is_types
from calculate_anything.constants import CACHE_DIR, CURRENCY_DATA_FILE
import calculate_anything.log as logging


class CacheException(Exception):
    pass


def preload(func):
    @wraps(func)
    def _wrapper(self, *args, **kwargs):
        self._load()
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
        self._logger = logging.getLogger(__name__)

    def _check_structure(self):
        if os.path.isfile(CACHE_DIR):
            try:
                os.remove(CACHE_DIR)
            except Exception as e:
                self._logger.error(
                    'Could not remove cache file {}: {}'.format(CACHE_DIR, e))
            return False

        if not os.path.exists(CACHE_DIR):
            try:
                os.makedirs(CACHE_DIR)
            except Exception as e:
                self._logger.error(
                    'Could not create cache directory {}: {}'.format(CACHE_DIR, e))
                return False

        if os.path.isdir(CURRENCY_DATA_FILE):
            try:
                shutil.rmtree(CURRENCY_DATA_FILE)
            except Exception as e:
                self._logger.error(
                    'Could not remove data directory {}: {}'.format(CURRENCY_DATA_FILE, e))
                return False

        if os.path.exists(CURRENCY_DATA_FILE):
            try:
                with open(CURRENCY_DATA_FILE, 'r') as f:
                    data = json.loads(f.read())
                    if not is_types(data.get('exchange_rates'), dict):
                        raise Exception('exchange rates is not a dict')
                    for k, v in data['exchange_rates'].items():
                        if not is_types(v, dict):
                            raise Exception(
                                'Currency {} rate is not a dict {}'.format(k, v))
                        if not is_types(v.get('rate'), int, float):
                            raise Exception('Currency rate is not a number')
                        if not is_types(v.get('timestamp_refresh'), int, float, type(None)):
                            raise Exception(
                                'timestamp_refresh is not a number or None')
                    if not is_types(data.get('last_update_timestamp'), int, float):
                        raise Exception(
                            'last_update_timestamp is not a number')
            except Exception as e:
                self._logger.error('Data file {} is possible corrupted, will try to remove it: {}'.format(
                    CURRENCY_DATA_FILE, e))
                try:
                    os.remove(CURRENCY_DATA_FILE)
                except Exception as e:
                    self._logger.error(
                        'Could not remove data file {}: {}'.format(CURRENCY_DATA_FILE, e))
                    return False

        if not os.path.exists(CURRENCY_DATA_FILE):
            data = {'exchange_rates': {}, 'last_update_timestamp': 0}
            try:
                with open(CURRENCY_DATA_FILE, 'w') as f:
                    f.write(json.dumps(data))
            except Exception as e:
                self._logger.error(
                    'Could not write default data file {}: {}'.format(CURRENCY_DATA_FILE, e))
                return False
        return True

    def _load(self):
        if self._loaded or not self.enabled or self._use_only_memory:
            return

        if not self._check_structure():
            self._use_only_memory = True
            self._data = {'exchange_rates': {}, 'last_update_timestamp': 0}
            return

        with open(CURRENCY_DATA_FILE, 'r') as f:
            self._data = json.loads(f.read())

        self._loaded = True
        return

    @property
    @preload
    def provider(self):
        return self._data.get('provider', '')

    @property
    @preload
    def last_update_timestamp(self):
        return self._data.get('last_update_timestamp', 0)

    @preload
    def get_rates(self, *currencies):
        if currencies:
            return {
                currency: self._data['exchange_rates'][currency]
                for currency in currencies
                if currency in self._data['exchange_rates']
            }
        return self._data['exchange_rates']

    @preload
    def get_rate_timestamp(self, currency):
        if currency not in self._data['exchange_rates']:
            return None
        return self._data['exchange_rates'][currency].get('timestamp_refresh')

    def enable(self, update_frequency):
        self._update_frequency = update_frequency

    def disable(self):
        self._update_frequency = 0

    @property
    def enabled(self):
        return self._update_frequency > 0

    def next_update_seconds(self):
        return max(0.0, self._data['last_update_timestamp'] + self._update_frequency - datetime.now().timestamp())

    def should_update(self):
        return datetime.now().timestamp() - self.last_update_timestamp > self._update_frequency

    def clear(self):
        self._data = {
            'exchange_rates': {},
            'last_update_timestamp': 0
        }
        if os.path.isfile(CURRENCY_DATA_FILE):
            try:
                os.remove(CURRENCY_DATA_FILE)
            except Exception as e:
                self._logger.error(
                    'Could not remove data file {}: {}'.format(CURRENCY_DATA_FILE, e))

    def save(self, exchange_rates, provider):
        if not self.enabled:
            return
        self._data = {
            'provider': provider,
            'exchange_rates': exchange_rates,
            'last_update_timestamp': datetime.now().timestamp()
        }
        if self._use_only_memory:
            return
        if not self._check_structure():
            self._use_only_memory = True
            return
        try:
            with open(CURRENCY_DATA_FILE, 'w') as f:
                f.write(json.dumps(self._data))
        except Exception as e:
            self._logger.error(
                'Could not save cache data {}: {}'.format(CURRENCY_DATA_FILE, e))
