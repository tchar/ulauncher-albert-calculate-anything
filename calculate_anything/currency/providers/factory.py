from typing import Dict, List
from calculate_anything.currency.providers import FixerIOCurrencyProvider
from calculate_anything.currency.providers.base import (
    CurrencyProvider,
    _MockCurrencyProvider,
)
from calculate_anything.exceptions import CurrencyProviderException


__all__ = ['CurrencyProviderFactory']


class CurrencyProviderFactory:
    providers: Dict[str, CurrencyProvider] = {
        'fixerio': FixerIOCurrencyProvider,
        'internal': _MockCurrencyProvider,
    }

    @staticmethod
    def get_available_providers() -> List[str]:
        return list(CurrencyProviderFactory.providers.keys())

    @staticmethod
    def get_provider(provider_name: str, api_key: str = '') -> CurrencyProvider:
        if provider_name in CurrencyProviderFactory.providers:
            return CurrencyProviderFactory.providers[provider_name](api_key)
        raise CurrencyProviderException(
            'No provider found with name "{}"'.format(provider_name)
        )
