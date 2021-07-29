import os
import shutil
import json
from datetime import datetime
from functools import wraps
from calculate_anything.constants import CURRENCY_DATA_FILE
from calculate_anything import logging


__all__ = ['CurrencyCache']


def validate_file_stat():
    if os.path.isdir(CURRENCY_DATA_FILE):
        shutil.rmtree(CURRENCY_DATA_FILE)


def validate_exchange_rate(currency, currency_data):
    if not isinstance(currency_data, dict):
        msg = 'Rate for "{}" is not a dict {}'
        msg = msg.format(currency, currency_data)
        raise Exception(msg)
    if not isinstance(currency_data.get('rate'), (int, float)):
        raise Exception('Currency rate is not a number')
    if not isinstance(currency_data.get('timestamp_refresh'),
                      (int, float, type(None))):
        raise Exception('timestamp_refresh is not a number or None')


def validate_cache():
    if not os.path.exists(CURRENCY_DATA_FILE):
        return
    with open(CURRENCY_DATA_FILE, 'r') as f:
        data = json.loads(f.read())
        if not isinstance(data.get('exchange_rates'), dict):
            raise Exception('exchange rates is not a dict')
        for currency, currency_data in data['exchange_rates'].items():
            validate_exchange_rate(currency, currency_data)
        if not isinstance(data.get('last_update_timestamp'), (int, float)):
            raise Exception('last_update_timestamp is not a number')


def create_cache():
    if not os.path.exists(CURRENCY_DATA_FILE):
        data = {'exchange_rates': {}, 'last_update_timestamp': 0}
        with open(CURRENCY_DATA_FILE, 'w') as f:
            f.write(json.dumps(data))
    return True


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
        try:
            validate_file_stat()
        except Exception as e:
            self._logger.exception(
                'Could not remove data directory {}: {}'
                .format(CURRENCY_DATA_FILE, e))
            return False

        remove = False
        try:
            validate_cache()
        except Exception as e:
            self._logger.exception('Data file {} is possibly '
                                   'corrupted, will try to remove it: {}'
                                   .format(CURRENCY_DATA_FILE, e))
            remove = True

        if remove:
            try:
                os.remove(CURRENCY_DATA_FILE)
            except Exception as e:
                self._logger.exception(
                    'Could not remove data file {}: {}'
                    .format(CURRENCY_DATA_FILE, e))
                return False
        try:
            return create_cache()
        except Exception as e:
            self._logger.exception(
                'Could not write default data file {}: {}'
                .format(CURRENCY_DATA_FILE, e))
        return False

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

    def enable(self, update_frequency):
        self._update_frequency = update_frequency

    def disable(self):
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
        self._data = {
            'exchange_rates': {},
            'last_update_timestamp': 0
        }
        if os.path.isfile(CURRENCY_DATA_FILE):
            try:
                os.remove(CURRENCY_DATA_FILE)
            except Exception as e:
                self._logger.exception(
                    'Could not remove data file {}: {}'
                    .format(CURRENCY_DATA_FILE, e))

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
            self._logger.exception(
                'Could not save cache data {}: {}'
                .format(CURRENCY_DATA_FILE, e))
