import pytest
from calculate_anything.exceptions import CurrencyProviderException
from tests.utils import currency_data, expected_currencies


def test_normal(mock_coinbase):
    data = {
        'data': {
            'currency': 'EUR',
            'rates': currency_data()['rates']
        }
    }

    with mock_coinbase(data, use_json=True) as coinbase:
        currencies = coinbase.request_currencies()
        assert currencies == expected_currencies()
        assert coinbase.had_error is False


def test_other_base_currency(mock_coinbase):
    data = {
        'data': {
            'currency': 'USD',
            'rates': currency_data('USD')['rates']
        }
    }

    with mock_coinbase(data, use_json=True) as coinbase:
        currencies = coinbase.request_currencies()
        assert currencies == expected_currencies()
        assert coinbase.had_error is False


def test_eur_not_in_rates(mock_coinbase):
    data = {
        'data': {
            'currency': 'USD',
            'rates': {
                k: v
                for k, v in currency_data('USD')['rates'].items()
                if k != 'EUR'}
        }
    }

    with mock_coinbase(data, use_json=True) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value) == 'EUR not base currency or not in rates'
        assert coinbase.had_error is True


@pytest.mark.parametrize('status_code', (300, 400, 500))
def test_response_code(mock_coinbase, status_code):
    with mock_coinbase(None, use_json=False, status=status_code) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        exc_str = 'Response code not 2xx: {}'.format(status_code)
        assert str(excinfo.value) == exc_str
        assert coinbase.had_error is True


def test_no_response(mock_coinbase):
    with mock_coinbase(None, use_json=False, respond=False) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value).startswith('Could not connect: ')
        assert coinbase.had_error is True


@pytest.mark.parametrize('error_data, msg', (
    ({'errors': 'Something went wrong'}, 'Something went wrong'),
    ({'errors': {'message': 'Something else went wrong'}},
     'Something else went wrong')
))
def test_error(mock_coinbase, error_data, msg):
    with mock_coinbase(error_data, use_json=True) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value) == 'Error in response: {}'.format(msg)
        assert coinbase.had_error is True


def test_malformed_json(mock_coinbase):
    malformed_jsondata = {
        'some other fields': 'EUR',
        'some fields': 1
    }

    with mock_coinbase(malformed_jsondata, use_json=True) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value) == 'Missing keys from JSON response'
        assert coinbase.had_error is True


@pytest.mark.parametrize('error_data,msg,use_json', (
    ('Some malformed not json data', 'Data is not a JSON', True),
    ('Some malformed not json data', 'Could not decode json data', False),
))
def test_malformed_data(mock_coinbase, error_data, msg, use_json):
    with mock_coinbase(error_data, use_json=use_json) as coinbase:
        with pytest.raises(CurrencyProviderException) as excinfo:
            coinbase.request_currencies()

        assert str(excinfo.value) == msg
        assert coinbase.had_error is True
