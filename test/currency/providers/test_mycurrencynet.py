import pytest
from calculate_anything.currency.providers import MyCurrencyNetCurrencyProvider
from calculate_anything.exceptions import CurrencyProviderException
from test.tutils import currency_data, expected_currencies


def test_normal(mock_currency_provider, mycurrencynet_data):
    cls = MyCurrencyNetCurrencyProvider
    rates = [
        {'currency_code': k, 'rate': v}
        for k, v in currency_data()['rates'].items()
    ]
    data = mycurrencynet_data('EUR', rates)

    with mock_currency_provider(cls, data, use_json=True) as mycurrencynet:
        currencies = mycurrencynet.request_currencies()
        assert currencies == expected_currencies()
        assert mycurrencynet.had_error is False


def test_other_base_currency(mock_currency_provider, mycurrencynet_data):
    cls = MyCurrencyNetCurrencyProvider
    rates = [
        {'currency_code': k, 'rate': v}
        for k, v in currency_data('USD')['rates'].items()
    ]
    data = mycurrencynet_data('USD', rates)

    with mock_currency_provider(cls, data, use_json=True) as mycurrencynet:
        currencies = mycurrencynet.request_currencies()
        assert currencies == expected_currencies()
        assert mycurrencynet.had_error is False


def test_missing_fields(mock_currency_provider, mycurrencynet_data):
    cls = MyCurrencyNetCurrencyProvider
    rates = [
        (
            {'currency_code': k, 'rate': v}
            if k != 'USD'
            else {'missing_code': k, 'rate': v}
        )
        for k, v in currency_data()['rates'].items()
    ]
    data = mycurrencynet_data('EUR', rates)

    with mock_currency_provider(cls, data, use_json=True) as mycurrencynet:
        currencies = mycurrencynet.request_currencies()
        assert currencies == expected_currencies(filterc=['USD'])
        assert mycurrencynet.had_error is False


def test_eur_not_in_rates(mock_currency_provider, mycurrencynet_data):
    cls = MyCurrencyNetCurrencyProvider
    rates = [
        {'currency_code': k, 'rate': v}
        for k, v in currency_data('USD')['rates'].items()
        if k != 'EUR'
    ]
    data = mycurrencynet_data('USD', rates)

    with mock_currency_provider(cls, data, use_json=True) as mycurrencynet:
        with pytest.raises(CurrencyProviderException) as excinfo:
            mycurrencynet.request_currencies()

        assert str(excinfo.value) == 'EUR not base currency or not in rates'
        assert mycurrencynet.had_error is True


@pytest.mark.parametrize('status_code', (300, 400, 500))
def test_response_code(mock_currency_provider, status_code):
    cls = MyCurrencyNetCurrencyProvider
    with mock_currency_provider(
        cls, None, use_json=False, status=status_code
    ) as mycurrencynet:
        with pytest.raises(CurrencyProviderException) as excinfo:
            mycurrencynet.request_currencies()

        exc_str = 'Response code not 2xx: {}'.format(status_code)
        assert str(excinfo.value) == exc_str
        assert mycurrencynet.had_error is True


def test_no_response(mock_currency_provider):
    cls = MyCurrencyNetCurrencyProvider
    with mock_currency_provider(
        cls, None, use_json=False, respond=False
    ) as mycurrencynet:
        with pytest.raises(CurrencyProviderException) as excinfo:
            mycurrencynet.request_currencies()

        assert str(excinfo.value).startswith('Could not connect: ')
        assert mycurrencynet.had_error is True


def test_malformed_json(mock_currency_provider):
    cls = MyCurrencyNetCurrencyProvider
    malformed_jsondata = {'some other fields': 'EUR', 'some fields': 1}

    with mock_currency_provider(
        cls, malformed_jsondata, use_json=True
    ) as mycurrencynet:
        with pytest.raises(CurrencyProviderException) as excinfo:
            mycurrencynet.request_currencies()

        assert str(excinfo.value) == 'Missing keys from JSON response'
        assert mycurrencynet.had_error is True


@pytest.mark.parametrize(
    'error_data,msg,use_json',
    (
        ('Some malformed not json data', 'Data is not a JSON', True),
        ('Some malformed not json data', 'Could not decode json data', False),
    ),
)
def test_malformed_data(mock_currency_provider, error_data, msg, use_json):
    cls = MyCurrencyNetCurrencyProvider
    with mock_currency_provider(
        cls, error_data, use_json=use_json
    ) as mycurrencynet:
        with pytest.raises(CurrencyProviderException) as excinfo:
            mycurrencynet.request_currencies()

        assert str(excinfo.value) == msg
        assert mycurrencynet.had_error is True
