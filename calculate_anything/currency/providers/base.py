from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps
import re
from typing import Any, Callable, Dict, Iterable, TypeVar
from urllib.parse import urljoin, urlparse, urlunparse, urlencode
from urllib.request import Request
from calculate_anything.currency.data import CurrencyData
from calculate_anything.exceptions import CurrencyProviderException


__all__ = ['ApiKeyCurrencyProvider', 'FreeCurrencyProvider']


RT = TypeVar('RT')


class CurrencyProvider(ABC):
    BASE_URL: str
    API_URL: str

    class Decorators:
        @staticmethod
        def with_ratelimit(func: Callable[..., RT]) -> RT:
            @wraps(func)
            def _wrapper(
                self: 'CurrencyProvider',
                *currencies: Iterable[str],
                force: bool = False
            ) -> Any:
                timestamp = datetime.now().timestamp()
                if (
                    not force
                    and self.had_error
                    and timestamp - 60 <= self.last_request_timestamp
                ):
                    raise CurrencyProviderException('Too many requests')
                self.last_request_timestamp = timestamp
                return func(self, *currencies, force=force)

            return _wrapper

    def __init__(self) -> None:
        self.last_request_timestamp = 0
        self.had_error = False

    @classmethod
    def get_request(
        cls, params: Dict[str, str] = {}, validate_uri: bool = True
    ) -> Request:
        headers = {'user-agent': 'Calculate Anything'}
        url = urljoin(cls.BASE_URL, cls.API_URL)
        url = list(urlparse(url))
        url[4] = urlencode(params)
        url = urlunparse(url)
        request = Request(url, headers=headers)
        # Only urls and only secure connections
        # Don't fucking install untrusted certs unless you want
        # a mitm xml bomb on your head
        # and no I won't install extra dependencies for your stupidity
        if validate_uri and not re.match(r'^https:\/\/', request.full_url):
            raise Exception('Invalid request url: {}'.format(request.full_url))
        return request

    @abstractmethod
    def request_currencies(
        self, *currencies: str, force: bool = False
    ) -> CurrencyData:
        pass


class _MockCurrencyProvider(CurrencyProvider):
    def __init__(self, *args, **kwargs):
        pass

    def request_currencies(
        self, *currencies: str, force: bool
    ) -> CurrencyData:
        pass


class FreeCurrencyProvider(CurrencyProvider):
    pass


class ApiKeyCurrencyProvider(CurrencyProvider):
    class Decorators(CurrencyProvider.Decorators):
        @staticmethod
        def with_valid_api_key(func: Callable[..., RT]) -> RT:
            @wraps(func)
            def _wrapper(
                self: 'ApiKeyCurrencyProvider', *args: Any, **kwargs: Any
            ):
                if not self.api_key_valid:
                    self.had_error = True
                    raise CurrencyProviderException('API Key is not valid')
                return func(self, *args, **kwargs)

            return _wrapper

    def __init__(self, api_key: str = '') -> None:
        super().__init__()
        self._api_key = api_key

    @property
    def api_key_valid(self) -> bool:
        return isinstance(self._api_key, str) and self._api_key.strip() != ''

    @property
    def api_key(self) -> str:
        return self._api_key

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        self._api_key = api_key
