from datetime import datetime
from ...utils import is_types
from ...exceptions import CurrencyProviderRequestException

class CurrencyProvider:
    def __init__(self, api_key=''):
        self._api_key = api_key
        self.last_request_timestamp = 0
        self.had_error = False

    def request_currencies(self, *currencies, force=False):
        if not self.api_key_valid:
            raise CurrencyProviderRequestException('API Key is not valid')
        if not force and self.had_error and datetime.now().timestamp() - 60 <= self.last_request_timestamp:
            raise CurrencyProviderRequestException('Could not make request')
        self.last_request_timestamp = datetime.now().timestamp()
        return {}

    @property
    def api_key_valid(self):
        return is_types(self._api_key, str) and self._api_key.strip() != ''

    def set_api_key(self, api_key):
        self._api_key = api_key