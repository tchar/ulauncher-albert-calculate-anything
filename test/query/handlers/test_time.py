from functools import lru_cache
from datetime import datetime, timedelta
import pytest
from pytz import timezone
from calculate_anything.time import TimezoneService
from calculate_anything.lang import LanguageService
from calculate_anything.query.handlers import MultiHandler
from calculate_anything.query.handlers import TimeQueryHandler
from calculate_anything.constants import (
    TIME_DATETIME_FORMAT,
    TIME_DATE_FORMAT,
    TIME_TIME_FORMAT,
)
from calculate_anything.utils import images_dir
from calculate_anything.utils.datetime import is_leap_year
from calculate_anything.exceptions import (
    DateOverflowException,
    MisparsedDateTimeException,
    MissingParsedatetimeException,
)
from test.tutils import (
    no_default_cities,
    no_parsedatetime,
    reset_instance,
    approxdt,
    approxstr,
    query_test_helper,
    set_time_reference,
)


LanguageService().set('en_US')
tr_time = LanguageService().get_translator('time')
tr_err = LanguageService().get_translator('errors')
TimezoneService().start()
TimezoneService().parse_default_cities_str(
    'Athens GR,New York City US', save=True
)
time_reference = datetime(2021, 7, 15, 14, 0, 0)


def dt(dt=None, tz=None):
    """Set a datetime reference for testing"""

    if dt is None:
        dt = time_reference
    if tz:
        ret = dt.astimezone(timezone(tz))
    else:
        ret = dt
    return ret


def timedelta_to_ydhms(dt: datetime, ref: datetime):
    if dt < ref:
        sg = '- '
        dt, ref = ref, dt
    else:
        sg = ''

    y = dt.year - ref.year
    old_dt = dt
    # Check if target date is february 29 before replacing years
    # If not reference is leap year move to March 1st
    if dt.month == 2 and dt.day == 29 and not is_leap_year(ref.year):
        dt = dt.replace(year=ref.year, month=3, day=1)
    else:
        dt = dt.replace(year=ref.year)
    if dt < ref:
        dt = old_dt
        y = 0
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


@lru_cache(maxsize=None)
def get_result(description, query, order, value=dt()):
    return {
        'result': {
            'value': approxdt(value),
            'query': query,
            'error': None,
            'order': order,
        },
        'query_result': {
            'icon': images_dir('time.svg'),
            'name': approxstr(value.strftime(TIME_DATETIME_FORMAT)),
            'description': approxstr(description),
            'clipboard': approxstr(value.strftime(TIME_DATETIME_FORMAT)),
            'error': None,
            'value': approxdt(value),
            'value_type': datetime,
            'order': order,
        },
    }


@lru_cache(maxsize=None)
def get_resulttz(city_name, country_name, iso2, query, order, value):
    icon = images_dir('flags', '{}.svg'.format(iso2.upper()))
    return {
        'result': {
            'value': approxdt(value),
            'query': query,
            'error': None,
            'order': order,
        },
        'query_result': {
            'icon': icon,
            'name': approxstr(
                '{}: {}'.format(city_name, value.strftime(TIME_TIME_FORMAT))
            ),
            'description': approxstr(
                '{} • {} • {} ({})'.format(
                    value.strftime(TIME_DATE_FORMAT),
                    country_name,
                    value.tzname(),
                    'UTC{:+.0f}'.format(
                        value.utcoffset().total_seconds() / 60 / 60
                    ),
                )
            ),
            'clipboard': approxstr(
                '{}: {}'.format(city_name, value.strftime(TIME_TIME_FORMAT))
            ),
            'error': None,
            'value': approxdt(value),
            'order': order,
            'value_type': datetime,
        },
    }


@lru_cache(maxsize=None)
def get_resulttd(value: timedelta, query: str, order: int):
    return {
        'result': {
            'value': approxdt(value),
            'query': query,
            'error': None,
            'order': order,
        },
        'query_result': {
            'icon': images_dir('time.svg'),
            'name': approxstr(timedelta_to_ydhms(value + dt(), dt())),
            'description': approxstr(
                '"{}" {} on {}'.format(
                    query.capitalize(),
                    'is' if value + dt() >= dt() else 'was',
                    (value + dt()).strftime(TIME_DATETIME_FORMAT),
                )
            ),
            'clipboard': approxstr(timedelta_to_ydhms(value + dt(), dt())),
            'error': None,
            'value': approxdt(value),
            'value_type': timedelta,
            'order': order,
        },
    }


def get_resultexc(query, exception, name_post='', desc_post=''):
    if exception == DateOverflowException:
        order = DateOverflowException.order
        name_key = 'date-overflow'
        desc_key = 'date-overflow-description'
    elif exception == MisparsedDateTimeException:
        order = MisparsedDateTimeException.order
        name_key = 'misparsed-datetime'
        desc_key = 'misparsed-datetime-description'

    return {
        'result': {
            'value': None,
            'query': query,
            'error': exception,
            'order': order,
        },
        'query_result': {
            'icon': images_dir('time.svg'),
            'name': tr_err(name_key) + name_post,
            'description': tr_err(desc_key) + desc_post,
            'clipboard': '',
            'error': exception,
            'value': None,
            'value_type': type(None),
            'order': order,
        },
    }


test_spec_simple = [
    {
        # Normal test 1
        'query': 'time',
        'results': [
            get_result('Now', query='', order=0),
            get_resulttz(
                'Athens',
                'Greece',
                'GR',
                query='',
                order=1,
                value=dt(tz='Europe/Athens'),
            ),
            get_resulttz(
                'New York City',
                'NY United States',
                'US',
                query='',
                order=2,
                value=dt(tz='America/New_York'),
            ),
        ],
    },
    {
        # Normal test 2
        'query': 'time + 1 day before',
        'results': [
            get_result(
                'Yesterday',
                query='+ 1 day before',
                order=0,
                value=dt(datetime(2021, 7, 14, 14, 0, 0)),
            ),
            get_resulttz(
                'Athens',
                'Greece',
                'GR',
                query='+ 1 day before',
                order=1,
                value=dt(
                    datetime(2021, 7, 14, 14, 0, 0),
                    tz='Europe/Athens',
                ),
            ),
            get_resulttz(
                'New York City',
                'NY United States',
                'US',
                query='+ 1 day before',
                order=2,
                value=dt(
                    datetime(2021, 7, 14, 14, 0, 0), tz='America/New_York'
                ),
            ),
        ],
    },
    {
        # Overflow with one chunk
        'query': 'time + 8000000 years',
        'results': [get_resultexc('+ 8000000 years', DateOverflowException)],
    },
    {
        # Overflow with multiple chunks
        'query': 'time + 4000 years + 4000 years',
        'results': [
            get_resultexc('+ 4000 years + 4000 years', DateOverflowException)
        ],
    },
    {
        # Not parsed
        'query': 'time + 1 microsecond',
        'results': [],
    },
    {
        # Partially parsed
        'query': 'time + 0.1 microsecond',
        'results': [
            get_resultexc(
                '+ 0.1',
                MisparsedDateTimeException,
                name_post=': "time + 0.1"',
                desc_post=': "time + 0.1 microsecond"',
            ),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_simple)
def test_simple(test_spec):
    with set_time_reference(time_reference):
        query_test_helper(TimeQueryHandler, test_spec)


test_spec_target_city = [
    {
        # Normal test with target city
        'query': 'time at Vancouver',
        'results': [
            get_resulttz(
                'Vancouver',
                'Canada',
                'CA',
                query='at Vancouver',
                order=0,
                value=dt(tz='America/Vancouver'),
            ),
            get_resulttz(
                'Vancouver',
                'WA United States',
                'US',
                query='at Vancouver',
                order=1,
                value=dt(tz='America/Los_Angeles'),
            ),
            get_result('Now', query='', order=2),
        ],
    },
    {
        # Normal test with target city, country
        'query': 'time at Paris France',
        'results': [
            get_resulttz(
                'Paris',
                'France',
                'FR',
                query='at Paris France',
                order=0,
                value=dt(tz='Europe/Paris'),
            ),
            get_result('Now', query='', order=1),
        ],
    },
    {
        # Normal test with uknown city
        'query': 'time at SomeCityThatDoesNotExist',
        'results': [get_result('Now', query='', order=0)],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_target_city)
def test_target_city(test_spec):
    with set_time_reference(time_reference):
        query_test_helper(TimeQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_time = [
    {
        # Normal test with time calculation
        'query': 'time + 2 MONTH 2 day 2 HoUrS 30 minutes 2 seconds - '
        '2 months 26 hour 30 minutes 2 SeCond',
        'results': [
            get_result(
                'Tomorrow',
                query='+ 2 MONTH 2 day 2 HoUrS 30 minutes 2 seconds - '
                '2 months 26 hour 30 minutes 2 SeCond',
                order=0,
                value=dt(datetime(2021, 7, 16, 14, 0, 0)),
            ),
            get_resulttz(
                'Athens',
                'Greece',
                'GR',
                query='+ 2 MONTH 2 day 2 HoUrS 30 minutes 2 seconds - '
                '2 months 26 hour 30 minutes 2 SeCond',
                order=1,
                value=dt(datetime(2021, 7, 16, 14, 0, 0), tz='Europe/Athens'),
            ),
            get_resulttz(
                'New York City',
                'NY United States',
                'US',
                query='+ 2 MONTH 2 day 2 HoUrS 30 minutes 2 seconds - '
                '2 months 26 hour 30 minutes 2 SeCond',
                order=2,
                value=dt(
                    datetime(2021, 7, 16, 14, 0, 0), tz='America/New_York'
                ),
            ),
        ],
    },
    {
        # Test partial matching
        'query': 'time + 1 day 2 some text',
        'results': [
            get_resultexc(
                '+ 1 day',
                MisparsedDateTimeException,
                name_post=': "time + 1 day"',
                desc_post=': "time + 1 day 2 some text"',
            ),
            get_result(
                'Tomorrow',
                query='+ 1 day',
                order=0,
                value=dt(datetime(2021, 7, 16, 14, 0, 0)),
            ),
            get_resulttz(
                'Athens',
                'Greece',
                'GR',
                query='+ 1 day',
                order=1,
                value=dt(datetime(2021, 7, 16, 14, 0, 0), tz='Europe/Athens'),
            ),
            get_resulttz(
                'New York City',
                'NY United States',
                'US',
                query='+ 1 day',
                order=2,
                value=dt(
                    datetime(2021, 7, 16, 14, 0, 0), tz='America/New_York'
                ),
            ),
        ],
    },
    {
        # Test overflows
        'query': 'time + 20000000 YeaRs',
        'results': [get_resultexc('+ 20000000 YeaRs', DateOverflowException)],
    },
    {
        # Invalid query 1
        'query': 'time ++ 1 month',
        'results': [],
    },
    {
        # Invalid query 2
        'query': 'time + 1 month - - 2 days +- 1 month',
        'results': [],
    },
    {
        # Invalid query 3
        'query': 'time + 1 at Paris',
        'results': [],
    },
    {
        # Invalid query 4
        'query': 'time + Some random string',
        'results': [],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_time)
def test_time(test_spec):
    with set_time_reference(time_reference):
        query_test_helper(TimeQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_time_target_city = [
    {
        # Normal test with time calculation and target city
        'query': 'time - 1 WeEk 1 DaY 2 HouR 56 min At ParIs',
        'results': [
            get_resulttz(
                'Paris',
                'France',
                'FR',
                query='- 1 WeEk 1 DaY 2 HouR 56 min At ParIs',
                order=0,
                value=dt(datetime(2021, 7, 7, 11, 4, 0), tz='Europe/Paris'),
            ),
            get_resulttz(
                'Paris',
                'TX United States',
                'US',
                query='- 1 WeEk 1 DaY 2 HouR 56 min At ParIs',
                order=1,
                value=dt(datetime(2021, 7, 7, 11, 4, 0), tz='America/Chicago'),
            ),
            get_result(
                tr_time('last-week').capitalize(),
                query='- 1 WeEk 1 DaY 2 HouR 56 min',
                order=2,
                value=dt(datetime(2021, 7, 7, 11, 4, 0)),
            ),
        ],
    },
    {
        'query': 'time + 1 month at Prague CzEcHia',
        'results': [
            get_resulttz(
                'Prague',
                'Czechia',
                'CZ',
                query='+ 1 month at Prague CzEcHia',
                order=0,
                value=dt(datetime(2021, 8, 15, 14, 0, 0), tz='Europe/Prague'),
            ),
            get_result(
                tr_time('next-month').capitalize(),
                query='+ 1 month',
                order=1,
                value=dt(datetime(2021, 8, 15, 14, 0, 0)),
            ),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_time_target_city)
def test_time_target_city(test_spec):
    with set_time_reference(time_reference):
        query_test_helper(TimeQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_until = [
    {
        # Normal test
        'query': 'time uNTill tomorrow',
        'results': [
            get_resulttd(
                timedelta(seconds=68400), query='uNTill tomorrow', order=0
            ),
            get_result('Now', query='uNTill tomorrow', order=1),
        ],
    },
    {
        # Test february 29 leap year
        'query': 'time until Feb 29 2024',
        'results': [
            get_resulttd(
                timedelta(days=959), query='until Feb 29 2024', order=0
            ),
            get_result('Now', query='until Feb 29 2024', order=1),
        ],
    },
    {
        # Test february 29 no year
        'query': 'time until Feb 29 2025',
        'results': [get_resultexc('until Feb 29 2025', DateOverflowException)],
    },
    {
        # Cannot parse until
        'query': 'time till SomeRandomString',
        'results': [
            get_resultexc(
                'till',
                MisparsedDateTimeException,
                name_post=': "time till"',
                desc_post=': "time till SomeRandomString"',
            ),
            get_result('Now', query='till', order=0),
        ],
    },
    {
        # Partial parse until
        'query': 'time tIl tomorrow midnight m',
        'results': [
            get_resultexc(
                'tIl tomorrow midnight',
                MisparsedDateTimeException,
                name_post=': "time tIl tomorrow midnight"',
                desc_post=': "time tIl tomorrow midnight m"',
            ),
            get_resulttd(
                timedelta(days=1, seconds=36000),
                query='tIl tomorrow midnight',
                order=0,
            ),
            get_result('Now', query='tIl tomorrow midnight', order=1),
        ],
    },
    {
        # Do not match digits only
        'query': 'time until 1245',
        'results': [
            get_resultexc(
                'until',
                MisparsedDateTimeException,
                name_post=': "time until"',
                desc_post=': "time until 1245"',
            ),
            get_result('Now', query='until', order=0),
        ],
    },
    {
        # Test overflows
        'query': 'time until 20000 yEaR',
        'results': [get_resultexc('until 20000 yEaR', DateOverflowException)],
    },
    {
        # Some generic testing 1
        'query': 'time until',
        'results': [
            get_result('Now', query='until', order=0),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_until)
def test_until(test_spec):
    with set_time_reference(time_reference):
        query_test_helper(TimeQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_parsedatetime_missing = [
    {
        # Normal test with time calculation and target city
        'query': 'time',
        'results': [
            {
                'result': {
                    'value': None,
                    'query': '',
                    'error': MissingParsedatetimeException,
                    'order': MissingParsedatetimeException.order,
                },
                'query_result': {
                    'icon': images_dir('time.svg'),
                    'name': tr_err('missing-parsedatetime-error'),
                    'description': tr_err(
                        'missing-parsedatetime-error-description'
                    ),
                    'clipboard': '/usr/bin/python3 -m pip install '
                    'parsedatetime',
                    'error': MissingParsedatetimeException,
                    'value': None,
                    'value_type': type(None),
                    'order': MissingParsedatetimeException.order,
                },
            }
        ],
    }
]


@pytest.mark.parametrize('test_spec', test_spec_parsedatetime_missing)
def test_parsedatetime_missing(test_spec):
    # Set parsedatetime to None
    with no_parsedatetime(), reset_instance(TimeQueryHandler):
        query_test_helper(TimeQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


# Some more tests for coverage
test_spec_cov = [
    {
        # Last year
        'query': 'time - 1 year',
        'results': [
            get_result(
                'Last year',
                query='- 1 year',
                order=0,
                value=dt(datetime(2020, 7, 15, 14, 0, 0)),
            ),
        ],
    },
    {
        # Next year
        'query': 'time + 1 year',
        'results': [
            get_result(
                'Next year',
                query='+ 1 year',
                order=0,
                value=dt(datetime(2022, 7, 15, 14, 0, 0)),
            ),
        ],
    },
    {
        # Years from now
        'query': 'time + 10 years',
        'results': [
            get_result(
                '10 years from now',
                query='+ 10 years',
                order=0,
                value=dt(datetime(2031, 7, 15, 14, 0, 0)),
            ),
        ],
    },
    {
        # Years ago
        'query': 'time - 5 years',
        'results': [
            get_result(
                '5 years ago',
                query='- 5 years',
                order=0,
                value=dt(datetime(2016, 7, 15, 14, 0, 0)),
            ),
        ],
    },
    {
        # Last month
        'query': 'time - 1 month',
        'results': [
            get_result(
                'Last month',
                query='- 1 month',
                order=0,
                value=dt(datetime(2021, 6, 15, 14, 0, 0)),
            ),
        ],
    },
    {
        # Next month
        'query': 'time + 1 month',
        'results': [
            get_result(
                'Next month',
                query='+ 1 month',
                order=0,
                value=dt(datetime(2021, 8, 15, 14, 0, 0)),
            ),
        ],
    },
    {
        # months from now
        'query': 'time + 2 months',
        'results': [
            get_result(
                '2 months from now',
                query='+ 2 months',
                order=0,
                value=dt(datetime(2021, 9, 15, 14, 0, 0)),
            ),
        ],
    },
    {
        # months ago
        'query': 'time - 5 months',
        'results': [
            get_result(
                '5 months ago',
                query='- 5 months',
                order=0,
                value=dt(datetime(2021, 2, 15, 14, 0, 0)),
            ),
        ],
    },
    {
        # next week
        'query': 'time + 1 week',
        'results': [
            get_result(
                'Next week',
                query='+ 1 week',
                order=0,
                value=dt(datetime(2021, 7, 22, 14, 0, 0)),
            ),
        ],
    },
    {
        # last week
        'query': 'time - 1 week',
        'results': [
            get_result(
                'Last week',
                query='- 1 week',
                order=0,
                value=dt(datetime(2021, 7, 8, 14, 0, 0)),
            ),
        ],
    },
    {
        # weeks from now
        'query': 'time + 2 weeks',
        'results': [
            get_result(
                '2 weeks from now',
                query='+ 2 weeks',
                order=0,
                value=dt(datetime(2021, 7, 29, 14, 0, 0)),
            ),
        ],
    },
    {
        # weeks ago
        'query': 'time - 2 weeks',
        'results': [
            get_result(
                '2 weeks ago',
                query='- 2 weeks',
                order=0,
                value=dt(datetime(2021, 7, 1, 14, 0, 0)),
            ),
        ],
    },
    {
        # yesterday
        'query': 'time - 1 day',
        'results': [
            get_result(
                'Yesterday',
                query='- 1 day',
                order=0,
                value=dt(datetime(2021, 7, 14, 14, 0, 0)),
            ),
        ],
    },
    {
        # in 2 days
        'query': 'time + 2 days',
        'results': [
            get_result(
                '2 days from now',
                query='+ 2 days',
                order=0,
                value=dt(datetime(2021, 7, 17, 14, 0, 0)),
            ),
        ],
    },
    {
        # 3 days ago
        'query': 'time - 3 days',
        'results': [
            get_result(
                '3 days ago',
                query='- 3 days',
                order=0,
                value=dt(datetime(2021, 7, 12, 14, 0, 0)),
            ),
        ],
    },
    {
        # today
        'query': 'time + 5 hours 3 minutes',
        'results': [
            get_result(
                'Today',
                query='+ 5 hours 3 minutes',
                order=0,
                value=dt(datetime(2021, 7, 15, 19, 3, 0)),
            ),
        ],
    },
    {
        # today
        'query': 'time until 1 day ago',
        'results': [
            get_resulttd(timedelta(days=-1), query='until 1 day ago', order=0),
            get_result('Now', query='until 1 day ago', order=1),
        ],
    },
    {
        # months diff last year but not full year
        'query': 'time until 8 months ago',
        'results': [
            get_resulttd(
                timedelta(days=-242), query='until 8 months ago', order=0
            ),
            get_result('Now', query='until 8 months ago', order=1),
        ],
    },
    {
        # years diff
        'query': 'time until next 2 years',
        'results': [
            get_resulttd(
                timedelta(days=730), query='until next 2 years', order=0
            ),
            get_result('Now', query='until next 2 years', order=1),
        ],
    },
    {
        # minutes diff
        'query': 'time until next 4 minutes',
        'results': [
            get_resulttd(
                timedelta(seconds=240), query='until next 4 minutes', order=0
            ),
            get_result('Now', query='until next 4 minutes', order=1),
        ],
    },
    {
        # seconds diff
        'query': 'time until 10 seconds ago',
        'results': [
            get_resulttd(
                timedelta(days=-1, seconds=86390),
                query='until 10 seconds ago',
                order=0,
            ),
            get_result('Now', query='until 10 seconds ago', order=1),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_cov)
def test_coverage(test_spec):
    with reset_instance(TimezoneService), no_default_cities():
        with set_time_reference(time_reference):
            query_test_helper(TimeQueryHandler, test_spec)
            query_test_helper(MultiHandler, test_spec, raw=True)
            query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)
