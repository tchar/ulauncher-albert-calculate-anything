from calculate_anything.units.service import UnitsService
import pytest
import random
from datetime import datetime
from pytz import timezone
from itertools import zip_longest
from calculate_anything.lang import LanguageService
from calculate_anything.time import TimezoneService
from calculate_anything.query.multi_handler import MultiHandler
from test.tutils import (
    approxdt, currency_data, approxunits, set_time_reference, random_str
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
fixed_currency_data = {
    random_str(3).upper(): random.uniform(0.1, 1000.0)
    for _ in range(2)
}
fixed_currency_data = currency_data('EUR', **fixed_currency_data)['rates']
time_reference = datetime(2021, 7, 15, 14, 0, 0)


test_spec_multi_handler = [{
    'id': 'multi_handler:calculator',
    'test': lambda _: {
        'query': '= 10 + 100 * sqrt(2) + tan(pi) + cosh(sqrt(100 + e))',
        'expected_values': [pytest.approx(12756.51)]
    }
}, {
    'id': 'multi_handler:currency_no_target',
    'test': lambda Q: {
        'query': '= 1025 BTC',
        'expected_values': [
            get_currency_value(Q, 1025, 'BTC', 'EUR'),
            get_currency_value(Q, 1025, 'BTC', 'USD'),
            get_currency_value(Q, 1025, 'BTC', 'CAD'),
            get_currency_value(Q, 1025, 'BTC', 'BTC'),
        ]
    }
}, {
    'id': 'multi_handler:curency_target',
    'test': lambda Q: {
        'query': '= 1257 $ to CAD, BTC,MXN, EUR',
        'expected_values': [
            get_currency_value(Q, 1257, 'USD', 'CAD'),
            get_currency_value(Q, 1257, 'USD', 'BTC'),
            get_currency_value(Q, 1257, 'USD', 'MXN'),
            get_currency_value(Q, 1257, 'USD', 'EUR'),
            get_currency_value(Q, 1257, 'USD', 'USD'),
        ]
    }
}, {
    'id': 'multi_handler:units',
    'test': lambda Q: {
        'query': '= 20.25 km/h to in/minute, m/s, mile/h, cm/day',
        'expected_values': [
            approxunits(Q(13287.4, 'inch / minute')),
            approxunits(Q(5.625, 'meter / second')),
            approxunits(Q(12.58, 'mile / hour')),
            approxunits(Q(48600000, 'centimeter / day')),
        ]
    }
}, {
    'id': 'multi_handler:time_calculation',
    'test': lambda _: {
        'query': 'time + 2 hours 3 minutes at paris france',
        'expected_values': [
            approxdt(datetime(2021, 7, 15, 16, 3, 0)
                     .astimezone(timezone('Europe/Paris'))),
            approxdt(datetime(2021, 7, 15, 16, 3, 0)),
        ]
    }
}]
ids_multi_handler = [t['id'] for t in test_spec_multi_handler]


@pytest.mark.parametrize(
    'test_spec',
    test_spec_multi_handler,
    ids=ids_multi_handler)
def test_multihandler(benchmark, mock_currency_service, test_spec):
    with mock_currency_service(default_currencies, error=False,
                               **fixed_currency_data), \
            set_time_reference(time_reference):
        Q = UnitsService().unit_registry.Quantity
        test_spec = test_spec['test'](Q)
        query = test_spec['query']
        expected_values = test_spec['expected_values']

        results = benchmark(lambda q: MultiHandler().handle(q), query)
        result_vals = map(lambda r: r.value, results)

        for expected_value, val in zip_longest(expected_values, result_vals):
            assert expected_value == val
