from functools import lru_cache
from datetime import datetime, timedelta
import pytest
from pytz import timezone
from calculate_anything.time import TimezoneService
from calculate_anything.lang import LanguageService
import calculate_anything.query.handlers.time as time_handler
from calculate_anything.query.handlers import TimeQueryHandler
from calculate_anything.constants import TIME_DATETIME_FORMAT, TIME_DATE_FORMAT, TIME_TIME_FORMAT
from calculate_anything.exceptions import DateOverflowException, MisparsedTimeException, MissingParsedatetimeException
from tests.utils import no_parsedatetime, reset_instance, approxdt, approxstr, query_test_helper_lazy, query_test_helper, no_parsedatetime


LanguageService().set('en_US')
tr_time = LanguageService().get_translator('time')
tr_err = LanguageService().get_translator('errors')
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


def timedelta_to_ydhms(dt: datetime, ref: datetime):
    if dt < ref:
        sg = '- '
        dt, ref = ref, dt
    else:
        sg = ''

    print('dt', dt, 'ref', ref)
    y = dt.year - ref.year
    td = dt - ref
    d = td.days
    h, remainder = divmod(td.seconds, 3600)
    m, s = divmod(remainder, 60)
    ydhms = [
        (y, 'years' if y != 1 else 'year'),
        (d, 'days' if d != 1 else 'day'),
        (h, 'hours' if h != 1 else 'hour'),
        (m, 'minutes' if m != 1 else 'minute'),
        (s, 'seconds' if s != 1 else 'second'),
    ]
    ydhms = filter(lambda t: t[0] != 0, ydhms)
    ydhms = map(lambda t: '{} {}'.format(*t), ydhms)
    ydhms = list(ydhms)[:3]
    return sg + ', '.join(ydhms)


def get_resulttd(target: datetime, query: str, order: int):
    return {
        'result': {
            # Use lambda for lazy evaluation
            'value': lambda: approxdt(target - datetime.now()),
            'query': query,
            'error': None,
            'order': order
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': lambda: timedelta_to_ydhms(target, datetime.now()),
            'description': lambda: '"{}" is on {}'.format(query.capitalize(), target.strftime(TIME_DATETIME_FORMAT)),
            'clipboard': lambda: timedelta_to_ydhms(target, datetime.now()),
            'error': None,
            'value': lambda: approxdt(target - datetime.now()),
            'value_type': timedelta,
            'order': order
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
        get_resulttz('Vancouver', 'Canada', 'CA', query='at Vancouver',
                     order=0, tz='America/Vancouver'),
        get_resulttz('Vancouver', 'WA United States', 'US',
                     query='at Vancouver', order=1, tz='America/Los_Angeles'),
        get_result('Now', query='', order=2)
    ]
}, {
    # Normal test with target city, country
    'query': 'time at Paris France',
    'results': [
        get_resulttz('Paris', 'France', 'FR', query='at Paris France',
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
    'query': 'time + 2 MONTH 1 day 2 HoUrS 30 minutes 2 seconds - 2 months 1 hour 2 minutes 1 SeCond',
    'results': [
        get_result('Tomorrow',
                   query='+ 2 MONTH 1 day 2 HoUrS 30 minutes 2 seconds - 2 months 1 hour 2 minutes 1 SeCond',
                   order=0, td=timedelta(days=1, seconds=5281)),
        get_resulttz('Athens', 'Greece', 'GR',
                     query='+ 2 MONTH 1 day 2 HoUrS 30 minutes 2 seconds - 2 months 1 hour 2 minutes 1 SeCond',
                     order=1, tz='Europe/Athens',
                     td=timedelta(days=1, seconds=5281)),
        get_resulttz('New York City', 'NY United States', 'US',
                     query='+ 2 MONTH 1 day 2 HoUrS 30 minutes 2 seconds - 2 months 1 hour 2 minutes 1 SeCond',
                     order=2, tz='America/New_York',
                     td=timedelta(days=1, seconds=5281))
    ]
}, {
    # Test partial matching
    'query': 'time + 1 hour 2 some text',
    'results': [{
        'result': {
            'value': None,
            'query': '+ 1 hour',
            'error': MisparsedTimeException,
            'order': 0
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': '{}: "time + 1 hour"'.format(tr_err('unfully-parsed-date')),
            'description': '{}: "time + 1 hour 2 some text"'.format(tr_err('unfully-parsed-date-description')),
            'clipboard': '',
            'error': None,
            'value': None,
            'value_type': type(None),
            'order': 0
        }
    },
        get_result('Today', query='+ 1 hour', order=1,
                   td=timedelta(seconds=3600)),
        get_resulttz('Athens', 'Greece', 'GR', query='+ 1 hour', order=2,
                     tz='Europe/Athens', td=timedelta(seconds=3600)),
        get_resulttz('New York City', 'NY United States', 'US',
                     query='+ 1 hour', order=3, tz='America/New_York',
                     td=timedelta(seconds=3600))
    ]
}, {
    # Test overflows
    'query': 'time + 20000000 YeaRs',
    'results': [{
        'result': {
            'value': None,
            'query': '+ 20000000 YeaRs',
            'error': DateOverflowException,
            'order': 0
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': tr_err('date-overflow'),
            'description': tr_err('date-overflow-description'),
            'clipboard': '',
            'error': None,
            'value': None,
            'value_type': type(None),
            'order': 0
        }
    }]
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
}, {
    # Invalid query 4
    'query': 'time + Some random string',
    'results': []
}]


@ pytest.mark.parametrize('test_spec', test_spec_time)
def test_time(test_spec):
    query_test_helper_lazy(TimeQueryHandler, test_spec)


test_spec_time_target_city = [{
    # Normal test with time calculation and target city
    'query': 'time - 1 WeEk 1 DaY 2 HouR 56 min At ParIs',
    'results': [
        get_resulttz('Paris', 'France', 'FR',
                     query='- 1 WeEk 1 DaY 2 HouR 56 min At ParIs',
                     order=0, tz='Europe/Paris',
                     td=timedelta(days=-8, seconds=-10560)),
        get_resulttz('Paris', 'TX United States', 'US',
                     query='- 1 WeEk 1 DaY 2 HouR 56 min At ParIs',
                     order=1, tz='America/Chicago',
                     td=timedelta(days=-8, seconds=-10560)),
        get_result(tr_time('last-week').capitalize(),
                   query='- 1 WeEk 1 DaY 2 HouR 56 min',
                   order=2, td=timedelta(days=-8, seconds=-10560)),
    ]
}, {
    'query': 'time + 1 month at Prague CzEcHia',
    'results': [
        get_resulttz('Prague', 'Czechia', 'CZ', query='+ 1 month at Prague CzEcHia',
                     order=0, tz='Europe/Prague',
                     td=timedelta(days=31)),
        get_result(tr_time('next-month').capitalize(),
                   query='+ 1 month', order=1, td=timedelta(days=31)),
    ]
}]


@ pytest.mark.parametrize('test_spec', test_spec_time_target_city)
def test_time_target_city(test_spec):
    query_test_helper_lazy(TimeQueryHandler, test_spec)


tomorrow_morning = (datetime.now() + timedelta(days=1)
                    ).replace(hour=9, minute=0, second=0, microsecond=0)

# Add 2 days because midnight is same day at 00:00:00
tomorrow_midnight = (datetime.now() + timedelta(days=2)
                     ).replace(hour=0, minute=0, second=0, microsecond=0)

test_spec_until = [{
    # Normal test
    'query': 'time uNTill tomorrow',
    'results': [
        get_resulttd(tomorrow_morning, query='uNTill tomorrow', order=0),
        get_result('Now', query='uNTill tomorrow', order=1),
    ]
}, {
    # Cannot parse until
    'query': 'time till SomeRandomString',
    'results': [{
        'result': {
            'value': None,
            'query': 'till',
            'error': MisparsedTimeException,
            'order': 0
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': '{}: "time till"'.format(tr_err('unfully-parsed-date')),
            'description': '{}: "time till SomeRandomString"'.format(tr_err('unfully-parsed-date-description')),
            'clipboard': '',
            'error': None,
            'value': None,
            'value_type': type(None),
            'order': 0
        }
    },
        get_result('Now', query='till', order=1)
    ]}, {
    # Partial parse until
    'query': 'time tIl tomorrow midnight m',
    'results': [{
        'result': {
            'value': None,
            'query': 'tIl tomorrow midnight',
            'error': MisparsedTimeException,
            'order': 0
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': '{}: "time tIl tomorrow midnight"'.format(tr_err('unfully-parsed-date')),
            'description': '{}: "time tIl tomorrow midnight m"'.format(tr_err('unfully-parsed-date-description')),
            'clipboard': '',
            'error': None,
            'value': None,
            'value_type': type(None),
            'order': 0
        }
    },
        get_resulttd(tomorrow_midnight,
                     query='tIl tomorrow midnight', order=1),
        get_result('Now', query='tIl tomorrow midnight', order=2)
    ]}, {
    # Do not match digits only
    'query': 'time until 1245',
    'results': [{
        'result': {
            'value': None,
            'query': 'until',
            'error': MisparsedTimeException,
            'order': 0
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': '{}: "time until"'.format(tr_err('unfully-parsed-date')),
            'description': '{}: "time until 1245"'.format(tr_err('unfully-parsed-date-description')),
            'clipboard': '',
            'error': None,
            'value': None,
            'value_type': type(None),
            'order': 0
        }
    }, get_result('Now', query='until', order=1),
    ]
}, {
    # Test overflows
    'query': 'time until 20000 yEaR',
    'results': [{
        'result': {
            'value': None,
            'query': 'until 20000 yEaR',
            'error': DateOverflowException,
            'order': 0
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': tr_err('date-overflow'),
            'description': tr_err('date-overflow-description'),
            'clipboard': '',
            'error': None,
            'value': None,
            'value_type': type(None),
            'order': 0
        }
    }]
}]


@ pytest.mark.parametrize('test_spec', test_spec_until)
def test_until(test_spec):
    query_test_helper_lazy(TimeQueryHandler, test_spec)


test_spec_parsedatetime_missing = [{
    # Normal test with time calculation and target city
    'query': 'time',
    'results': [{
        'result': {
            'value': None,
            'query': '',
            'error': MissingParsedatetimeException,
            'order': -1
        },
        'query_result': {
            'icon': 'images/time.svg',
            'name': tr_err('install-parsedatetime'),
            'description': tr_err('install-parsedatetime-description'),
            'clipboard': 'pip install parsedatetime',
            'error': MissingParsedatetimeException,
            'value': None,
            'value_type': type(None),
            'order': -1
        }
    }]
}]


@pytest.mark.parametrize('test_spec', test_spec_parsedatetime_missing)
def test_parsedatetime_missing(test_spec):
    # Set parsedatetime to None
    with reset_instance(TimeQueryHandler, context=no_parsedatetime):
        query_test_helper(TimeQueryHandler, test_spec)
