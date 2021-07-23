from types import LambdaType
from contextlib import contextmanager
from datetime import datetime, timedelta
from itertools import zip_longest
from simpleeval import SimpleEval
import parsedatetime
from calculate_anything.time.service import TimezoneService
import calculate_anything.query.handlers.calculator as calculator_handler
import calculate_anything.query.handlers.time as time_handler
from calculate_anything.utils import Singleton, StupidEval


@contextmanager
def empty_ctx():
    yield


@contextmanager
def no_simpleeval():
    calculator_handler.SimpleEval = StupidEval
    yield
    calculator_handler.SimpleEval = SimpleEval


@contextmanager
def no_parsedatetime():
    time_handler.parsedatetime = None
    yield
    time_handler.parsedatetime = parsedatetime


@contextmanager
def no_default_cities():
    default_cities = TimezoneService()._default_cities
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
def reset_instance(cls, context=empty_ctx):
    if cls in Singleton._instances:
        del Singleton._instances[cls]

    with context():
        yield cls()

    del Singleton._instances[cls]
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


def query_test_helper(cls, test_spec):
    results = cls().handle(test_spec['query'])
    if results is None:
        assert len(test_spec['results']) == 0
        return

    assert len(results) == len(test_spec['results'])

    results = sorted(results, key=lambda result: result.order)
    assert len(results) == len(test_spec['results'])

    for result, item in zip(results, test_spec['results']):
        assert result.value == item['result']['value']
        assert result.query == item['result']['query']
        assert (
            result.error == item['result']['error'] or
            isinstance(result.error, item['result']['error'])
        )
        assert result.order == item['result']['order']

        query_result = result.to_query_result()
        assert query_result.icon == item['query_result']['icon']
        assert query_result.name == item['query_result']['name']
        assert query_result.description == item['query_result']['description']
        assert query_result.clipboard == item['query_result']['clipboard']
        assert (
            query_result.error == item['query_result']['error'] or
            isinstance(query_result.error, item['query_result']['error'])
        )
        assert query_result.order == item['query_result']['order']
        assert query_result.value == item['query_result']['value']
        # Although seems stupid we use this to distinguish between equalities in floats and ints
        # For example 3.0 is not equal to 3 we want the type to be correct
        assert isinstance(query_result.value,
                          item['query_result']['value_type'])

