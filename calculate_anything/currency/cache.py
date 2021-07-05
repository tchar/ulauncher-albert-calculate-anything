import os
import shutil
import json
from datetime import datetime
from functools import wraps
from ..utils import is_types
from ..constants import CACHE_DIR, DATA_FILE
from ..logging_wrapper import LoggingWrapper as logging

class CacheException(Exception):
    pass

def preload(func):
    @wraps(func)
    def _wrapper(self, *args, **kwargs):
        self._load()
        return func(self, *args, **kwargs)
    return _wrapper

class CurrencyCache:
    def __init__(self, _update_frequency=0):
        self._update_frequency = _update_frequency
        self._data = {}
        self._loaded = False
        self._use_only_memory = False
        self._logger = logging.getLogger(__name__)

    def _check_structure(self):
        if os.path.isfile(CACHE_DIR):
            try:
                os.remove(CACHE_DIR)
            except Exception as e:
                self._logger.error('Could not remove cache file {}: {}'.format(CACHE_DIR, e))
            return False
        
        if not os.path.exists(CACHE_DIR):
            try:
                os.makedirs(CACHE_DIR)
            except Exception as e:
                self._logger.error('Could not create cache directory {}: {}'.format(CACHE_DIR, e))
                return False

        if os.path.isdir(DATA_FILE):
            try:
                shutil.rmtree(DATA_FILE)
            except Exception as e:
                self._logger.error('Could not remove data directory {}: {}'.format(DATA_FILE, e))
                return False

        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    data = json.loads(f.read())
                    if not is_types(data.get('exchange_rates'), dict):
                        raise Exception('exchange rates is not a dict')
                    for k, v in data['exchange_rates'].items():
                        if len(k) != 3:
                            raise Exception('Currency {} is invalid'.format(k))
                        if not is_types(v, dict):
                            raise Exception('Currency {} rate is not a dict {}'.format(k, v))
                        if not is_types(v.get('rate'), int, float):
                            raise Exception('Currency rate is not a number')
                        if not is_types(v.get('timestamp_refresh'), int, float, type(None)):
                            raise Exception('timestamp_refresh is not a number or None')
                    if not is_types(data.get('last_update_timestamp'), int, float):
                        raise Exception('last_update_timestamp is not a number')
            except Exception as e:
                self._logger.error('Data file {} is possible corrupted, will try to remove it: {}'.format(DATA_FILE, e))
                try:
                    os.remove(DATA_FILE)
                except Exception as e:
                    self._logger.error('Could not remove data file {}: {}'.format(DATA_FILE, e))
                    return False

        if not os.path.exists(DATA_FILE):
            data = {'exchange_rates': {}, 'last_update_timestamp': 0}
            try:
                with open(DATA_FILE, 'w') as f:
                    f.write(json.dumps(data))
            except Exception as e:
                self._logger.error('Could not write default data file {}: {}'.format(DATA_FILE, e))
                return False
        return True

    def _load(self):
        if self._loaded or not self.enabled or self._use_only_memory:
            return
        
        if not self._check_structure():
            self._use_only_memory = True
            self._data = {'exchange_rates': {}, 'last_update_timestamp': 0}
            return

        with open(DATA_FILE, 'r') as f:
            self._data = json.loads(f.read())

        self._loaded = True
        return

    @property
    @preload
    def last_update_timestamp(self):
        return self._data['last_update_timestamp']

    @preload
    def get_rates(self, *currencies):
        if currencies:
            return {
                currency: self._data['exchange_rates'][currency]
                for currency in currencies
                if currency in self._data['exchange_rates']
            }
        return self._data['exchange_rates']

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

    @preload
    def save(self, exchange_rates):
        if not self.enabled:
            return
        self._data = {
            'exchange_rates': exchange_rates,
            'last_update_timestamp': datetime.now().timestamp()
        }
        try:
            with open(DATA_FILE, 'w') as f:
                f.write(json.dumps(self._data))
        except Exception as e:
            self._logger.error('Could not save cache data {}: {}'.format(DATA_FILE, e))
        