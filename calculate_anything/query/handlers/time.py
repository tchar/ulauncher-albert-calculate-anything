from re import search
import pytz
from datetime import datetime, timedelta
try:
    import parsedatetime
except ImportError:
    parsedatetime = None
from .interface import QueryHandler
from ..lang import Language
from ..result import QueryResult
from ...time.service import TimezoneService
from ...utils import Singleton
from ...logging_wrapper import LoggingWrapper
from ...constants import FLAGS, TIME_QUERY_REGEX, TIME_QUERY_REGEX_SPLIT, TIME_SUBQUERY_REGEX, TIME_SUBQUERY_DIGITS, TIME_SPLIT_REGEX

class TimeQueryHandler(QueryHandler, metaclass=Singleton):
    DATETIME_FORMAT = '%A %-d %B %Y %H:%M:%S'
    DATE_FORMAT = '%A %-d %B %Y'
    TIME_FORMAT = '%H:%M:%S'

    def __init__(self):
        self._logger = LoggingWrapper.getLogger(__name__)

    def _get_time_location(self, date, location, order_offset=0):
        items = []
        search_terms = []
        if location:
            location = location.split(',')
            location, search_terms = location[0].strip(), map(str.strip, location[1:])
        locations = TimezoneService().get(location, *search_terms, add_defaults=location == '')
        if not locations:
            return items

        order = 0
        for location in locations:
            try:
                tz = pytz.timezone(location['timezone'])
            except pytz.UnknownTimeZoneError as e:
                self._logger.error('Could not find time zone: {}'.format(location))
                continue
            location_datetime = date.astimezone(tz)
            timezone_name = location_datetime.tzname()
            utc = int(location_datetime.utcoffset().total_seconds() / 60 / 60)
            utc = 'UTC{:+}'.format(utc)
            
            location_time = location_datetime.strftime(TimeQueryHandler.TIME_FORMAT)
            location_date = location_datetime.strftime(TimeQueryHandler.DATE_FORMAT)
            
            city_name = location['name']
            country_name = location['country']
            country_code = location['cc'].upper()
            if country_code == 'US':
                state_name = location['state'].upper()
                country_name = '{} {}'.format(state_name, country_name)

            name = '{}: {}'.format(city_name, location_time)
            description = '{} - {} - {} ({}) '.format(location_date, country_name, timezone_name, utc)

            if country_code in FLAGS:
                icon = 'images/flags/{}'.format(FLAGS[country_code])
            else:
                icon = 'images/country.svg'

            items.append(QueryResult(
                icon=icon,
                value=name,
                name=name,
                description=description,
                order=order + order_offset
            ))
            order += 1
        return items

    def handle(self, query):
        translator = Language().get_translator('time')

        if parsedatetime is None:
            return [QueryResult(
                icon='images/time.svg',
                value='pip install parsedatetime',
                name=translator('install-parsedatetime'),
                description=translator('install-parsedatetime-description'),
                is_error=True,
                order=-1
            )]

        query = query.lower()
        if len(TIME_QUERY_REGEX.findall(query)) != 1:
            return

        query = TIME_QUERY_REGEX_SPLIT.split(query)
        if len(query) > 1:
            query, location = map(str.strip, query) 
        else:
            query = query[0].strip()
            location = ''

        query = TIME_QUERY_REGEX.sub('', query)
        query = TIME_SPLIT_REGEX.split(query)
        query = map(str.strip, query)

        signs = set(['+', '-'])
        cal = parsedatetime.Calendar()
        now = datetime.now()
        date = timedelta()
        prev = None

        date_overflows = False

        for subquery in query:
            if subquery == '+':
                if prev in signs:
                    return None
            elif subquery == '-':
                if prev in signs:
                    return None
            elif subquery == '':
                pass
            else:
                if prev not in signs:
                    return None

                if not TIME_SUBQUERY_REGEX.match(subquery):
                    return None
                
                diff = cal.nlp(subquery, sourceTime=datetime.min)
                if diff is None:
                    return None

                diff = diff[0][0] - datetime.min

                is_zero = TIME_SUBQUERY_DIGITS.findall(subquery)
                is_zero = map(float, is_zero)
                is_zero = map(lambda x: x == 0, is_zero)
                is_zero = all(is_zero)

                if not is_zero and diff == timedelta():
                    date_overflows = True
                    break

                if prev == '+':
                    date += diff
                else:
                    date -= diff
            prev = subquery
        
        try:
            date += now
        except OverflowError:
            date_overflows = True

        if date_overflows:
            return [QueryResult(
                icon='images/time.svg',
                value='',
                name=translator('years-overflow'),
                description=translator('years-overflow-description'),
                order=0
            )]

        value = date.strftime(TimeQueryHandler.DATETIME_FORMAT)

        now_week = now.isocalendar()[1]
        date_week = date.isocalendar()[1]

        if now.year - 1 == date.year:
            description = translator('last-year')
        elif now.year + 1 == date.year:
            description = translator('next-year')
        elif now.year != date.year:
            if date.year > now.year:
                description = translator('years-from-now')
            else:
                description = translator('years-ago')
            description = '{} {}'.format(abs(now.year - date.year), description)
        elif now.month - 1 == date.month:
            description = translator('last-month')
        elif now.month + 1 == date.month:
            description = translator('next-month')
        elif now.month != date.month:
            if date.month > now.month:
                description = translator('months-from-now')
            else:
                description = translator('months ago')
            description = '{} {}'.format(abs(now.month - date.month), description)
        elif now_week - 1 == date_week:
            description = translator('last-week')
        elif now_week + 1 == date_week:
            description = translator('next-week')
        elif now_week != date_week:
            if date_week > now_week:
                description = translator('weeks-from-now')
            else:
                description = translator('weeks-ago')
            description = '{} {}'.format(abs(now_week - date_week), description)
        elif now.day - 1 == date.day:
            description = translator('yesterday')
        elif now.day + 1 == date.day:
            description = translator('tomorrow')
        elif now.day != date.day:
            if date.day > now.day:
                description = translator('days-from-now')
            else:
                description = translator('days-ago')
            description = '{} {}'.format(abs(now.day - date.day), description)
        else:
            description = translator('today')

        items = [QueryResult(
            icon='images/time.svg',
            value=value,
            name=value,
            description=description,
            order=0
        )]

        items.extend(self._get_time_location(date, location, order_offset=len(items)))
        return items
