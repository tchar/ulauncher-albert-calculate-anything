from functools import lru_cache
import pytest
from pytz import timezone
from datetime import datetime, timedelta
from calculate_anything.time import TimezoneService
from calculate_anything.lang import LanguageService
from calculate_anything.query.handlers import TimeQueryHandler
from calculate_anything.constants import TIME_DATETIME_FORMAT, TIME_DATE_FORMAT, TIME_TIME_FORMAT
from tests.utils import query_test_helper_lazy, approxdt, approxstr


LanguageService().set('en_US')
tr_time = LanguageService().get_translator('time')
default_cities = TimezoneService().parse_default_cities(
    'Athens GR,New York City US')
TimezoneService().set_default_cities(default_cities)


@lru_cache(maxsize=None)
def get_result(description, query, order, td=timedelta()):
    return {
        'result': {
            # Use lambda for lazy evaluation
            'value': lambda: approxdt(datetime.now() + td),
            'query': query,
            'error': None,
            'order': order
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': lambda: approxstr((datetime.now() + td).strftime(TIME_DATETIME_FORMAT)),
            'description': lambda: description,
            'clipboard': lambda: approxstr((datetime.now() + td).strftime(TIME_DATETIME_FORMAT)),
            'error': None,
            'value': lambda: approxdt(datetime.now() + td),
            'value_type': datetime,
            'order': order
        }
    }


@lru_cache(maxsize=None)
def get_resulttz(city_name, country_name, iso2, query, order, tz, td=timedelta()):
    return {
        'result': {
            'value': lambda: approxdt(datetime.now(tz=timezone(tz)) + td),
            'query': query,
            'error': None,
            'order': order
        },
        'query_result': {
            'icon': 'images/flags/{}.svg'.format(iso2.upper()),
            'name': lambda: approxstr(
                '{}: {}'.format(
                    city_name,
                    (datetime.now(tz=timezone(tz)) + td).strftime(TIME_TIME_FORMAT))
            ),
            'description': lambda: approxstr(
                '{} • {} • {}'.format(
                    (datetime.now(tz=timezone(tz)) + td).strftime(
                        TIME_DATE_FORMAT),
                    country_name,
                    int((datetime.now(tz=timezone(tz)) +
                        td).utcoffset().total_seconds() / 60 / 60)
                )
            ),
            'clipboard': lambda: approxstr(
                '{}: {}'.format(
                    city_name,
                    (datetime.now(tz=timezone(tz)) + td).strftime(
                        TIME_TIME_FORMAT)
                )
            ),
            'error': None,
            'value': lambda: approxdt(datetime.now(tz=timezone(tz)) + td),
            'order': order,
            'value_type': datetime
        }
    }


test_spec_simple = [{
    # Normal test
    'query': 'time',
    'results': [
        get_result('Now', query='', order=0),
        get_resulttz('Athens', 'Greece', 'GR', query='',
                     order=1, tz='Europe/Athens'),
        get_resulttz('New York City', 'NY United States', 'US',
                     query='', order=2, tz='America/New_York')
    ]
}]


@ pytest.mark.parametrize('test_spec', test_spec_simple)
def test_simple(test_spec):
    query_test_helper_lazy(TimeQueryHandler, test_spec)


test_spec_target_city = [{
    # Normal test with target city
    'query': 'time at Vancouver',
    'results': [
        get_resulttz('Vancouver', 'Canada', 'CA', query='',
                     order=0, tz='America/Vancouver'),
        get_resulttz('Vancouver', 'WA United States', 'US',
                     query='', order=1, tz='America/Los_Angeles'),
        get_result('Now', query='', order=2)
    ]
}, {
    # Normal test with target city, country
    'query': 'time at Paris France',
    'results': [
        get_resulttz('Paris', 'France', 'FR', query='',
                     order=0, tz='Europe/Paris'),
        get_result('Now', query='', order=1)
    ]
}, {
    # Normal test with uknown city
    'query': 'time at SomeCityThatDoesNotExist',
    'results': [get_result('Now', query='', order=0)]
}]


@ pytest.mark.parametrize('test_spec', test_spec_target_city)
def test_target_city(test_spec):
    query_test_helper_lazy(TimeQueryHandler, test_spec)


test_spec_time = [{
    # Normal test with time calculation
    'query': 'time + 2 month 1 day 2 hours 30 minutes 2 seconds - 2 months 1 hour 2 minutes 1 second',
    'results': [
        get_result('Tomorrow', query='', order=0,
                   td=timedelta(days=1, seconds=5281)),
        get_resulttz('Athens', 'Greece', 'GR', query='',
                     order=1, tz='Europe/Athens',
                     td=timedelta(days=1, seconds=5281)),
        get_resulttz('New York City', 'NY United States', 'US',
                     query='', order=2, tz='America/New_York',
                     td=timedelta(days=1, seconds=5281))
    ]
}, {
    # Invalid query 1
    'query': 'time ++ 1 month',
    'results': []
}, {
    # Invalid query 2
    'query': 'time + 1 month - - 2 days +- 1 month',
    'results': []
}, {
    # Invalid query 3
    'query': 'time + 1 at Paris',
    'results': []
}]


@ pytest.mark.parametrize('test_spec', test_spec_time)
def test_time(test_spec):
    query_test_helper_lazy(TimeQueryHandler, test_spec)


test_spec_time_target_city = [{
    # Normal test with time calculation and target city
    'query': 'time - 1 week 1 day 2 hours 56 min at Paris',
    'results': [
        get_resulttz('Paris', 'France', 'FR', query='',
                     order=0, tz='Europe/Paris',
                     td=timedelta(days=-8, seconds=-10560)),
        get_resulttz('Paris', 'TX United States', 'US',
                     query='', order=1, tz='America/Chicago',
                     td=timedelta(days=-8, seconds=-10560)),
        get_result(tr_time('last-week').capitalize(),
                   query='', order=2, td=timedelta(days=-8, seconds=-10560)),
    ]
}, {
    'query': 'time + 1 month at Prague Czechia',
    'results': [
        get_resulttz('Prague', 'Czechia', 'CZ', query='',
                     order=0, tz='Europe/Prague',
                     td=timedelta(days=31)),
        get_result(tr_time('next-month').capitalize(),
                   query='', order=1, td=timedelta(days=31)),
    ]
}]


@ pytest.mark.parametrize('test_spec', test_spec_time_target_city)
def test_time_target_city(test_spec):
    query_test_helper_lazy(TimeQueryHandler, test_spec)
