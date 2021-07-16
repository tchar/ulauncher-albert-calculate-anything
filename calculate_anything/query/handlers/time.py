import re
import pytz
from datetime import datetime, timedelta
try:
    import parsedatetime
except ImportError:
    parsedatetime = None
from .interface import QueryHandlerInterface
from ...calculation import LocationTimeCalculation, TimeCalculation
from ...time.service import TimezoneService
from ...exceptions import MissingParsedatetimeException, DateOverflowException
from ...utils import Singleton, partition
from ...logging_wrapper import LoggingWrapper
from ...constants import (
    TIME_QUERY_REGEX, TIME_QUERY_REGEX_SPLIT, TIME_SUBQUERY_REGEX,
    TIME_SUBQUERY_DIGITS, TIME_SPLIT_REGEX, PLUS_MINUS_REGEX_REPLACE_FUNC,
    TIME_LOCATION_REPLACE_REGEX
)

class TimeQueryHandler(QueryHandlerInterface, metaclass=Singleton):

    def __init__(self):
        self._logger = LoggingWrapper.getLogger(__name__)

    def _get_location_search_combinations(location):
        location = location.strip()
        if not location:
            return []

        locations_tmp = TIME_LOCATION_REPLACE_REGEX.sub(' ', location)
        locations_tmp = locations_tmp.split(' ')
        locations_tmp = map(str.strip, locations_tmp)
        locations_tmp = filter(lambda s: s, locations_tmp)
        locations_tmp = list(locations_tmp)
        locations_tmp = partition(locations_tmp)

        locations = []
        for item in locations_tmp:
            location = ' '.join(map(str, item[0]))
            search_terms = [' '.join(map(str, sublist)) for sublist in item[1:]]
            locations.append((location, search_terms))
        return sorted(locations, key=lambda item: len(item[0]))

    def _get_locations(self, location):
        search_terms = []
        locations = TimeQueryHandler._get_location_search_combinations(location)
        
        if not locations:
            return TimezoneService().get_defaults(), True
        
        for location, search_terms in locations:
            location, search_terms
            found_locations = TimezoneService().get(location, *search_terms)
            if found_locations:
                return found_locations, False

        return [], True

    def _get_time_location(self, date, locations, order_offset=0):
        items = []
        order = 0
        for location in locations:
            try:
                tz = pytz.timezone(location['timezone'])
            except pytz.UnknownTimeZoneError as e:
                self._logger.error('Could not find time zone: {}'.format(location))
                continue
            
            location_datetime = date.astimezone(tz)
            item = LocationTimeCalculation(
                value=location_datetime,
                location=location,
                order=order+order_offset
            )
            items.append(item)
            order += 1
        return items


    def handle(self, query, try_again=True):
        if parsedatetime is None:
            result = TimeCalculation(
                error=MissingParsedatetimeException,
                order=-1
            )
            return [result]
            
        query = query.lower()
        query = PLUS_MINUS_REGEX_REPLACE_FUNC(query)

        if len(TIME_QUERY_REGEX.findall(query)) != 1:
            return

        query = TIME_QUERY_REGEX_SPLIT.split(query, maxsplit=1)
        if len(query) > 1:
            query, location = map(str.strip, query)
        else:
            query = query[0].strip()
            location = ''

        query = TIME_QUERY_REGEX.sub('', query)
        query = TIME_SPLIT_REGEX.split(query)
        query = map(str.strip, query)
        query = list(query)

        signs = set(['+', '-'])
        cal = parsedatetime.Calendar()
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
                    if not try_again: return None
                    new_query = 'now at ' + ' '.join(query).replace('now', '')
                    return self.handle(new_query, try_again=False)

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
            date += datetime.now()
        except OverflowError:
            date_overflows = True
            
        if date_overflows:
            result = TimeCalculation(error=DateOverflowException)
            return [result]

        locations, add_defaults = self._get_locations(location)
        order_offset_locations = 1 if add_defaults else 0
    

        items = []
        items.extend(
            self._get_time_location(
                date,
                locations, 
                order_offset=order_offset_locations
            )
        )

        item = TimeCalculation(
            value=date,
            order=0 if add_defaults else len(items)
        )
        items.append(item)
        return items
