from calculate_anything.exceptions import CurrencyProviderException
import pytest
from calculate_anything.currency.providers.base import (
    CurrencyProvider,
    CurrencyData,
)


class CurrencyProviderImpl(CurrencyProvider):
    @CurrencyProvider.Decorators.with_ratelimit
    def request_currencies(self, *currencies, force=False) -> CurrencyData:
        return {}


def test_too_many_requests():
    provider = CurrencyProviderImpl()
    provider.request_currencies()
    provider.had_error = True

    with pytest.raises(CurrencyProviderException) as excinfo:
        provider.request_currencies()

    assert str(excinfo.value) == 'Too many requests'

    assert provider.had_error is True
    provider.request_currencies(force=True)
