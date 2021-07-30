import os
import pytest
import random
import string
import time
from functools import lru_cache
from contextlib import contextmanager
from datetime import datetime, timedelta
from itertools import zip_longest
import tempfile
from simpleeval import SimpleEval
import parsedatetime
from calculate_anything.time import TimezoneService
from calculate_anything.lang import LanguageService
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


@lru_cache(maxsize=None)
def mem_path():
    mem_path_ = '/dev/shm'
    fallback = tempfile.gettempdir()
    if not os.path.exists(mem_path_):
        return fallback
    rand_name = random_str(20)
    rand_path = os.path.join(mem_path_, rand_name)
    try:
        with open(rand_path, 'w', encoding='utf-8') as f:
            f.write('\n')
    except Exception:
        return fallback
    try:
        os.remove(rand_path)
        return mem_path_
    except Exception:
        return fallback


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
def extra_translations(mode, translations):
    old_data = LanguageService()._data.copy()
    if mode not in LanguageService()._data:
        LanguageService()._data[mode] = {}
    for k, v in translations.items():
        LanguageService()._data[mode][k] = v
    yield
    LanguageService()._data = old_data


def osremove(path):
    try:
        if path is None:
            return
        if not os.path.exists(path):
            return
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)
    # Fucking windows
    except Exception:
        pass


def temp_filepath(*filenames):
    mem_path_ = mem_path()
    filepaths = []
    for filename in filenames:
        filepath = os.path.join(mem_path_, filename)
        osremove(filepath)
        filepaths.append(filepath)

    if len(filepaths) == 1:
        return filepaths[0]
    if len(filepaths) > 1:
        return filepaths


@contextmanager
def temp_file(*filenames, sleep=0):
    filepaths = []
    filenames = filter(None, filenames)
    try:
        for filename, data in filenames:
            filepath = temp_filepath(filename)
            if isinstance(data, str):
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(data)
                    time.sleep(sleep)
            else:
                os.mkdir(filepath)
                time.sleep(sleep)
            filepaths.append(filepath)
        if len(filepaths) == 1:
            yield filepaths[0]
        elif len(filepaths) > 1:
            yield filepaths
        else:
            yield
    finally:
        for filepath in filepaths:
            osremove(filepath)


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


def test_query_result(item, query_result):
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


def query_test_helper(cls, test_spec, raw=False, only_qr=False):
    if raw:
        results = cls().handle_raw(test_spec['query'])
    else:
        results = cls().handle(test_spec['query'])
    if results is None:
        assert len(test_spec['results']) == 0
        return

    assert len(test_spec['results']) == len(results)

    results = sorted(results, key=lambda result: result.order)
    assert len(test_spec['results']) == len(results)

    for result, item in zip(results, test_spec['results']):
        if only_qr:
            query_result = result
            test_query_result(item, query_result)
            return

        assert item['result']['value'] == result.value
        assert item['result']['query'] == result.query
        assert (
            item['result']['error'] is None or
            isinstance(result.error, item['result']['error'])
        )
        assert item['result']['order'] == result.order

        query_result = result.to_query_result()
        test_query_result(item, query_result)


@lru_cache(maxsize=None)
def currency_data(base_currency='EUR'):
    rates = {
        'EUR': 1,
        'USD': 0.9,
        'MXN': 0.2,
        'CAD': 0.7,
        'AMD': 0.4,
        'RON': 0.5,
        'AED': 10,
        'BTC': 100000,
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
