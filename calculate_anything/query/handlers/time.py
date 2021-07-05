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
        now = datetime.now().replace(microsecond=0)
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
                date += now
            else:
                if prev not in signs:
                    return None
                diff = cal.nlp(subquery, sourceTime=datetime.min)
                if diff is None:
                    return None
                if prev == '+':
                    date += diff[0][0] - datetime.min
                else:
                    date -= diff[0][0] - datetime.min
            prev = subquery

        date = date.replace(microsecond=0)
        value = '{}'.format(date)
        if now.date() == date.date() and now != date:
            name = '{} {}'.format(Language().translate('Today at', 'dates'), date.time())
        elif now.date() + timedelta(days=1) == date.date():
            name = '{} {}'.format(Language().translate('Tomorrow at', 'dates'), date.time(), date.time())
        elif now.date() - timedelta(days=1) == date.date():
            name = '{} {}'.format(Language().translate('Yesterday at', 'dates'), date.time(), date.time())
        else:
            name = '{}'.format(date)

        return [QueryResult(
            icon='images/time.svg',
            value=value,
            name=name,
            order=0
        )]