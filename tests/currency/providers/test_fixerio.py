from datetime import datetime
import pytest
from calculate_anything.exceptions import CurrencyProviderException
from tests.utils import currency_data, expected_currencies


def test_normal(mock_fixerio):
    timestamp = datetime.now().timestamp()
    data = {
        'success': True,
        'timestamp': timestamp,
        'base': 'EUR',
        'rates': currency_data()['rates']
    }

    with mock_fixerio(data, use_json=True) as fixerio:
        currencies = fixerio.request_currencies()
        assert currencies == expected_currencies(timestamp=timestamp)
        assert fixerio.had_error is False


def test_other_base_currency(mock_fixerio):
    timestamp = datetime.now().timestamp()
    data = {
        'success': True,
        'timestamp': timestamp,
        'base': 'USD',
        'rates': currency_data('USD')['rates']
    }

    with mock_fixerio(data, use_json=True) as fixerio:
        currencies = fixerio.request_currencies()
        assert currencies == expected_currencies(timestamp=timestamp)
        assert fixerio.had_error is False


def test_eur_not_in_rates(mock_fixerio):
    data = {
        'success': True,
        'base': 'USD',
        'rates': {
            k: v
            for k, v in currency_data('USD')['rates'].items()
            if k != 'EUR'}
    }

    with mock_fixerio(data, use_json=True) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == 'EUR not base currency or not in rates'
        assert fixerio.had_error is True


@pytest.mark.parametrize('status_code', (300, 400, 500))
def test_response_code(mock_fixerio, status_code):
    with mock_fixerio(None, use_json=False, status=status_code) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        exc_str = 'Response code not 2xx: {}'.format(status_code)
        assert str(excinfo.value) == exc_str
        assert fixerio.had_error is True


def test_no_response(mock_fixerio):
    with mock_fixerio(None, use_json=False, respond=False) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value).startswith('Could not connect: ')
        assert fixerio.had_error is True


@pytest.mark.parametrize('error_data, msg', (
    ({'success': False, 'errors': {'error': 'Something went wrong'}},
     'Something went wrong'),
    ({'success': False, 'errors': 'Something else went wrong'},
     'Something else went wrong')
))
def test_error(mock_fixerio, error_data, msg):
    with mock_fixerio(error_data, use_json=True) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == 'Error in response: {}'.format(msg)
        assert fixerio.had_error is True


def test_malformed_json(mock_fixerio):
    malformed_jsondata = {
        'some other fields': 'EUR',
        'some fields': 1
    }

    with mock_fixerio(malformed_jsondata, use_json=True) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == 'Missing keys from JSON response'
        assert fixerio.had_error is True


@pytest.mark.parametrize('error_data,msg,use_json', (
    ('Some malformed not json data', 'Data is not a JSON', True),
    ('Some malformed not json data', 'Could not decode json data', False),
))
def test_malformed_data(mock_fixerio, error_data, msg, use_json):
    with mock_fixerio(error_data, use_json=use_json) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == msg
        assert fixerio.had_error is True


def test_invalid_api_key(mock_fixerio):
    with mock_fixerio('some data', use_json=True, api_key=None) as fixerio:
        with pytest.raises(CurrencyProviderException) as excinfo:
            fixerio.request_currencies()

        assert str(excinfo.value) == 'API Key is not valid'
        assert fixerio.had_error is True
