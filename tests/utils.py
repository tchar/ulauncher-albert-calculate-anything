import pytest
import random
import string
from functools import lru_cache
from contextlib import contextmanager
from datetime import datetime, timedelta
from itertools import zip_longest
from simpleeval import SimpleEval
import parsedatetime
from calculate_anything.time import TimezoneService
from calculate_anything.units import UnitsService
from calculate_anything.currency import CurrencyService
import calculate_anything.query.handlers.units as units_handler
import calculate_anything.query.handlers.calculator as calculator_handler
import calculate_anything.query.handlers.base_n as base_n_handler
import calculate_anything.query.handlers.time as time_handler
from calculate_anything.utils import StupidEval
from calculate_anything.utils.singleton import Singleton


def random_str(length=None):
    length = length if length else 100
    return ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length)
    )


@contextmanager
def empty_ctx():
    yield


@contextmanager
def calculator_no_simpleeval():
    calculator_handler.SimpleEval = StupidEval
    yield
    calculator_handler.SimpleEval = SimpleEval


@contextmanager
def base_n_no_simpleeval():
    base_n_handler.SimpleEval = StupidEval
    get_simple_eval = base_n_handler.get_simple_eval
    base_n_handler.get_simple_eval = lambda: StupidEval()
    yield
    base_n_handler.get_simple_eval = get_simple_eval
    base_n_handler.SimpleEval = SimpleEval


@contextmanager
def no_parsedatetime():
    time_handler.parsedatetime = None
    yield
    time_handler.parsedatetime = parsedatetime


@contextmanager
def no_pint(units_service=True):
    pint = units_handler.pint
    units_handler.pint = None
    if units_service:
        yield
    else:
        UnitsService()._running = False
        yield
        UnitsService()._running = True
    units_handler.pint = pint


@contextmanager
def no_default_currencies():
    default_currencies = CurrencyService().default_currencies
    CurrencyService().set_default_currencies([])
    yield
    CurrencyService().set_default_currencies(default_currencies)


@contextmanager
def no_requests():
    missing_requests = CurrencyService()._missing_requests
    CurrencyService()._missing_requests = True
    with no_default_currencies():
        yield
    CurrencyService()._missing_requests = missing_requests


@contextmanager
def no_default_cities():
    default_cities = TimezoneService().default_cities
    TimezoneService().set_default_cities([])
    yield
    TimezoneService().set_default_cities(default_cities)


def set_time_reference(datetime):
    @contextmanager
    def _set_time_reference():
        now = time_handler.TimeQueryHandler.now
        time_handler.TimeQueryHandler.now = lambda: datetime
        yield
        time_handler.TimeQueryHandler.now = now
    return _set_time_reference


@contextmanager
def currency_provider_had_error():
    provider_had_error = CurrencyService()._provider.had_error
    CurrencyService()._provider.had_error = True
    with no_default_currencies():
        yield
    CurrencyService()._provider.had_error = provider_had_error


@contextmanager
def reset_instance(*classes, context=empty_ctx):
    old_instances = {}
    for cls in classes:
        if cls in Singleton._instances:
            instance = Singleton._instances[cls]
            old_instances[cls] = instance
            del Singleton._instances[cls]

    with context():
        tmp_classes = tuple(cls() for cls in classes)
        yield tmp_classes

    for cls in classes:
        del Singleton._instances[cls]
        if cls in old_instances:
            Singleton._instances[cls] = old_instances[cls]
        else:
            cls()


class Approx:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)


class ApproxDt(Approx):
    def __init__(self, data, tol):
        super().__init__(data)
        self.tol = tol

    def __eq__(self, other):
        if isinstance(self.data, datetime):
            if self.data.tzinfo != other.tzinfo:
                return False
        small, big = sorted([self.data, other])
        return big - small <= self.tol


def approxdt(dt, tol=timedelta(seconds=5)):
    return ApproxDt(dt, tol)


class ApproxStr(Approx):
    def __init__(self, data, reject_chars):
        super().__init__(data)
        self.reject_chars = reject_chars

    def __eq__(self, other):
        res = zip_longest(self.data, other, fillvalue=None)
        res = map(lambda r: r[0] != r[1], res)
        return sum(res) < self.reject_chars


def approxstr(s, reject_chars=3):
    return ApproxStr(s, reject_chars)


class ApproxUnits(Approx):
    def __init__(self, data, tol):
        super().__init__(data)
        self.tol = tol

    def __eq__(self, other):
        return self.data.units == other.units and \
            pytest.approx(self.data.magnitude, self.tol) == other.magnitude


def approxunits(unit, tol=0.01):
    return ApproxUnits(unit, tol)


def query_test_helper(cls, test_spec):
    results = cls().handle(test_spec['query'])
    if results is None:
        assert len(test_spec['results']) == 0
        return

    assert len(test_spec['results']) == len(results)

    results = sorted(results, key=lambda result: result.order)
    assert len(test_spec['results']) == len(results)

    for result, item in zip(results, test_spec['results']):
        assert item['result']['value'] == result.value
        assert item['result']['query'] == result.query
        assert (
            item['result']['error'] == result.error or
            isinstance(result.error, item['result']['error'])
        )
        assert item['result']['order'] == result.order

        query_result = result.to_query_result()
        assert item['query_result']['icon'] == query_result.icon
        assert item['query_result']['name'] == query_result.name
        assert item['query_result']['description'] == query_result.description
        assert item['query_result']['clipboard'] == query_result.clipboard
        assert (
            item['query_result']['error'] == query_result.error or
            isinstance(query_result.error, item['query_result']['error'])
        )
        assert item['query_result']['order'] == query_result.order
        assert item['query_result']['value'] == query_result.value
        # Although seems stupid we use this to distinguish between equalities
        # in floats and ints. For example 3.0 is not equal to 3 we want the
        # type to be correct
        assert isinstance(query_result.value,
                          item['query_result']['value_type'])


@lru_cache(maxsize=None)
def currency_data(base_currency='EUR'):
    rates = {
        'EUR': 1,
        'USD': 0.9,
        # 'BTC': 100000

    }
    return {
        'base_currency': base_currency,
        'rates': {
            k: v / rates[base_currency]
            for k, v in rates.items()
        }
    }


def expected_currencies(timestamp=None, filterc=set()):
    timestamp = timestamp or datetime.now().timestamp()
    return {
        k: {
            'rate': pytest.approx(v),
            'timestamp_refresh': pytest.approx(timestamp)
        }
        for k, v in currency_data('EUR')['rates'].items()
        if k not in filterc
    }
