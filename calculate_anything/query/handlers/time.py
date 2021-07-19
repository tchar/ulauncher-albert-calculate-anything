import re
import pytz
from datetime import datetime, timedelta
try:
    import parsedatetime
except ImportError:
    parsedatetime = None
from .interface import QueryHandlerInterface
from ...calculation import LocationTimeCalculation, TimeCalculation, TimedeltaCalculation
from ...time.service import TimezoneService
from ...exceptions import DateAddDateException, MissingParsedatetimeException, DateOverflowException, MisparsedTimeException
from ...utils import Singleton, partition
from ... import logging 
from ...constants import (
    TIME_QUERY_REGEX, TIME_QUERY_REGEX_SPLIT, TIME_SUBQUERY_REGEX,
    TIME_SUBQUERY_DIGITS, TIME_SPLIT_REGEX, PLUS_MINS_REGEX,
    TIME_LOCATION_REPLACE_REGEX
)

class TimeQueryHandler(QueryHandlerInterface, metaclass=Singleton):

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._date_reference = datetime(year=2000, month=1, day=1)

    @staticmethod
    def _timedelta_overflows(query, td):
        is_zero = TIME_SUBQUERY_DIGITS.findall(query)
        is_zero = map(float, is_zero)
        is_zero = map(lambda x: x == 0, is_zero)
        is_zero = all(is_zero)
        return not is_zero and td == timedelta()

    def _get_location_search_combinations(location):
        location = location.strip()
        if not location:
            return []

        locations_tmp = TIME_LOCATION_REPLACE_REGEX.sub(' ', location)
        locations_tmp = locations_tmp.split(' ')
        locations_tmp = map(str.strip, locations_tmp)
        locations_tmp = filter(None, locations_tmp)
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
        if len(location) >= 2:
            locations = TimeQueryHandler._get_location_search_combinations(location)
        else:
            locations = []

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

    def _get_until(self, query):
        now = datetime.now()
        cal = parsedatetime.Calendar()
        try:
            date = cal.nlp(query, sourceTime=now)
            if date is None:
                return [TimeCalculation(
                    value=now,
                    reference_date=now,
                    order=0
                )]

            date, flags, _, _, parsed_query = date[0]
            if re.match(r'^\s*\d+\s*$', parsed_query):
                return []

            if flags == 0:
                raise OverflowError

            diff = date - now
            # Adjust midnights because they refer to same day whereas it should be "tomorrow"
            is_currently_midnight = now.hour | now.minute | now.second | now.microsecond == 0
            if not is_currently_midnight and 'midnight' in parsed_query:
                date += timedelta(days=1)
            overflows = False
            if TimeQueryHandler._timedelta_overflows(query, diff):
                overflows = True
        except OverflowError as e:
            overflows = True

        if overflows:
            item = TimedeltaCalculation(error=DateOverflowException)
            return [item]

        items = []
        if parsed_query != query:
            item = TimedeltaCalculation(
                error=MisparsedTimeException(
                    message='Could not fully parse',
                    extra={
                        'original_query': query,
                        'parsed_query': parsed_query
                    }
                ),
                order=-1
            )
            items.append(item)
        items.append(
            TimedeltaCalculation(
                value=date,
                reference_date=now,
                query=query,
                order=len(items)
            )
        )
        items.append(TimeCalculation(
            value=now,
            reference_date=now,
            order=0
        ))
        return items

    def _calculate(self, query, suffix, try_again):
        query = TIME_SPLIT_REGEX.split(query)
        query = map(str.strip, query)
        query = filter(None, query)
        query = list(query)
    
        signs = set(['+', '-'])
        cal = parsedatetime.Calendar()
        date_td = timedelta()
        prev = None

        misparsed = False
        parsed_subqueries = query.copy()
        date_overflows_error = False
        date_add_date_error = False

        for i, subquery in enumerate(query):
            if subquery == '+':
                if prev in signs:
                    return []
            elif subquery == '-':
                if prev in signs:
                    return []
            else:
                if prev not in signs:
                    if not try_again:
                        return []
                    new_query = 'now at ' + ' '.join(query).replace('now', '')
                    return self.handle(new_query, try_again=False)

                if not TIME_SUBQUERY_REGEX.match(subquery):
                    return []
                
                try:
                    diff = cal.nlp(subquery, sourceTime=self._date_reference)
                except (ValueError, OverflowError):
                    date_add_date_error = True
                    break
                if diff is None:
                    return []

                diff, _, _, _, parsed_query = diff[0]
                if parsed_query != subquery:
                    parsed_subqueries[i] = parsed_query
                    misparsed = True
                    
                diff = diff - self._date_reference

                if TimeQueryHandler._timedelta_overflows(subquery, diff):
                    date_overflows_error = True
                    break

                if prev == '+':
                    date_td += diff
                else:
                    date_td -= diff
            prev = subquery

        items = []
        if misparsed:
            original_query = ' '.join(query)
            parsed_query = ' '.join(parsed_subqueries)
            item = TimeCalculation(
                error=MisparsedTimeException(
                    'Could not fully parse',
                    extra={
                        'original_query': original_query,
                        'parsed_query': parsed_query
                    }
                )
            )
            items.append(item)

        if date_add_date_error:
            item = TimeCalculation(error=DateAddDateException, order=len(items))
            items.append(item)
            return items

        now = datetime.now()
        try:
            date = now + date_td
        except OverflowError:
            date_overflows_error

        if date_overflows_error:
            item = TimeCalculation(error=DateOverflowException, order=len(items))
            items.append(item)
            return items

        locations, added_defaults = self._get_locations(suffix)
        order_offset_locations = len(items) + 1 if added_defaults else len(items)
        location_items = (
            self._get_time_location(
                date,
                locations,
                order_offset=order_offset_locations
            )
        )
        order_next = len(items) if added_defaults else len(items) + len(location_items)
        items.extend(location_items)

        item = TimeCalculation(
            value=date,
            reference_date=now,
            order=order_next
        )
        items.append(item)
        return items

    def handle(self, query, try_again=True):
        if parsedatetime is None:
            result = TimeCalculation(
                error=MissingParsedatetimeException,
                order=-1
            )
            return [result]
            
        query = query.lower()
        query = PLUS_MINS_REGEX.sub_dict(query)

        if not TIME_QUERY_REGEX.match(query):
            return

        query = TIME_QUERY_REGEX_SPLIT.split(query, maxsplit=1)
        if len(query) > 1:
            query, keyword, suffix = map(str.strip, query)
        else:
            query = query[0].strip()
            keyword = ''
            suffix = ''

        query = TIME_QUERY_REGEX.sub('', query)
        if 'til' in keyword and query.strip() == '':
            items = self._get_until(suffix)
        else:
            items = self._calculate(query, suffix, try_again)
        
        return items
