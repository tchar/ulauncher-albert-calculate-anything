from calculate_anything.exceptions import CurrencyProviderException
from datetime import datetime
from urllib.parse import urljoin, urlparse, urlunparse, urlencode
from urllib.request import Request

__all__ = ['ApiKeyCurrencyProvider', 'FreeCurrencyProvider']


class _MockCurrencyProvider:
    def __init__(self, *args, **kwargs):
        pass


class CurrencyProvider:
    BASE_URL = ''
    API_URL = ''

    def __init__(self):
        self.last_request_timestamp = 0
        self.had_error = False

    def get_request(self, params={}):
        cls = self.__class__
        headers = {
            'user-agent': 'Calculate Anything'
        }
        url = urljoin(cls.BASE_URL, cls.API_URL)
        url = list(urlparse(url))
        url[4] = urlencode(params)
        url = urlunparse(url)
        return Request(url, headers=headers)

    def request_currencies(self, *currencies, force=False):
        timestamp = datetime.now().timestamp()
        if not force and self.had_error and \
                timestamp - 60 <= self.last_request_timestamp:
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
