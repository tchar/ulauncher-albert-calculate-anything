from calculate_anything.query.handlers.units import UnitsQueryHandler
from calculate_anything.units.service import UnitsService
import pytest
from datetime import datetime, timedelta
from pytz import timezone
from itertools import zip_longest
from calculate_anything.lang import LanguageService
from calculate_anything.time import TimezoneService
from calculate_anything.query.handlers import (
    CalculatorQueryHandler,
    PercentagesQueryHandler,
    TimeQueryHandler,
    Base10QueryHandler,
    Base16QueryHandler,
    Base2QueryHandler,
    Base8QueryHandler,
)
from calculate_anything.query.handlers import MultiHandler
from test.tutils import (
    approxdt,
    currency_data,
    approxunits,
    set_time_reference,
    random_str,
)


def get_currency_value(Q, amount, origin, target):
    data = fixed_currency_data
    unit = 'currency_{}'.format(target)
    amount = amount * data[target] / data[origin]
    return approxunits(Q(amount, unit))


LanguageService().set('en_US')
TimezoneService().start()
default_currencies = ['EUR', 'USD', 'BTC', 'CAD']
# Some extra currencies for benchmarking
fixed_currency_data = {random_str(3).upper(): float(i + 1) for i in range(200)}
fixed_currency_data = currency_data('EUR', **fixed_currency_data)['rates']
time_reference = datetime(2021, 7, 15, 14, 0, 0)


test_spec_handlers = [
    {
        'id': 'calculator',
        'test': lambda _: {
            'query': '= 10 + 100 * sqrt(2) + tan(pi) + cosh(sqrt(100 + e))',
            'expected_values': [pytest.approx(12756.51)],
            'handler': CalculatorQueryHandler,
        },
    },
    {
        'id': 'percentage',
        'test': lambda _: {
            'query': '= 10 + 100 * sqrt(2) + tan(pi) + cosh(sqrt(100 + e))%',
            'expected_values': [pytest.approx(19238.21)],
            'handler': PercentagesQueryHandler,
        },
    },
    {
        'id': 'dec',
        'test': lambda _: {
            'query': 'dec 11231 + 12 + 12912 mod 14 + 12 or 1 - 24 xor 2 * 24',
            'expected_values': [-5, -5, -5, -5],
            'handler': Base10QueryHandler,
        },
    },
    {
        'id': 'hex',
        'test': lambda _: {
            'query': 'hex ffab + ff2 + ab124 mod 25 + '
            '25 or ffaf - 22ff xor ae * 12',
            'expected_values': [
                122828,
                122828,
                122828,
                122828,
                '20:66:66:61:62:20:2b:20:66:66:32:20:2b:20:61:'
                '62:31:32:34:20:6d:6f:64:20:32:35:20:2b:20:32:'
                '35:20:6f:72:20:66:66:61:66:20:2d:20:32:32:66:'
                '66:20:78:6f:72:20:61:65:20:2a:20:31:32',
            ],
            'handler': Base16QueryHandler,
        },
    },
    {
        'id': 'bin',
        'test': lambda _: {
            'query': 'bin 10101 + 1001 - 110010 mod 1000 + '
            '10101 or 10110 - 11010 xor 1001 * 111001',
            'expected_values': [-515, -515, -515, -515],
            'handler': Base2QueryHandler,
        },
    },
    {
        'id': 'oct',
        'test': lambda _: {
            'query': 'oct 11231 + 12 + 1212 mod 14 + 12 or 1 - 24 xor 2 * 24',
            'expected_values': [-17, -17, -17, -17],
            'handler': Base8QueryHandler,
        },
    },
    {
        'id': 'color',
        'test': lambda _: {
            'query': 'hex #ff0000',
            'expected_values': [
                pytest.approx((255, 0, 0)),
                pytest.approx((0, 1.0, 1.0)),
                pytest.approx((0, 1.0, 0.5)),
                pytest.approx((0, 1.0, 1.0, 0.0)),
                '20:23:66:66:30:30:30:30',
            ],
            'handler': Base16QueryHandler,
        },
    },
    {
        'id': 'currency_no_target',
        'test': lambda Q: {
            'query': '= 1025 BTC',
            'expected_values': [
                get_currency_value(Q, 1025, 'BTC', 'EUR'),
                get_currency_value(Q, 1025, 'BTC', 'USD'),
                get_currency_value(Q, 1025, 'BTC', 'CAD'),
                get_currency_value(Q, 1025, 'BTC', 'BTC'),
            ],
            'handler': UnitsQueryHandler,
        },
    },
    {
        'id': 'curency_target',
        'test': lambda Q: {
            'query': '= 1257 $ to CAD, BTC,MXN, EUR',
            'expected_values': [
                get_currency_value(Q, 1257, 'USD', 'CAD'),
                get_currency_value(Q, 1257, 'USD', 'BTC'),
                get_currency_value(Q, 1257, 'USD', 'MXN'),
                get_currency_value(Q, 1257, 'USD', 'EUR'),
                get_currency_value(Q, 1257, 'USD', 'USD'),
            ],
            'handler': UnitsQueryHandler,
        },
    },
    {
        'id': 'units',
        'test': lambda Q: {
            'query': '= 20.25 km/h to in/minute, m/s, mile/h, cm/day',
            'expected_values': [
                approxunits(Q(13287.4, 'inch / minute')),
                approxunits(Q(5.625, 'meter / second')),
                approxunits(Q(12.58, 'mile / hour')),
                approxunits(Q(48600000, 'centimeter / day')),
            ],
            'handler': UnitsQueryHandler,
        },
    },
    {
        'id': 'time_calculation',
        'test': lambda _: {
            'query': 'time + 2 hours 3 minutes at paris france',
            'expected_values': [
                approxdt(
                    datetime(2021, 7, 15, 16, 3, 0).astimezone(
                        timezone('Europe/Paris')
                    )
                ),
                approxdt(datetime(2021, 7, 15, 16, 3, 0)),
            ],
            'handler': TimeQueryHandler,
        },
    },
    {
        'id': 'time_until',
        'test': lambda _: {
            'query': 'time until December 31 2021 midnight',
            'expected_values': [
                approxdt(timedelta(days=169, seconds=36000)),
                approxdt(datetime(2021, 7, 15, 14, 0, 0)),
            ],
            'handler': TimeQueryHandler,
        },
    },
]
ids_handlers = [t['id'] for t in test_spec_handlers]


@pytest.mark.parametrize('test_spec', test_spec_handlers, ids=ids_handlers)
def test_single_handler(benchmark, mock_currency_service, test_spec):
    with mock_currency_service(
        default_currencies, error=False, **fixed_currency_data
    ), set_time_reference(time_reference):
        Q = UnitsService().unit_registry.Quantity
        test_spec = test_spec['test'](Q)
        query = test_spec['query']
        expected_values = test_spec['expected_values']

        handler = test_spec['handler']()
        results = benchmark(handler.handle, query)
        results = sorted(results, key=lambda result: result.order)
        result_vals = map(lambda r: r.value, results)

        for expected_value, val in zip_longest(expected_values, result_vals):
            assert expected_value == val


@pytest.mark.parametrize('test_spec', test_spec_handlers, ids=ids_handlers)
def test_multihandler(benchmark, mock_currency_service, test_spec):
    with mock_currency_service(
        default_currencies, error=False, **fixed_currency_data
    ), set_time_reference(time_reference):
        Q = UnitsService().unit_registry.Quantity
        test_spec = test_spec['test'](Q)
        query = test_spec['query']
        expected_values = test_spec['expected_values']

        multi_handler = MultiHandler()
        results = benchmark(multi_handler.handle, query)
        results = sorted(results, key=lambda result: result.order)
        result_vals = map(lambda r: r.value, results)

        for expected_value, val in zip_longest(expected_values, result_vals):
            assert expected_value == val
