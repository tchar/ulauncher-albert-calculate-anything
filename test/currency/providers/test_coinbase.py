import pytest
from calculate_anything.currency.providers import CoinbaseCurrencyProvider
from calculate_anything.exceptions import CurrencyProviderException
from test.tutils import currency_data, expected_currencies


def test_normal(mock_currency_provider, coinbase_data):
    cls = CoinbaseCurrencyProvider
    data = coinbase_data('EUR', currency_data('EUR')['rates'])

    with mock_currency_provider(cls, data, use_json=True) as coinbase:
        currencies = coinbase.request_currencies()
        assert currencies == expected_currencies()
        assert coinbase.had_error is False


def test_other_base_currency(mock_currency_provider, coinbase_data):
    cls = CoinbaseCurrencyProvider
    data = coinbase_data('USD', currency_data('USD')['rates'])
    with mock_currency_provider(cls, data, use_json=True) as coinbase:
        currencies = coinbase.request_currencies()
        assert currencies == expected_currencies()
        assert coinbase.had_error is False


def test_eur_not_in_rates(mock_currency_provider, coinbase_data):
    cls = CoinbaseCurrencyProvider
    rates = {
        k: v for k, v in currency_data('USD')['rates'].items() if k != 'EUR'
    }
    data = coinbase_data('USD', rates)

    with mock_currency_provider(cls, data, use_json=True) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value) == 'EUR not base currency or not in rates'
        assert coinbase.had_error is True


@pytest.mark.parametrize('status_code', (300, 400, 500))
def test_response_code(mock_currency_provider, status_code):
    cls = CoinbaseCurrencyProvider
    with mock_currency_provider(
        cls, None, use_json=False, status=status_code
    ) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        exc_str = 'Response code not 2xx: {}'.format(status_code)
        assert str(excinfo.value) == exc_str
        assert coinbase.had_error is True


def test_no_response(mock_currency_provider):
    cls = CoinbaseCurrencyProvider
    with mock_currency_provider(
        cls, None, use_json=False, respond=False
    ) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value).startswith('Could not connect: ')
        assert coinbase.had_error is True


@pytest.mark.parametrize(
    'error_data, msg',
    (
        ({'errors': 'Something went wrong'}, 'Something went wrong'),
        (
            {'errors': {'message': 'Something else went wrong'}},
            'Something else went wrong',
        ),
    ),
)
def test_error(mock_currency_provider, error_data, msg):
    cls = CoinbaseCurrencyProvider
    with mock_currency_provider(cls, error_data, use_json=True) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value) == 'Error in response: {}'.format(msg)
        assert coinbase.had_error is True


def test_malformed_json(mock_currency_provider):
    cls = CoinbaseCurrencyProvider
    malformed_jsondata = {'some other fields': 'EUR', 'some fields': 1}

    with mock_currency_provider(
        cls, malformed_jsondata, use_json=True
    ) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value) == 'Missing keys from JSON response'
        assert coinbase.had_error is True


@pytest.mark.parametrize(
    'error_data,msg,use_json',
    (
        ('Some malformed not json data', 'Data is not a JSON', True),
        ('Some malformed not json data', 'Could not decode json data', False),
    ),
)
def test_malformed_data(mock_currency_provider, error_data, msg, use_json):
    cls = CoinbaseCurrencyProvider
    with mock_currency_provider(cls, error_data, use_json=use_json) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value) == msg
        assert coinbase.had_error is True
