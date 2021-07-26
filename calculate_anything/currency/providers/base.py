from calculate_anything.exceptions import CurrencyProviderRequestException, MissingRequestsException
from datetime import datetime
from calculate_anything.utils import is_types, get_module
has_requests = get_module('requests') is not None

__all__ = ['ApiKeyCurrencyProvider', 'FreeCurrencyProvider']


class _MockCurrencyProvider:
    def __init__(self, *args, **kwargs):
        pass


class _CurrencyProvider:
    def __init__(self):
        self.last_request_timestamp = 0
        self.had_error = False

    def request_currencies(self, *currencies, force=False):
        if not has_requests:
            self.had_error = True
            raise MissingRequestsException('requests is not installed')
        if not force and self.had_error and datetime.now().timestamp() - 60 <= self.last_request_timestamp:
            self.had_error = True
            raise CurrencyProviderRequestException('Could not make request')
        self.last_request_timestamp = datetime.now().timestamp()
        return {}


class FreeCurrencyProvider(_CurrencyProvider):
    pass


class ApiKeyCurrencyProvider(_CurrencyProvider):
    def __init__(self, api_key=''):
        super().__init__()
        self._api_key = api_key

    @property
    def api_key_valid(self):
        return is_types(self._api_key, str) and self._api_key.strip() != ''

    def set_api_key(self, api_key):
        self._api_key = api_key

    def request_currencies(self, *currencies, force):
        super_result = super().request_currencies(*currencies, force)
        if not self.api_key_valid:
            self.had_error = True
            raise CurrencyProviderRequestException('API Key is not valid')
        return super_result
