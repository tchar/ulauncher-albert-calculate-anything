from calculate_anything.exceptions import (
    CurrencyProviderException, MissingRequestsException
)
from datetime import datetime
from calculate_anything.utils import get_module
has_requests = get_module('requests') is not None

__all__ = ['ApiKeyCurrencyProvider', 'FreeCurrencyProvider']


class _MockCurrencyProvider:
    def __init__(self, *args, **kwargs):
        pass


class CurrencyProvider:
    def __init__(self):
        self.last_request_timestamp = 0
        self.had_error = False

    def request_currencies(self, *currencies, force=False):
        if not has_requests:
            self.had_error = True
            raise MissingRequestsException('requests is not installed')

        timestamp = datetime.now().timestamp()
        if not force and self.had_error and \
                timestamp - 60 <= self.last_request_timestamp:
            self.had_error = True
            raise CurrencyProviderException('Too many requests')
        self.last_request_timestamp = timestamp
        return {}


class FreeCurrencyProvider(CurrencyProvider):
    pass


class ApiKeyCurrencyProvider(CurrencyProvider):
    def __init__(self, api_key=''):
        super().__init__()
        self._api_key = api_key

    @property
    def api_key_valid(self):
        return isinstance(self._api_key, str) and self._api_key.strip() != ''

    def set_api_key(self, api_key):
        self._api_key = api_key

    def request_currencies(self, *currencies, force):
        super_result = super().request_currencies(*currencies, force)
        if not self.api_key_valid:
            self.had_error = True
            raise CurrencyProviderException('API Key is not valid')
        return super_result
