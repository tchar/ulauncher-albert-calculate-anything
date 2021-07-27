import locale
import time
from datetime import datetime
from calculate_anything.currency import CurrencyService
import pytest
from calculate_anything.lang import LanguageService
from calculate_anything.units import UnitsService
from calculate_anything.query.handlers.units import UnitsQueryHandler
from calculate_anything.exceptions import (
    MissingPintException, MissingRequestsException, CurrencyProviderException
)
from tests.utils import (
    approxunits, currency_provider_had_error,
    no_pint, no_requests, query_test_helper
)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

LanguageService().set('en_US')
UnitsService().start()
CurrencyService().set_default_currencies(
    ['EUR', 'USD', 'BTC', 'CAD']).enable_cache(86400).start()
while CurrencyService()._cache._data['exchange_rates'] == {}:
    time.sleep(0.1)
    cache_data = CurrencyService()._cache._data['exchange_rates']
tr_err = LanguageService().get_translator('errors')
Quantity = UnitsService().unit_registry.Quantity


def get_unit_result(parsed_query, value, name, description,
                    order=0, icon='images/convert.svg', error=None):
    return {
        'result': {
            'query': parsed_query,
            'value': value,
            'error': error,
            'order': order
        },
        'query_result': {
            'icon': icon,
            'name': name,
            'description': description,
            'clipboard': name,
            'error': error,
            'order': order,
            'value': value,
            'value_type': Quantity
        }
    }


def currency_amount(amount, currency_from, currency_to, quantity):
    amount_from = cache_data[currency_from]['rate']
    amount_to = cache_data[currency_to]['rate']
    amount *= amount_to / amount_from
    if quantity:
        return Quantity(amount, 'currency_{}'.format(currency_to))
    amount = locale.currency(amount, symbol='', grouping=True)
    return '{} {}'.format(amount, currency_to)


def currency_description(currency_from, currency_to):
    dt = datetime.fromtimestamp(cache_data[currency_to]['timestamp_refresh'])
    dt = dt.strftime('%Y-%m-%d %H:%M')
    amount = currency_amount(1, currency_from, currency_to, True)
    return '1 {} = {:.6f} {} as of {}'.format(currency_from, amount.magnitude,
                                              currency_to, dt)


test_spec_units_simple = [{
    # Simple test - 1
    'query': '= 1 cm to m',
    'results': [
        get_unit_result(
            '1 centimeter to meter', approxunits(Quantity(0.01, 'meter')),
            '0.01 meter', '1 centimeter = 0.01 meter • [length]'
        ),
    ]
}, {
    # Simple test - 2
    'query': '= 10 c to f',
    'results': [
        get_unit_result(
            '10 degree_Celsius to degree_Fahrenheit',
            approxunits(Quantity(50.0, 'degree_Fahrenheit')),
            '50 degree Fahrenheit', '[temperature]'
        ),
    ]
}, {
    # Simple test - 2
    'query': '= 27.75 kg to pounds',
    'results': [
        get_unit_result(
            '27.75 kilogram to pound', approxunits(Quantity(61.18, 'pound')),
            '61.1783 pound', '1 kilogram = 2.20462 pound • [mass]'
        ),
    ]
}, {
    # Simple test - 4
    'query': '= 5400 second to h',
    'results': [
        get_unit_result(
            '5400 second to hour', approxunits(Quantity(1.5, 'hour')),
            '1.5 hour', '1 second = 0.000277778 hour • [time]'
        ),
    ]
}, {
    # Simple test - 1
    'query': '= 150000000 b to mb',
    'results': [
        get_unit_result(
            '150000000 byte to megabyte', approxunits(
                Quantity(150, 'megabyte')),
            '150 megabyte', ''
        ),
    ]
}, ]


@pytest.mark.parametrize('test_spec', test_spec_units_simple)
def test_units_simple(test_spec):
    query_test_helper(UnitsQueryHandler, test_spec)


test_spec_units_multi = [{
    # Multi - 1
    'query': '= 10 cm to m, in, feet, km',
    'results': [
        get_unit_result(
            '10 centimeter to meter', approxunits(Quantity(0.1, 'meter')),
            '0.1 meter', '1 centimeter = 0.01 meter • [length]', order=0
        ),
        get_unit_result(
            '10 centimeter to inch', approxunits(Quantity(3.937, 'inch')),
            '3.93701 inch', '1 centimeter = 0.393701 inch • [length]', order=1
        ),
        get_unit_result(
            '10 centimeter to foot', approxunits(Quantity(0.3281, 'foot')),
            '0.328084 foot', '1 centimeter = 0.0328084 foot • [length]',
            order=2
        ),
        get_unit_result(
            '10 centimeter to kilometer', approxunits(
                Quantity(0.0001, 'kilometer')),
            '0.0001 kilometer', '1 centimeter = 1e-05 kilometer • [length]',
            order=3
        ),
    ]
}, {
    # Multi - 2
    'query': '= 0.547 km/h to in/minute, mile/s, cm/min, foot/s',
    'results': [
        get_unit_result(
            '0.547 kilometer / hour to inch / minute',
            approxunits(Quantity(358.92, 'inch / minute')),
            '358.924 inch / minute', '1 kilometer / hour = '
            '656.168 inch / minute • [length / time]'
        ),
        get_unit_result(
            '0.547 kilometer / hour to mile / second',
            approxunits(Quantity(0.000094, 'mile / second')),
            '9.44139e-05 mile / second',
            '1 kilometer / hour = 0.000172603 mile / second • [length / time]',
            order=1
        ),
        get_unit_result(
            '0.547 kilometer / hour to centimeter / minute',
            approxunits(Quantity(911.67, 'centimetre / minute')),
            '911.667 centimeter / minute',
            '1 kilometer / hour = '
            '1666.67 centimeter / minute • [length / time]',
            order=2
        ),
        get_unit_result(
            '0.547 kilometer / hour to foot / second',
            approxunits(Quantity(0.4985, 'foot / second')),
            '0.498505 foot / second',
            '1 kilometer / hour = 0.911344 foot / second • [length / time]',
            order=3
        ),
    ]
}, {
    # Multi - 3
    'query': '= 100 mb /s m to b/min cm, km gb/hour, in pb/day',
    'results': [
        get_unit_result(
            '100.0 megabyte * meter / second to byte * centimeter / minute',
            approxunits(Quantity(6e+11, 'byte * centimeter / minute')),
            '6e+11 byte * centimeter / minute',
            '1 megabyte * meter / second = '
            '6e+09 byte * centimeter / minute • [length / time]',
        ),
        get_unit_result(
            '100.0 megabyte * meter / second to gigabyte * kilometer / hour',
            approxunits(Quantity(0.36, 'gigabyte * kilometer / hour')),
            '0.36 gigabyte * kilometer / hour',
            '1 megabyte * meter / second = '
            '0.0036 gigabyte * kilometer / hour • [length / time]',
            order=1
        ),
        get_unit_result(
            '100.0 megabyte * meter / second to inch * petabyte / day',
            approxunits(Quantity(0.34015748, 'inch * petabyte / day')),
            '0.340157 inch * petabyte / day',
            '1 megabyte * meter / second = '
            '0.00340157 inch * petabyte / day • [length / time]',
            order=2
        ),
    ]
}, ]


@pytest.mark.parametrize('test_spec', test_spec_units_multi)
def test_units_multi(test_spec):
    query_test_helper(UnitsQueryHandler, test_spec)


test_spec_currency = [{
    'query': '= 10,000 MXN',
    'results': [
        get_unit_result(
            '10000 currency_MXN to currency_EUR',
            approxunits(currency_amount(10000, 'MXN', 'EUR', True)),
            currency_amount(10000, 'MXN', 'EUR', False),
            currency_description('MXN', 'EUR'),
            order=0, icon='images/flags/EUR.svg'
        ),
        get_unit_result(
            '10000 currency_MXN to currency_USD',
            approxunits(currency_amount(10000, 'MXN', 'USD', True)),
            currency_amount(10000, 'MXN', 'USD', False),
            currency_description('MXN', 'USD'),
            order=1, icon='images/flags/USD.svg'
        ),
        get_unit_result(
            '10000 currency_MXN to currency_BTC',
            approxunits(currency_amount(10000, 'MXN', 'BTC', True)),
            currency_amount(10000, 'MXN', 'BTC', False),
            currency_description('MXN', 'BTC'),
            order=2, icon='images/flags/BTC.svg'
        ),
        get_unit_result(
            '10000 currency_MXN to currency_CAD',
            approxunits(currency_amount(10000, 'MXN', 'CAD', True)),
            currency_amount(10000, 'MXN', 'CAD', False),
            currency_description('MXN', 'CAD'),
            order=3, icon='images/flags/CAD.svg'
        ),
        get_unit_result(
            '10000 currency_MXN to currency_MXN',
            approxunits(Quantity(10000, 'currency_MXN')),
            '10,000.00 MXN', '',
            order=4, icon='images/flags/MXN.svg'
        ),
    ]
}, {
    'query': '= 7.277 AMD to RON',
    'results': [
        get_unit_result(
            '7.277 currency_AMD to currency_RON',
            approxunits(currency_amount(7.277, 'AMD', 'RON', True)),
            currency_amount(7.277, 'AMD', 'RON', False),
            currency_description('AMD', 'RON'),
            order=0, icon='images/flags/RON.svg'
        ),
        get_unit_result(
            '7.277 currency_AMD to currency_AMD',
            approxunits(Quantity(7.277, 'currency_AMD')),
            '7.28 AMD', '',
            order=1, icon='images/flags/AMD.svg'
        ), ]
}, {
    # Only one result (do not show duplicate 10 CAD)
    'query': '= 10 CAD to CAD',
    'results': [
        get_unit_result(
            '10 currency_CAD to currency_CAD',
            approxunits(currency_amount(10, 'CAD', 'CAD', True)),
            '10.00 CAD', '', order=0, icon='images/flags/CAD.svg'
        ),
    ]
}, {
    'query': '= 0.1 BTC to cad,EUR,USD,AED',
    'results': [
        get_unit_result(
            '0.1 currency_BTC to currency_CAD',
            approxunits(currency_amount(0.1, 'BTC', 'CAD', True)),
            currency_amount(0.1, 'BTC', 'CAD', False),
            currency_description('BTC', 'CAD'),
            order=0, icon='images/flags/CAD.svg'
        ),
        get_unit_result(
            '0.1 currency_BTC to currency_EUR',
            approxunits(currency_amount(0.1, 'BTC', 'EUR', True)),
            currency_amount(0.1, 'BTC', 'EUR', False),
            currency_description('BTC', 'EUR'),
            order=1, icon='images/flags/EUR.svg'
        ),
        get_unit_result(
            '0.1 currency_BTC to currency_USD',
            approxunits(currency_amount(0.1, 'BTC', 'USD', True)),
            currency_amount(0.1, 'BTC', 'USD', False),
            currency_description('BTC', 'USD'),
            order=2, icon='images/flags/USD.svg'
        ),
        get_unit_result(
            '0.1 currency_BTC to currency_AED',
            approxunits(currency_amount(0.1, 'BTC', 'AED', True)),
            currency_amount(0.1, 'BTC', 'AED', False),
            currency_description('BTC', 'AED'),
            order=3, icon='images/flags/AED.svg'
        ),
        get_unit_result(
            '0.1 currency_BTC to currency_BTC',
            approxunits(Quantity(0.1, 'currency_BTC')),
            '0.10 BTC', '',
            order=4, icon='images/flags/BTC.svg'
        ),
    ]
}]


@pytest.mark.parametrize('test_spec', test_spec_currency)
def test_currency(test_spec):
    query_test_helper(UnitsQueryHandler, test_spec)


test_spec_missing_pint = [{
    'query': '= 10 meters to decimeters',
    'results': [{
        'result': {
            'query': '',
            'value': None,
            'error': MissingPintException,
            'order': -1020
        },
        'query_result': {
            'icon': 'images/convert.svg',
            'name': tr_err('missing-pint-error'),
            'description': tr_err('missing-pint-error-description'),
            'clipboard': 'pip install Pint',
            'error': MissingPintException,
            'order': -1020,
            'value': None,
            'value_type': type(None)
        }
    }]
}]


@pytest.mark.parametrize('test_spec', test_spec_missing_pint)
def test_missing_pint(test_spec):
    with no_pint(units_service=True):
        query_test_helper(UnitsQueryHandler, test_spec)

    with no_pint(units_service=False):
        query_test_helper(UnitsQueryHandler, test_spec)


test_spec_missing_requests = [{
    'query': '= 10 CAD',
    'results': [{
        'result': {
            'query': '',
            'value': None,
            'error': MissingRequestsException,
            'order': -1030
        },
        'query_result': {
            'icon': 'images/icon.svg',
            'name': tr_err('missing-requests-error'),
            'description': tr_err('missing-requests-error-description'),
            'clipboard': 'pip install requests',
            'error': MissingRequestsException,
            'order': -1030,
            'value': None,
            'value_type': type(None)
        }
    }]
}]


@pytest.mark.parametrize('test_spec', test_spec_missing_requests)
def test_missing_requests(test_spec):
    with no_requests():
        query_test_helper(UnitsQueryHandler, test_spec)


test_spec_provider_had_error = [{
    'query': '= 10 CAD',
    'results': [{
        'result': {
            'query': '',
            'value': None,
            'error': CurrencyProviderException,
            'order': -60
        },
        'query_result': {
            'icon': 'images/icon.svg',
            'name': tr_err('currency-provider-error'),
            'description': tr_err('currency-provider-error-description'),
            'clipboard': '',
            'error': CurrencyProviderException,
            'order': -60,
            'value': None,
            'value_type': type(None)
        }
    }]
}]


@pytest.mark.parametrize('test_spec', test_spec_provider_had_error)
def test_provider_had_error(test_spec):
    with currency_provider_had_error():
        query_test_helper(UnitsQueryHandler, test_spec)
