from ...utils import is_types
from ...exceptions import CurrencyProviderRequestException

class CurrencyProvider:
    def __init__(self, api_key=''):
        self._api_key = api_key

    def request_currencies(self, *currencies):
        if not self.api_key_valid:
            raise CurrencyProviderRequestException('API Key is not valid')
        return {}

    @property
    def api_key_valid(self):
        return is_types(self._api_key, str) and self._api_key.strip() != ''

    def set_api_key(self, api_key):
        self._api_key = api_key