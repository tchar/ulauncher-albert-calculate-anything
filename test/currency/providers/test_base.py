from calculate_anything.exceptions import CurrencyProviderException
import pytest
from calculate_anything.currency.providers.base import CurrencyProvider


def test_too_many_requests():
    provider = CurrencyProvider()
    provider.request_currencies()
    provider.had_error = True

    with pytest.raises(CurrencyProviderException) as excinfo:
        provider.request_currencies()

    assert str(excinfo.value) == 'Too many requests'

    assert provider.had_error is True
    provider.request_currencies(force=True)
