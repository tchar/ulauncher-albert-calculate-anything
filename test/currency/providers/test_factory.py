from calculate_anything.exceptions import CurrencyProviderException
import pytest
from calculate_anything.currency.providers import (
    CurrencyProviderFactory,
    FixerIOCurrencyProvider,
)
from calculate_anything.currency.providers.base import _MockCurrencyProvider


def test_get_available_providers():
    available_providers = CurrencyProviderFactory.get_available_providers()
    assert sorted(available_providers) == sorted(['fixerio', 'internal'])


def test_get_provider():
    provider = CurrencyProviderFactory.get_provider('internal')
    assert isinstance(provider, _MockCurrencyProvider)

    provider = CurrencyProviderFactory.get_provider('fixerio')
    assert isinstance(provider, FixerIOCurrencyProvider)

    provider = CurrencyProviderFactory.get_provider('fixerio', api_key='1245')
    assert isinstance(provider, FixerIOCurrencyProvider)
    assert provider.api_key_valid
    assert provider._api_key == '1245'

    with pytest.raises(CurrencyProviderException):
        CurrencyProviderFactory.get_provider('Some uknown provider key')
