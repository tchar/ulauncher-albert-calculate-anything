from calculate_anything.exceptions import CurrencyProviderException
from datetime import datetime

import pytest
# import pytest
from tests.utils import currency_data, expected_currencies


def xmldata(rates, time=datetime.today().strftime('%Y-%m-%d')):
    rates = ((k, v) for k, v in rates.items() if k != 'EUR')
    rates = ['<Cube currency="{}" rate="{}"/>'.format(c, r) for c, r in rates]
    rates = '\n'.join(rates)

    return '''
    <gesmes:Envelope xmlns:gesmes="http://www.gesmes.org/xml/2002-08-01"
        xmlns="http://www.ecb.int/vocabulary/2002-08-01/eurofxref">
        <gesmes:subject>Reference rates</gesmes:subject>
    <gesmes:Sender>
        <gesmes:name>European Central Bank</gesmes:name>
    </gesmes:Sender>
    <Cube>
        <Cube time="{}">
            {}
        </Cube>
    </Cube>
    </gesmes:Envelope>
    '''.format(time, rates)


def test_normal(mock_ecb):
    rates = currency_data()['rates']
    with mock_ecb(data=xmldata(rates)) as ecb:
        currencies = ecb.request_currencies()
        timestamp = datetime.today().replace(hour=0, minute=0,
                                             second=0, microsecond=0)
        timestamp = timestamp.timestamp()
        assert currencies == expected_currencies(timestamp=timestamp)
        assert ecb.had_error is False


def test_malformed_time(mock_ecb):
    rates = currency_data()['rates']
    with mock_ecb(data=xmldata(rates, 'Some time')) as ecb:
        currencies = ecb.request_currencies()
        timestamp = datetime.now().timestamp()
        assert currencies == expected_currencies(timestamp=timestamp)
        assert ecb.had_error is False


def test_malformed_partial_data(mock_ecb):
    rates = currency_data()['rates']
    rates = rates.copy()
    rates['USD'] = 'Some invalid rate'

    with mock_ecb(data=xmldata(rates)) as ecb:
        currencies = ecb.request_currencies()
        timestamp = datetime.today().replace(hour=0, minute=0,
                                             second=0, microsecond=0)
        timestamp = timestamp.timestamp()
        assert currencies == expected_currencies(
            timestamp=timestamp, filterc=['USD'])
        assert ecb.had_error is False


@pytest.mark.parametrize('status_code', (300, 400, 500))
def test_response_code(mock_ecb, status_code):
    with mock_ecb(None, status=status_code) as ecb:
        with pytest.raises(CurrencyProviderException) as excinfo:
            ecb.request_currencies()

        exc_str = 'Response code not 2xx ({})'.format(status_code)
        assert str(excinfo.value) == exc_str
        assert ecb.had_error is True


def test_no_response(mock_ecb):
    with mock_ecb(None, respond=False) as ecb:
        with pytest.raises(CurrencyProviderException) as excinfo:
            ecb.request_currencies()

        assert str(excinfo.value).startswith('Could not connect: ')
        assert ecb.had_error is True


def test_no_xml_children(mock_ecb):
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

    with mock_ecb(data=data) as ecb:
        with pytest.raises(CurrencyProviderException) as excinfo:
            ecb.request_currencies()

            assert str(excinfo.value).startswith('XML data not as expected: ')
            assert ecb.had_error is True


def test_malformed_data(mock_ecb):
    rates = currency_data()['rates']
    with mock_ecb(data=xmldata(rates) + 'somestring') as ecb:
        with pytest.raises(CurrencyProviderException) as excinfo:
            ecb.request_currencies()

        assert str(excinfo.value).startswith(
            'Could not parse ECB xml response: ')
        assert ecb.had_error is True
