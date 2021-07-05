from datetime import datetime, timedelta
from re import sub
try:
    import parsedatetime
except ImportError:
    parsedatetime = None
from .units import UnitsQueryHandler
from .interface import QueryHandler
from ..lang import Language
from ..result import QueryResult
from ...utils import Singleton
from ...constants import TIME_QUERY_REGEX, TIME_SUBQUERY_REGEX, TIME_SUBQUERY_DIGITS, TIME_SPLIT_REGEX

class TimeQueryHandler(QueryHandler, metaclass=Singleton):

    def handle(self, query):
        query = query.lower()

        if not TIME_QUERY_REGEX.match(query):
            return

        translator = Language().get_translator("time")

        if parsedatetime is None:
            return [QueryResult(
                icon='images/time.svg',
                value='pip install parsedatetime',
                name=translator('install-parsedatetime'),
                description=translator('install-parsedatetime-description'),
                is_error=True,
                order=-1
            )]

        query = TIME_QUERY_REGEX.sub('now', query)
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
            elif subquery == 'now':
                if prev != '+' and prev is not None:
                    return None
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

        value = date.strftime('%A %-d %B %Y %H:%M:%S')

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

        return [QueryResult(
            icon='images/time.svg',
            value=value,
            name=value,
            description=description,
            order=0
        )]
    