from .provider import _MockCurrencyProvider
from .fixerio import FixerIOCurrencyProvider
from ...exceptions import CurrencyProviderException


class CurrencyProviderFactory:
    providers = {
        'fixerio': FixerIOCurrencyProvider,
        'internal': _MockCurrencyProvider
    }

    @staticmethod
    def get_available_providers():
        return list(CurrencyProviderFactory.providers.keys())

    @staticmethod
    def get_provider(provider_name, api_key=''):
        if provider_name in CurrencyProviderFactory.providers:
            return CurrencyProviderFactory.providers[provider_name](api_key)
        raise CurrencyProviderException(
            'No provider found with name "{}"'.format(provider_name))
