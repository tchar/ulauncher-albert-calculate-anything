import pytest
from calculate_anything.currency.providers import ECBCurrencyProvider
from calculate_anything.exceptions import CurrencyProviderException
from datetime import datetime
from test.tutils import currency_data, expected_currencies


def test_normal(mock_currency_provider, ecb_data):
    cls = ECBCurrencyProvider
    rates = currency_data()['rates']
    data = ecb_data(rates)

    with mock_currency_provider(cls, data, use_json=False) as ecb:
        currencies = ecb.request_currencies()
        timestamp = datetime.today().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        timestamp = timestamp.timestamp()
        assert currencies == expected_currencies(timestamp=timestamp)
        assert ecb.had_error is False


def test_malformed_time(mock_currency_provider, ecb_data):
    cls = ECBCurrencyProvider
    rates = currency_data()['rates']
    data = ecb_data(rates, 'Some time')
    with mock_currency_provider(cls, data, use_json=False) as ecb:
        currencies = ecb.request_currencies()
        timestamp = datetime.now().timestamp()
        assert currencies == expected_currencies(timestamp=timestamp)
        assert ecb.had_error is False


def test_malformed_partial_data(mock_currency_provider, ecb_data):
    cls = ECBCurrencyProvider
    rates = currency_data()['rates']
    rates = rates.copy()
    rates['USD'] = 'Some invalid rate'
    data = ecb_data(rates)

    with mock_currency_provider(cls, data, use_json=False) as ecb:
        currencies = ecb.request_currencies()
        timestamp = datetime.today().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        timestamp = timestamp.timestamp()
        assert currencies == expected_currencies(
            timestamp=timestamp, filterc=['USD']
        )
        assert ecb.had_error is False


@pytest.mark.parametrize('status_code', (300, 400, 500))
def test_response_code(mock_currency_provider, status_code):
    cls = ECBCurrencyProvider
    with mock_currency_provider(
        cls, None, status=status_code, use_json=False
    ) as ecb:
        with pytest.raises(CurrencyProviderException) as excinfo:
            ecb.request_currencies()

        exc_str = 'Response code not 2xx ({})'.format(status_code)
        assert str(excinfo.value) == exc_str
        assert ecb.had_error is True


def test_no_response(mock_currency_provider):
    cls = ECBCurrencyProvider
    with mock_currency_provider(
        cls, None, respond=False, use_json=False
    ) as ecb:
        with pytest.raises(CurrencyProviderException) as excinfo:
            ecb.request_currencies()

        assert str(excinfo.value).startswith('Could not connect: ')
        assert ecb.had_error is True


def test_no_xml_children(mock_currency_provider):
    cls = ECBCurrencyProvider
    data = '''
    <gesmes:Envelope xmlns:gesmes="http://www.gesmes.org/xml/2002-08-01"
        xmlns="http://www.ecb.int/vocabulary/2002-08-01/eurofxref">
        <gesmes:subject>Reference rates</gesmes:subject>
    <gesmes:Sender>
        <gesmes:name>European Central Bank</gesmes:name>
    </gesmes:Sender>
    <Cube>
    </Cube>
    </gesmes:Envelope>
    '''

    with mock_currency_provider(cls, data, use_json=False) as ecb:
        with pytest.raises(CurrencyProviderException) as excinfo:
            ecb.request_currencies()

            assert str(excinfo.value).startswith('XML data not as expected: ')
            assert ecb.had_error is True


def test_malformed_data(mock_currency_provider, ecb_data):
    cls = ECBCurrencyProvider
    rates = currency_data()['rates']
    with mock_currency_provider(
        cls, ecb_data(rates) + 'junk', use_json=False
    ) as ecb:
        with pytest.raises(CurrencyProviderException) as excinfo:
            ecb.request_currencies()

        assert str(excinfo.value).startswith(
            'Could not parse ECB xml response: '
        )
        assert ecb.had_error is True
