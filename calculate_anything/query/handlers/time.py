import re
import pytz
from datetime import datetime, timedelta
try:
    import parsedatetime
except ImportError:  # pragma: no cover (tested artificially)
    parsedatetime = None  # pragma: no cover
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything.calculation import (
    LocationTimeCalculation, TimeCalculation,
    TimedeltaCalculation
)
from calculate_anything.time import TimezoneService
from calculate_anything.exceptions import (
    MissingParsedatetimeException, DateOverflowException,
    MisparsedDateTimeException
)
from calculate_anything.utils import Singleton, partition, flatten, deduplicate
from calculate_anything.utils.datetime import parsedatetime_str
from calculate_anything import logging
from calculate_anything.constants import (
    TIME_AGO_BEFORE_REGEX, TIME_QUERY_REGEX_SPLIT, TIME_SUBQUERY_REGEX,
    TIME_SPLIT_REGEX, PLUS_MINUS_REGEX,
    TIME_LOCATION_REPLACE_REGEX
)


__all__ = ['TimeQueryHandler']


class TimeQueryHandler(QueryHandler, metaclass=Singleton):

    def __init__(self):
        super().__init__('time')
        self._logger = logging.getLogger(__name__)
        if parsedatetime is not None:
            self._cal = parsedatetime.Calendar(
                version=parsedatetime.VERSION_CONTEXT_STYLE)
        else:
            self._cal = None

    @staticmethod
    def now():
        return datetime.now().replace(microsecond=0)

    def _parse_dt(self, query, reference_datetime):
        try:
            date = self._cal.nlp(query, sourceTime=reference_datetime)
        except Exception as e:  # pragma: no cover (catching unexpected exception)
            self._logger.exception(  # pragma: no cover
                'Got unexpected exception when parsing datetime: '
                '{} with reference time {}: {}'
                .format(query, reference_datetime, e))
            return None, None, None, None, False  # pragma: no cover

        if date is None:
            return None, None, None, None, False

        date, flags, _, _, parsed_query = date[0]
        match = re.match(r'^\s*\d+\.?(\d+)?\s*$', parsed_query) is None
        overflow = flags == parsedatetime.pdtContext(0) and match
        td = date - reference_datetime
        return date, td, parsed_query, match, overflow

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
            return TimezoneService().default_cities, True

        locations = TimeQueryHandler._get_location_search_combinations(
            location)

        for location, search_terms in locations:
            found_locations = TimezoneService().get(location, *search_terms)
            if found_locations:
                return found_locations, False

        return [], True

    def _get_time_location(self, date, locations, parsed_query, order_offset=0):
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
                query=parsed_query,
                order=order+order_offset
            )
            items.append(item)
            order += 1
        return items

    def _get_until(self, keyword, query):
        now = TimeQueryHandler.now()
        if query.strip() == '':
            date, parsed_query, match, overflow = now, '', True, False
            no_query = True
        else:
            date, _, parsed_query, match, overflow = self._parse_dt(query, now)
            no_query = False

        if parsed_query:
            parsed_query_kw = '{} {}'.format(keyword, parsed_query)
        else:
            parsed_query_kw = keyword

        if not any([date, parsed_query, match, overflow]) or not match:
            original_query_kw_kw = '{} {} {}'.format(
                self.keyword, keyword, query)
            parsed_query_kw_kw = '{} {}'.format(self.keyword, keyword)

            item1 = TimedeltaCalculation(
                query=keyword,
                error=MisparsedDateTimeException(
                    message='Could not fully parse',
                    extra={
                        'original_query': original_query_kw_kw,
                        'parsed_query': parsed_query_kw_kw
                    }
                ),
                order=-80
            )
            item2 = TimeCalculation(
                value=now,
                reference_date=now,
                query=keyword,
                order=0
            )
            return [item1, item2]
        elif overflow:
            item = TimedeltaCalculation(
                query=parsed_query_kw,
                error=DateOverflowException,
                order=-50
            )
            return [item]

        # Adjust midnights because they refer to same day whereas it should be "tomorrow"
        is_currently_midnight = now.hour | now.minute | now.second | now.microsecond == 0
        if not is_currently_midnight and 'midnight' in parsed_query:
            date += timedelta(days=1)

        items_pre = []
        items = []
        if parsed_query != query:
            original_query_kw_kw = '{} {} {}'.format(
                self.keyword, keyword, query)
            parsed_query_kw_kw = '{} {} {}'.format(
                self.keyword, keyword, parsed_query)
            item = TimedeltaCalculation(
                query=parsed_query_kw,
                error=MisparsedDateTimeException(
                    message='Could not fully parse',
                    extra={
                        'original_query': original_query_kw_kw,
                        'parsed_query': parsed_query_kw_kw,
                    }
                ),
                order=-80
            )
            items_pre.append(item)

        if not no_query:
            items.append(
                TimedeltaCalculation(
                    value=date - now,
                    reference_date=now,
                    target_date=date,
                    query=parsed_query_kw,
                    order=len(items)
                )
            )
        items.append(TimeCalculation(
            value=now,
            query=parsed_query_kw,
            reference_date=now,
            order=len(items)
        ))
        return items_pre + items

    def _calculate(self, query, keyword, suffix):
        original_query = query
        query = PLUS_MINUS_REGEX.sub_dict(query)
        query = TIME_SPLIT_REGEX.split(query)
        query = map(str.strip, query)
        query = filter(None, query)
        query = list(query)

        signs_set = set(['+', '-', 'before', 'ago'])
        dates = []
        signs = []
        prev = None

        misparsed = False
        parsed_subqueries = query.copy()
        date_overflows = False
        now = TimeQueryHandler.now()

        for i, subquery in enumerate(query):
            if subquery in signs_set:
                if prev in signs_set:
                    return []
            elif not TIME_SUBQUERY_REGEX.match(subquery):
                return []
            else:
                sign = prev
                virtual_subquery, n = TIME_AGO_BEFORE_REGEX.subn(' ', subquery)
                if n:
                    sign = '-'
                virtual_subquery = virtual_subquery.strip()

                date, _, parsed_query, match, overflow = self._parse_dt(
                    virtual_subquery, now)
                if not any([date, parsed_query, match, overflow]):
                    return None

                if parsed_query != virtual_subquery.rstrip():
                    parsed_subqueries[i] = parsed_query
                    misparsed = True
                if overflow:
                    date_overflows = True
                    break
                if match:
                    dates.append(date)
                    signs.append(sign)
            prev = subquery

        parsed_query_calc = ' '.join(parsed_subqueries)
        parsed_query_locs = parsed_query_calc
        if keyword:
            if parsed_query_locs:
                parsed_query_locs = '{} {} {}'.format(
                    parsed_query_locs, keyword, suffix)
            else:
                parsed_query_locs = '{} {}'.format(keyword, suffix)

        items_pre = []
        items = []
        if misparsed:
            original_query_kw = '{} {}'.format(self.keyword, ' '.join(query))
            parsed_query_kw = '{} {}'.format(self.keyword, parsed_query_calc)
            item = TimeCalculation(
                query=parsed_query_calc,
                error=MisparsedDateTimeException(
                    'Could not fully parse',
                    extra={
                        'original_query': original_query_kw,
                        'parsed_query': parsed_query_kw
                    }
                ),
                order=-80
            )
            items_pre.append(item)

        signs = list(1 if s == '+' else -1 for s in signs)
        query_str = parsedatetime_str(now, dates, signs).strip()
        if date_overflows:
            pass
        elif not query_str and original_query.strip() != '':
            return items_pre + items
        elif not query_str:
            date = now
        else:
            date = self._cal.nlp(query_str, sourceTime=now)
            if date is None:
                self._logger.error(  # pragma: no cover (Should not enter, here, logging just in case)
                    'Something went wrong when trying to calculate '
                    'date from date chunks: dates={}, query={}'.format(dates, query_str))
                return items_pre + items  # pragma: no cover
            date, context, _, _, _ = date[0]
            if context == parsedatetime.pdtContext(0):
                date_overflows = True

        if date_overflows:
            item = TimeCalculation(
                query=parsed_query_calc,
                error=DateOverflowException,
                order=-50
            )
            items_pre.append(item)
            return items_pre + items

        locations, added_defaults = self._get_locations(suffix)
        order_offset_locations = len(
            items) + 1 if added_defaults else len(items)
        location_items = (
            self._get_time_location(
                date,
                locations,
                parsed_query_locs,
                order_offset=order_offset_locations
            )
        )
        order_next = len(items) if added_defaults else len(
            items) + len(location_items)
        items.extend(location_items)

        item = TimeCalculation(
            value=date,
            reference_date=now,
            query=parsed_query_calc,
            order=order_next
        )
        items.append(item)
        return items_pre + items

    def handle_raw(self, query):
        if self._cal is None:
            result = TimeCalculation(
                error=MissingParsedatetimeException,
                order=-1000
            )
            return [result]

        query = TIME_QUERY_REGEX_SPLIT.split(query, maxsplit=1)
        if len(query) > 1:
            query, keyword, suffix = map(str.strip, query)
        else:
            query = query[0].strip()
            keyword = ''
            suffix = ''

        if 'til' in keyword.lower() and query.strip() == '':
            items = self._get_until(keyword, suffix)
        else:
            items = self._calculate(query, keyword, suffix)

        return items

    @QueryHandler.Decorators.can_handle
    def handle(self, query):
        return self.handle_raw(query)
