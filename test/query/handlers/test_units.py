import locale
import pytest
from datetime import datetime
from calculate_anything.lang import LanguageService
from calculate_anything.units import UnitsService
from calculate_anything.preferences import Preferences
from calculate_anything.query.handlers import MultiHandler
from calculate_anything.query.handlers import UnitsQueryHandler
from calculate_anything.utils import images_dir
from calculate_anything.exceptions import (
    MissingPintException,
    CurrencyProviderException,
    ZeroDivisionException,
)
from test.tutils import (
    approxunits,
    extra_translations,
    no_pint,
    query_test_helper,
)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

LanguageService().set('en_US')
UnitsService().start()
default_currencies = ['EUR', 'USD', 'BTC', 'CAD']
tr_err = LanguageService().get_translator('errors')


def get_unit_result(Q):
    def _get_unit_result(
        parsed_query,
        value,
        name,
        description,
        order=0,
        icon=images_dir('convert.svg'),
        error=None,
    ):
        return {
            'result': {
                'query': parsed_query,
                'value': value,
                'error': error,
                'order': order,
            },
            'query_result': {
                'icon': icon,
                'name': name,
                'description': description,
                'clipboard': name,
                'error': error,
                'order': order,
                'value': value,
                'value_type': Q,
            },
        }

    return _get_unit_result


def currency_amount(Q, data):
    def _currency_amount(amount, currency_from, currency_to, quantity):
        amount_from = data[currency_from]['rate']
        amount_to = data[currency_to]['rate']
        amount *= amount_to / amount_from
        if quantity:
            return Q(amount, 'currency_{}'.format(currency_to))
        amount = locale.currency(amount, symbol='', grouping=True)
        return '{} {}'.format(amount, currency_to)

    return _currency_amount


def currency_description(Q, data):
    def _currency_description(currency_from, currency_to):
        dt = datetime.fromtimestamp(data[currency_to]['timestamp_refresh'])
        dt = dt.strftime('%Y-%m-%d %H:%M')
        amount = currency_amount(Q, data)(1, currency_from, currency_to, True)
        msg = '1 {} = {:.6f} {} as of {}'
        msg = msg.format(currency_from, amount.magnitude, currency_to, dt)
        return msg

    return _currency_description


test_spec_units_simple = [
    lambda Q: {
        # Simple test - 1
        'query': '= 1 m',
        'results': [
            get_unit_result(Q)(
                '1 meter to meter',
                approxunits(Q(1, 'meter')),
                '1 meter',
                '[length]',
            ),
        ],
    },
    lambda Q: {
        # Simple test - 2
        'query': '= 1 cm to m',
        'results': [
            get_unit_result(Q)(
                '1 centimeter to meter',
                approxunits(Q(0.01, 'meter')),
                '0.01 meter',
                '1 centimeter = 0.01 meter • [length]',
            ),
        ],
    },
    lambda Q: {
        # Simple test - 3
        'query': '= 10 c to f',
        'results': [
            get_unit_result(Q)(
                '10 degree_Celsius to degree_Fahrenheit',
                approxunits(Q(50.0, 'degree_Fahrenheit')),
                '50 degree Fahrenheit',
                '[temperature]',
            ),
        ],
    },
    lambda Q: {
        # Simple test - 4
        'query': '= 27.75 kg to pounds',
        'results': [
            get_unit_result(Q)(
                '27.75 kilogram to pound',
                approxunits(Q(61.18, 'pound')),
                '61.1783 pound',
                '1 kilogram = 2.20462 pound • [mass]',
            ),
        ],
    },
    lambda Q: {
        # Simple test - 5
        'query': '= 5400 second to h',
        'results': [
            get_unit_result(Q)(
                '5400 second to hour',
                approxunits(Q(1.5, 'hour')),
                '1.5 hour',
                '1 second = 0.000277778 hour • [time]',
            ),
        ],
    },
    lambda Q: {
        # Simple test - 6
        'query': '= 150000000 b to mb',
        'results': [
            get_unit_result(Q)(
                '150000000 byte to megabyte',
                approxunits(Q(150, 'megabyte')),
                '150 megabyte',
                '',
            ),
        ],
    },
    lambda _: {
        # Test zero division error
        'query': '= 10 / 0 meters to decimeters',
        'results': [
            {
                'result': {
                    'query': '10 / 0 meters to decimeters',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('convert.svg'),
                    'name': tr_err('zero-division-error'),
                    'description': tr_err('zero-division-error-description'),
                    'clipboard': '',
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_units_simple)
def test_units_simple(mock_currency_service, test_spec):
    with mock_currency_service(default_currencies, error=False):
        Quantity = UnitsService().unit_registry.Quantity
        test_spec = test_spec(Quantity)
        query_test_helper(UnitsQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_units_multi = [
    lambda Q: {
        # Multi - 1
        'query': '= 10 cm to m, in, feet, km',
        'results': [
            get_unit_result(Q)(
                '10 centimeter to meter',
                approxunits(Q(0.1, 'meter')),
                '0.1 meter',
                '1 centimeter = 0.01 meter • [length]',
                order=0,
            ),
            get_unit_result(Q)(
                '10 centimeter to inch',
                approxunits(Q(3.937, 'inch')),
                '3.93701 inch',
                '1 centimeter = 0.393701 inch • [length]',
                order=1,
            ),
            get_unit_result(Q)(
                '10 centimeter to foot',
                approxunits(Q(0.3281, 'foot')),
                '0.328084 foot',
                '1 centimeter = 0.0328084 foot • [length]',
                order=2,
            ),
            get_unit_result(Q)(
                '10 centimeter to kilometer',
                approxunits(Q(0.0001, 'kilometer')),
                '0.0001 kilometer',
                '1 centimeter = 1e-05 kilometer • [length]',
                order=3,
            ),
        ],
    },
    lambda Q: {
        # Multi - 2
        'query': '= 0.547 km/h to in/minute, mile/s, cm/min, foot/s',
        'results': [
            get_unit_result(Q)(
                '0.547 kilometer / hour to inch / minute',
                approxunits(Q(358.92, 'inch / minute')),
                '358.924 inch / minute',
                '1 kilometer / hour = '
                '656.168 inch / minute • [length / time]',
            ),
            get_unit_result(Q)(
                '0.547 kilometer / hour to mile / second',
                approxunits(Q(0.000094, 'mile / second')),
                '9.44139e-05 mile / second',
                '1 kilometer / hour = 0.000172603 '
                'mile / second • [length / time]',
                order=1,
            ),
            get_unit_result(Q)(
                '0.547 kilometer / hour to centimeter / minute',
                approxunits(Q(911.67, 'centimetre / minute')),
                '911.667 centimeter / minute',
                '1 kilometer / hour = '
                '1666.67 centimeter / minute • [length / time]',
                order=2,
            ),
            get_unit_result(Q)(
                '0.547 kilometer / hour to foot / second',
                approxunits(Q(0.4985, 'foot / second')),
                '0.498505 foot / second',
                '1 kilometer / hour = 0.911344 '
                'foot / second • [length / time]',
                order=3,
            ),
        ],
    },
    lambda Q: {
        # Multi - 3
        'query': '= 100 mb /s m to b/min cm, km gb/hour, in pb/day',
        'results': [
            get_unit_result(Q)(
                '100.0 megabyte * meter / second to '
                'byte * centimeter / minute',
                approxunits(Q(6e11, 'byte * centimeter / minute')),
                '6e+11 byte * centimeter / minute',
                '1 megabyte * meter / second = '
                '6e+09 byte * centimeter / minute • [length / time]',
            ),
            get_unit_result(Q)(
                '100.0 megabyte * meter / second to '
                'gigabyte * kilometer / hour',
                approxunits(Q(0.36, 'gigabyte * kilometer / hour')),
                '0.36 gigabyte * kilometer / hour',
                '1 megabyte * meter / second = '
                '0.0036 gigabyte * kilometer / hour • [length / time]',
                order=1,
            ),
            get_unit_result(Q)(
                '100.0 megabyte * meter / second to inch * petabyte / day',
                approxunits(Q(0.34015748, 'inch * petabyte / day')),
                '0.340157 inch * petabyte / day',
                '1 megabyte * meter / second = '
                '0.00340157 inch * petabyte / day • [length / time]',
                order=2,
            ),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_units_multi)
def test_units_multi(test_spec, mock_currency_service):
    with mock_currency_service(default_currencies, error=False):
        Quantity = UnitsService().unit_registry.Quantity
        test_spec = test_spec(Quantity)
        query_test_helper(UnitsQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_units_mode_crazy = [
    lambda Q: {
        # Simple test - 1
        'query': '= 1 m',
        'results': [
            get_unit_result(Q)(
                '1 meter to meter',
                approxunits(Q(1, 'meter')),
                '1 meter',
                '[length]',
            ),
            get_unit_result(Q)(
                '1 molar to molar',
                approxunits(Q(1, 'molar')),
                '1 molar',
                '[substance / length ^ 3]',
                1,
            ),
        ],
    },
    lambda Q: {
        # Simple test - 2
        'query': '= 1 cm to m',
        'results': [
            get_unit_result(Q)(
                '1 centimeter to meter',
                approxunits(Q(0.01, 'meter')),
                '0.01 meter',
                '1 centimeter = 0.01 meter • [length]',
            ),
            get_unit_result(Q)(
                '1 centimolar to molar',
                approxunits(Q(0.01, 'molar')),
                '0.01 molar',
                '1 centimolar = 0.01 molar • [substance / length ^ 3]',
                1,
            ),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_units_mode_crazy)
def test_units_mode_crazy(test_spec, mock_currency_service):
    with mock_currency_service(default_currencies, error=False):
        # Set crazy mode
        preferences = Preferences()
        preferences.units.set_conversion_mode('crazy')
        preferences.commit()

        Quantity = UnitsService().unit_registry.Quantity
        test_spec = test_spec(Quantity)
        query_test_helper(UnitsQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)

        preferences.units.set_conversion_mode('normal')
        preferences.commit()


test_spec_currency = [
    lambda Q, data: {
        'query': '= 10,000 mexican',
        'results': [
            get_unit_result(Q)(
                '10000 currency_MXN to currency_EUR',
                approxunits(
                    currency_amount(Q, data)(10000, 'MXN', 'EUR', True)
                ),
                currency_amount(Q, data)(10000, 'MXN', 'EUR', False),
                currency_description(Q, data)('MXN', 'EUR'),
                order=0,
                icon=images_dir('flags', 'EUR.svg'),
            ),
            get_unit_result(Q)(
                '10000 currency_MXN to currency_USD',
                approxunits(
                    currency_amount(Q, data)(10000, 'MXN', 'USD', True)
                ),
                currency_amount(Q, data)(10000, 'MXN', 'USD', False),
                currency_description(Q, data)('MXN', 'USD'),
                order=1,
                icon=images_dir('flags', 'USD.svg'),
            ),
            get_unit_result(Q)(
                '10000 currency_MXN to currency_BTC',
                approxunits(
                    currency_amount(Q, data)(10000, 'MXN', 'BTC', True)
                ),
                currency_amount(Q, data)(10000, 'MXN', 'BTC', False),
                currency_description(Q, data)('MXN', 'BTC'),
                order=2,
                icon=images_dir('flags', 'BTC.svg'),
            ),
            get_unit_result(Q)(
                '10000 currency_MXN to currency_CAD',
                approxunits(
                    currency_amount(Q, data)(10000, 'MXN', 'CAD', True)
                ),
                currency_amount(Q, data)(10000, 'MXN', 'CAD', False),
                currency_description(Q, data)('MXN', 'CAD'),
                order=3,
                icon=images_dir('flags', 'CAD.svg'),
            ),
            get_unit_result(Q)(
                '10000 currency_MXN to currency_MXN',
                approxunits(
                    currency_amount(Q, data)(10000, 'MXN', 'MXN', True)
                ),
                '10,000.00 MXN',
                '',
                order=4,
                icon=images_dir('flags', 'MXN.svg'),
            ),
        ],
    },
    lambda Q, data: {
        'query': '= 7.277 AMD to RON',
        'results': [
            get_unit_result(Q)(
                '7.277 currency_AMD to currency_RON',
                approxunits(
                    currency_amount(Q, data)(7.277, 'AMD', 'RON', True)
                ),
                currency_amount(Q, data)(7.277, 'AMD', 'RON', False),
                currency_description(Q, data)('AMD', 'RON'),
                order=0,
                icon=images_dir('flags', 'RON.svg'),
            ),
            get_unit_result(Q)(
                '7.277 currency_AMD to currency_AMD',
                approxunits(
                    currency_amount(Q, data)(7.277, 'AMD', 'AMD', True)
                ),
                '7.28 AMD',
                '',
                order=1,
                icon=images_dir('flags', 'AMD.svg'),
            ),
        ],
    },
    lambda Q, data: {
        # Test aliases from translator
        'query': '= 100.27 $ to BTC',
        'results': [
            get_unit_result(Q)(
                '100.27 currency_USD to currency_BTC',
                approxunits(
                    currency_amount(Q, data)(100.27, 'USD', 'BTC', True)
                ),
                currency_amount(Q, data)(100.27, 'USD', 'BTC', False),
                currency_description(Q, data)('USD', 'BTC'),
                order=0,
                icon=images_dir('flags', 'BTC.svg'),
            ),
            get_unit_result(Q)(
                '100.27 currency_USD to currency_USD',
                approxunits(
                    currency_amount(Q, data)(100.27, 'USD', 'USD', True)
                ),
                '100.27 USD',
                '',
                order=1,
                icon=images_dir('flags', 'USD.svg'),
            ),
        ],
    },
    lambda Q, data: {
        # Only one result (do not show duplicate 10 CAD)
        'query': '= 10 CAD to CAD',
        'results': [
            get_unit_result(Q)(
                '10 currency_CAD to currency_CAD',
                approxunits(currency_amount(Q, data)(10, 'CAD', 'CAD', True)),
                '10.00 CAD',
                '',
                order=0,
                icon=images_dir('flags', 'CAD.svg'),
            ),
        ],
    },
    lambda Q, data: {
        'query': '= 0.1 BTC to cad,EUR,USD,AED',
        'results': [
            get_unit_result(Q)(
                '0.1 currency_BTC to currency_CAD',
                approxunits(currency_amount(Q, data)(0.1, 'BTC', 'CAD', True)),
                currency_amount(Q, data)(0.1, 'BTC', 'CAD', False),
                currency_description(Q, data)('BTC', 'CAD'),
                order=0,
                icon=images_dir('flags', 'CAD.svg'),
            ),
            get_unit_result(Q)(
                '0.1 currency_BTC to currency_EUR',
                approxunits(currency_amount(Q, data)(0.1, 'BTC', 'EUR', True)),
                currency_amount(Q, data)(0.1, 'BTC', 'EUR', False),
                currency_description(Q, data)('BTC', 'EUR'),
                order=1,
                icon=images_dir('flags', 'EUR.svg'),
            ),
            get_unit_result(Q)(
                '0.1 currency_BTC to currency_USD',
                approxunits(currency_amount(Q, data)(0.1, 'BTC', 'USD', True)),
                currency_amount(Q, data)(0.1, 'BTC', 'USD', False),
                currency_description(Q, data)('BTC', 'USD'),
                order=2,
                icon=images_dir('flags', 'USD.svg'),
            ),
            get_unit_result(Q)(
                '0.1 currency_BTC to currency_AED',
                approxunits(currency_amount(Q, data)(0.1, 'BTC', 'AED', True)),
                currency_amount(Q, data)(0.1, 'BTC', 'AED', False),
                currency_description(Q, data)('BTC', 'AED'),
                order=3,
                icon=images_dir('flags', 'AED.svg'),
            ),
            get_unit_result(Q)(
                '0.1 currency_BTC to currency_BTC',
                approxunits(currency_amount(Q, data)(0.1, 'BTC', 'BTC', True)),
                '0.10 BTC',
                '',
                order=4,
                icon=images_dir('flags', 'BTC.svg'),
            ),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_currency)
def test_currency(mock_currency_service, test_spec):
    with mock_currency_service(default_currencies, error=False) as data:
        Q = UnitsService().unit_registry.Quantity
        test_spec = test_spec(Q, data)
        query_test_helper(UnitsQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_aliases_translations = [
    lambda Q: {
        'query': '= 1 &',
        'results': [
            get_unit_result(Q)(
                '1 meter to meter',
                approxunits(Q(1, 'meter')),
                '1 meter',
                '[length]',
            ),
        ],
    },
    lambda Q: {
        'query': '= 1 & to c&',
        'results': [
            get_unit_result(Q)(
                '1 meter to centimeter',
                approxunits(Q(100, 'centimeter')),
                '100 centimeter',
                '1 meter = 100 centimeter • [length]',
            ),
        ],
    },
    lambda Q: {
        'query': '= 1 m',
        'results': [
            get_unit_result(Q)(
                '1 meter to meter',
                approxunits(Q(1, 'meter')),
                '1 meter',
                '[length]',
            ),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_aliases_translations)
def test_aliases_translations(mock_currency_service, test_spec):
    translations = {'&': 'meter', 'm': 'meter'}
    with mock_currency_service(
        default_currencies, error=False
    ), extra_translations('units', translations):
        Q = UnitsService().unit_registry.Quantity
        test_spec = test_spec(Q)

        query_test_helper(UnitsQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_missing_pint = [
    {
        'query': '= 10 meters to decimeters',
        'results': [
            {
                'result': {
                    'query': '',
                    'value': None,
                    'error': MissingPintException,
                    'order': MissingPintException.order,
                },
                'query_result': {
                    'icon': images_dir('convert.svg'),
                    'name': tr_err('missing-pint-error'),
                    'description': tr_err('missing-pint-error-description'),
                    'clipboard': '/usr/bin/python3 -m pip install Pint',
                    'error': MissingPintException,
                    'order': MissingPintException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    }
]


@pytest.mark.parametrize('test_spec', test_spec_missing_pint)
def test_missing_pint(test_spec):
    with no_pint(units_service=True):
        query_test_helper(UnitsQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)

    with no_pint(units_service=False):
        query_test_helper(UnitsQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_provider_had_error = [
    {
        'query': '= 10 CAD',
        'results': [
            {
                'result': {
                    'query': '',
                    'value': None,
                    'error': CurrencyProviderException,
                    'order': CurrencyProviderException.order,
                },
                'query_result': {
                    'icon': images_dir('convert.svg'),
                    'name': tr_err('currency-provider-error'),
                    'description': tr_err(
                        'currency-provider-error-description'
                    ),
                    'clipboard': '',
                    'error': CurrencyProviderException,
                    'order': CurrencyProviderException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    }
]


@pytest.mark.parametrize('test_spec', test_spec_provider_had_error)
def test_provider_had_error(mock_currency_service, test_spec):
    with mock_currency_service(default_currencies, error=True):
        query_test_helper(UnitsQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_special_cases_spec = [
    lambda _: {'query': '= 10', 'results': []},
    lambda _: {'query': '= 10 cm / cm', 'results': []},
    lambda _: {
        # Only on NORMAL mode
        'query': '= 10 EUR / kilogram',
        'results': [],
    },
    lambda Q: {
        'query': '= 10 c ()',
        'results': [
            get_unit_result(Q)(
                '10 degree_Celsius to degree_Celsius',
                approxunits(Q(10.0, 'degree_Celsius')),
                '10 degree Celsius',
                '[temperature]',
            ),
        ],
    },
    lambda Q: {
        'query': '= 10 m',
        'results': [
            get_unit_result(Q)(
                '10 meter to meter',
                approxunits(Q(10.0, 'meter')),
                '10 meter',
                '[length]',
            ),
        ],
    },
    lambda _: {'query': '= 10 c(c', 'results': []},
    lambda _: {'query': '= 10 % c', 'results': []},
]


@pytest.mark.parametrize('test_spec', test_special_cases_spec)
def test_special_cases(mock_currency_service, test_spec):
    with mock_currency_service(default_currencies, error=False):
        Q = UnitsService().unit_registry.Quantity
        test_spec = test_spec(Q)
        query_test_helper(UnitsQueryHandler, test_spec)


test_units_service_not_running = [
    lambda _: {'query': '= 10 meter to centimeter', 'results': []}
]


@pytest.mark.parametrize('test_spec', test_units_service_not_running)
def test_unit_service_not_running(mock_currency_service, test_spec):
    with mock_currency_service(default_currencies, error=False):
        UnitsService().stop()
        test_spec = test_spec(None)
        query_test_helper(UnitsQueryHandler, test_spec)
