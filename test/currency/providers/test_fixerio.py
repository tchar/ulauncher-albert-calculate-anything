from datetime import datetime
import pytest
from calculate_anything.currency.providers import FixerIOCurrencyProvider
from calculate_anything.exceptions import CurrencyProviderException
from test.tutils import currency_data, expected_currencies


def test_normal(mock_currency_provider, fixerio_data):
    cls = FixerIOCurrencyProvider
    timestamp = datetime.now().timestamp()
    rates = currency_data()['rates']
    data = fixerio_data('EUR', rates, timestamp)

    with mock_currency_provider(cls, data, use_json=True) as fixerio:
        currencies = fixerio.request_currencies()
        assert currencies == expected_currencies(timestamp=timestamp)
        assert fixerio.had_error is False


def test_other_base_currency(mock_currency_provider, fixerio_data):
    cls = FixerIOCurrencyProvider
    timestamp = datetime.now().timestamp()
    rates = currency_data('USD')['rates']
    data = fixerio_data('USD', rates, timestamp)

    with mock_currency_provider(cls, data, use_json=True) as fixerio:
        currencies = fixerio.request_currencies()
        assert currencies == expected_currencies(timestamp=timestamp)
        assert fixerio.had_error is False


def test_eur_not_in_rates(mock_currency_provider, fixerio_data):
    cls = FixerIOCurrencyProvider
    timestamp = datetime.now().timestamp()
    rates = {
        k: v for k, v in currency_data('USD')['rates'].items() if k != 'EUR'
    }
    data = fixerio_data('USD', rates, timestamp)

    with mock_currency_provider(cls, data, use_json=True) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == 'EUR not base currency or not in rates'
        assert fixerio.had_error is True


@pytest.mark.parametrize('status_code', (300, 400, 500))
def test_response_code(mock_currency_provider, status_code):
    cls = FixerIOCurrencyProvider
    with mock_currency_provider(
        cls, None, use_json=False, status=status_code
    ) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        exc_str = 'Response code not 2xx: {}'.format(status_code)
        assert str(excinfo.value) == exc_str
        assert fixerio.had_error is True


def test_no_response(mock_currency_provider):
    cls = FixerIOCurrencyProvider
    with mock_currency_provider(
        cls, None, use_json=False, respond=False
    ) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value).startswith('Could not connect: ')
        assert fixerio.had_error is True


@pytest.mark.parametrize(
    'error_data, msg',
    (
        (
            {'success': False, 'errors': {'error': 'Something went wrong'}},
            'Something went wrong',
        ),
        (
            {'success': False, 'errors': 'Something else went wrong'},
            'Something else went wrong',
        ),
    ),
)
def test_error(mock_currency_provider, error_data, msg):
    cls = FixerIOCurrencyProvider
    with mock_currency_provider(cls, error_data, use_json=True) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == 'Error in response: {}'.format(msg)
        assert fixerio.had_error is True


def test_malformed_json(mock_currency_provider):
    cls = FixerIOCurrencyProvider
    malformed_jsondata = {'some other fields': 'EUR', 'some fields': 1}

    with mock_currency_provider(
        cls, malformed_jsondata, use_json=True
    ) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == 'Missing keys from JSON response'
        assert fixerio.had_error is True


@pytest.mark.parametrize(
    'error_data,msg,use_json',
    (
        ('Some malformed not json data', 'Data is not a JSON', True),
        ('Some malformed not json data', 'Could not decode json data', False),
    ),
)
def test_malformed_data(mock_currency_provider, error_data, msg, use_json):
    cls = FixerIOCurrencyProvider
    with mock_currency_provider(cls, error_data, use_json=use_json) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == msg
        assert fixerio.had_error is True


def test_invalid_api_key(mock_currency_provider):
    cls = FixerIOCurrencyProvider
    with mock_currency_provider(
        cls, 'some data', use_json=True, api_key=None
    ) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == 'API Key is not valid'
        assert fixerio.had_error is True
