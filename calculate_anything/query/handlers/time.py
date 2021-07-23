import re
import pytz
from datetime import datetime, timedelta
try:
    import parsedatetime
except ImportError:
    parsedatetime = None
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything.calculation.time import (
    LocationTimeCalculation, TimeCalculation,
    TimedeltaCalculation
)
from calculate_anything.time.service import TimezoneService
from calculate_anything.exceptions import (
    DateAddDateException, MissingParsedatetimeException,
    DateOverflowException, MisparsedTimeException
)
from calculate_anything.utils.singleton import Singleton
from calculate_anything.utils.iter import partition, flatten, deduplicate
from calculate_anything.logging_wrapper import LoggingWrapper as logging
from calculate_anything.constants import (
    TIME_QUERY_REGEX_SPLIT, TIME_SUBQUERY_REGEX,
    TIME_SPLIT_REGEX, PLUS_MINUS_REGEX,
    TIME_LOCATION_REPLACE_REGEX
)


class TimeQueryHandler(QueryHandler, metaclass=Singleton):

    def __init__(self):
        super().__init__('time')
        self._logger = logging.getLogger(__name__)
        if parsedatetime is not None:
            self._cal = parsedatetime.Calendar(
                version=parsedatetime.VERSION_CONTEXT_STYLE)
        else:
            self._cal = None

    # TODO: To be removed
    # @staticmethod
    # def _timedelta_overflows(query, td):
    #     is_zero = TIME_SUBQUERY_DIGITS.findall(query)
    #     is_zero = map(float, is_zero)
    #     is_zero = map(lambda x: x == 0, is_zero)
    #     is_zero = all(is_zero)
    #     return not is_zero and td == timedelta()

    def _parse_dt(self, query, reference_datetime):
        try:
            date = self._cal.nlp(query, sourceTime=reference_datetime)
        except Exception as e:
            self._logger.exception(
                'Got unexpected exception when parsing datetime: '
                '{} with reference time {}: {}'
                .format(query, reference_datetime, e))
            return None, None, None, None, False

        if date is None:
            return None, None, None, None, False

        date, flags, _, _, parsed_query = date[0]
        regex_match = re.match(r'^\s*\d+\s*$', parsed_query) is None
        overflow = flags == parsedatetime.pdtContext(0)
        td = date - reference_datetime
        return date, td, parsed_query, regex_match, overflow

    def _get_location_search_combinations(location):
        location = location.strip()
        locations_tmp = TIME_LOCATION_REPLACE_REGEX.sub(' ', location)
        locations_tmp = locations_tmp.split(' ')
        locations_tmp = map(str.strip, locations_tmp)
        locations_tmp = filter(None, locations_tmp)
        locations_tmp = list(locations_tmp)
        locations_tmp = partition(locations_tmp)

        locations = []
        for item in locations_tmp:
            location = ' '.join(map(str, item[0]))
            search_terms = flatten(item[1:])
            search_terms = deduplicate(search_terms)
            search_terms = tuple(search_terms)
            locations.append((location, search_terms))

        locations = deduplicate(locations)
        return locations

    def _get_locations(self, location):
        search_terms = []
        if len(location) < 2:
            return TimezoneService().get_defaults(), True

        locations = TimeQueryHandler._get_location_search_combinations(
            location)

        for location, search_terms in locations:
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
            except pytz.UnknownTimeZoneError as e:  # pragma: no cover (just in case)
                self._logger.error(  # pragma: no cover
                    'Could not find time zone: {}: {}'.format(location, e))
                continue  # pragma: no cover

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
        date, _, parsed_query, match, overflow = self._parse_dt(query, now)

        if not any([date, parsed_query, match, overflow]):
            item = TimeCalculation(
                value=now,
                reference_date=now,
                order=0
            )
            return [item]
        elif not match:
            return []
        elif overflow:
            item = TimedeltaCalculation(error=DateOverflowException)
            return [item]

        # Adjust midnights because they refer to same day whereas it should be "tomorrow"
        is_currently_midnight = now.hour | now.minute | now.second | now.microsecond == 0
        if not is_currently_midnight and 'midnight' in parsed_query:
            date += timedelta(days=1)

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
        date_td = timedelta()
        prev = None

        misparsed = False
        parsed_subqueries = query.copy()
        date_overflows = False
        date_add_date_error = False
        reference_dt = datetime.now()

        for i, subquery in enumerate(query):
            if subquery == '+':
                if prev in signs:
                    return []
            elif subquery == '-':
                if prev in signs:
                    return []
            else:
                # TODO: To be removed
                # if prev not in signs:
                #     if not try_again:
                #         return []
                #     new_query = self.keyword + ' at ' + ' '.join(query)
                #     return self.handle_raw(new_query, try_again=False)

                if not TIME_SUBQUERY_REGEX.match(subquery):
                    return []

                date, td, parsed_query, match, overflow = self._parse_dt(
                    subquery, reference_dt)
                if not any([date, parsed_query, match, overflow]):
                    return None
                if parsed_query != subquery:
                    parsed_subqueries[i] = parsed_query
                    misparsed = True
                if overflow:
                    date_overflows = True
                    break
                if prev == '+':
                    date_td += td
                else:
                    date_td -= td
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
            item = TimeCalculation(
                error=DateAddDateException, order=len(items))
            items.append(item)
            return items

        now = datetime.now()
        try:
            date = now + date_td
        except OverflowError:
            date_overflows = True

        if date_overflows:
            item = TimeCalculation(
                error=DateOverflowException, order=len(items))
            items.append(item)
            return items

        locations, added_defaults = self._get_locations(suffix)
        order_offset_locations = len(
            items) + 1 if added_defaults else len(items)
        location_items = (
            self._get_time_location(
                date,
                locations,
                order_offset=order_offset_locations
            )
        )
        order_next = len(items) if added_defaults else len(
            items) + len(location_items)
        items.extend(location_items)

        item = TimeCalculation(
            value=date,
            reference_date=now,
            order=order_next
        )
        items.append(item)
        return items

    def handle_raw(self, query, try_again=True):
        if self._cal is None:
            result = TimeCalculation(
                error=MissingParsedatetimeException,
                order=-1
            )
            return [result]
        query = query.lower()
        query = PLUS_MINUS_REGEX.sub_dict(query)

        query = TIME_QUERY_REGEX_SPLIT.split(query, maxsplit=1)
        if len(query) > 1:
            query, keyword, suffix = map(str.strip, query)
        else:
            query = query[0].strip()
            keyword = ''
            suffix = ''

        if 'til' in keyword and query.strip() == '':
            items = self._get_until(suffix)
        else:
            items = self._calculate(query, suffix, try_again)

        return items

    @QueryHandler.Decorators.can_handle
    def handle(self, query):
        return self.handle_raw(query)
