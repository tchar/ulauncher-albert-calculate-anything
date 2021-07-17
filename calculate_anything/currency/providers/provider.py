from ...utils import is_types, get_module
has_requests = get_module('requests') is not None
from datetime import datetime
from ...exceptions import CurrencyProviderRequestException, MissingRequestsException

class CurrencyProvider:
    def __init__(self, api_key=''):
        self._api_key = api_key
        self.last_request_timestamp = 0
        self.had_error = False

    def request_currencies(self, *currencies, force=False):
        if not has_requests:
            self.had_error = True
            raise MissingRequestsException('requests is not installed')
        if not self.api_key_valid:
            self.had_error = True
            raise CurrencyProviderRequestException('API Key is not valid')
        if not force and self.had_error and datetime.now().timestamp() - 60 <= self.last_request_timestamp:
            self.had_error = True
            raise CurrencyProviderRequestException('Could not make request')
        self.last_request_timestamp = datetime.now().timestamp()
        return {}

    @property
    def api_key_valid(self):
        return is_types(self._api_key, str) and self._api_key.strip() != ''

    def set_api_key(self, api_key):
        self._api_key = api_key