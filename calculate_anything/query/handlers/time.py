from datetime import datetime, timedelta
try:
    import parsedatetime
except ImportError:
    parsedatetime = None
from .units import UnitsQueryHandler
from .interface import QueryHandler
from ..lang import Language
from ..result import QueryResult
from ...utils import Singleton
from ...constants import TIME_QUERY_REGEX, TIME_SPLIT_REGEX

class TimeQueryHandler(QueryHandler, metaclass=Singleton):

    def handle(self, query):
        query = query.lower()

        if not TIME_QUERY_REGEX.match(query):
            return

        if parsedatetime is None:
            return [QueryResult(
                icon='images/time.svg',
                value='pip install parsedatetime',
                name='Looks like parsedatetime is not installed.',
                description='Install it with "pip install parsedatetime" and restart launcher.',
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
                diff = cal.nlp(subquery, sourceTime=datetime.min)
                if diff is None:
                    return None
                diff = diff[0][0] - datetime.min
                if prev == '+':
                    date += diff
                else:
                    date -= diff
            prev = subquery
        
        date = date + now

        value = date.strftime('%A %-d %B %Y %H:%M:%S')

        now_week = now.isocalendar()[1]
        date_week = date.isocalendar()[1]

        if now.year - 1 == date.year:
            description = Language().translate('Last year', 'dates')
        elif now.year + 1 == date.year:
            description = Language().translate('Next year', 'dates')
        elif now.year != date.year:
            if date.year > now.year:
                description = Language().translate('years from now', 'dates')
            else:
                description = Language().translate('years ago', 'dates')
            description = '{} {}'.format(abs(now.year - date.year), description)
        elif now.month - 1 == date.month:
            description = Language().translate('Last month', 'dates')
        elif now.month + 1 == date.month:
            description = Language().translate('Next month', 'dates')
        elif now.month != date.month:
            if date.month > now.month:
                description = Language().translate('months from now', 'dates')
            else:
                description = Language().translate('months ago', 'dates')
            description = '{} {}'.format(abs(now.month - date.month), description)
        elif now_week - 1 == date_week:
            description = Language().translate('Last week', 'dates')
        elif now_week + 1 == date_week:
            description = Language().translate('Next week', 'dates')
        elif now_week != date_week:
            if date_week > now_week:
                description = Language().translate('weeks from now', 'dates')
            else:
                description = Language().translate('weeks ago', 'dates')
            description = '{} {}'.format(abs(now_week - date_week), description)
        elif now.day - 1 == date.day:
            description = Language().translate('Last day', 'dates')
        elif now.day + 1 == date.day:
            description = Language().translate('Next day', 'dates')
        elif now.day != date.day:
            if date.day > now.day:
                description = Language().translate('days from now', 'dates')
            else:
                description = Language().translate('days ago', 'dates')
            description = '{} {}'.format(abs(now.day - date.day), description)
        else:
            description = Language().translate('Today', 'dates')

        return [QueryResult(
            icon='images/time.svg',
            value=value,
            name=value,
            description=description,
            order=0
        )]
    