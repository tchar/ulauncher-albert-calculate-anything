from typing import Tuple, Union
from calculate_anything.lang import LanguageService
from calculate_anything.calculation.base import Calculation
from calculate_anything.utils.datetime import is_leap_year
from calculate_anything.utils import images_dir
from calculate_anything.constants import (
    FLAGS,
    TIME_DATETIME_FORMAT,
    TIME_DATE_FORMAT,
    TIME_TIME_FORMAT,
)
from calculate_anything.time.data import CityData
from calculate_anything.query.result import QueryResult
from datetime import datetime, timedelta


__all__ = [
    'TimeCalculation',
    'LocationTimeCalculation',
    'TimedeltaCalculation',
]


class TimeCalculation(Calculation):
    def __init__(
        self,
        value: Union[datetime, timedelta],
        reference_date: datetime,
        query: str,
        order: int = 0,
    ):
        super().__init__(value, query, order)
        self.reference_date = reference_date

    def to_query_result(self) -> QueryResult:
        translator = LanguageService().get_translator('time')

        now = self.reference_date
        now_week = now.isocalendar()[1]
        date_week = self.value.isocalendar()[1]

        if now == self.value:
            description = translator('now').capitalize()
        elif now.year < self.value.year:
            diff = self.value.year - now.year
            description = 'years-from-now' if diff > 1 else 'next-year'
            diff = '{} '.format(diff) if diff > 1 else ''
            description = translator(description)
            description = '{}{}'.format(diff, description)
        elif now.year > self.value.year:
            diff = now.year - self.value.year
            description = 'years-ago' if diff > 1 else 'last-year'
            diff = '{} '.format(diff) if diff > 1 else ''
            description = translator(description)
            description = '{}{}'.format(diff, description)
        elif now.month < self.value.month:
            diff = self.value.month - now.month
            description = 'months-from-now' if diff > 1 else 'next-month'
            diff = '{} '.format(diff) if diff > 1 else ''
            description = translator(description)
            description = '{}{}'.format(diff, description)
        elif now.month > self.value.month:
            diff = now.month - self.value.month
            description = 'months-ago' if diff > 1 else 'last-month'
            diff = '{} '.format(diff) if diff > 1 else ''
            description = translator(description)
            description = '{}{}'.format(diff, description)
        elif now_week < date_week:
            diff = date_week - now_week
            description = 'weeks-from-now' if diff > 1 else 'next-week'
            diff = '{} '.format(diff) if diff > 1 else ''
            description = translator(description)
            description = '{}{}'.format(diff, description)
        elif now_week > date_week:
            diff = now_week - date_week
            description = 'weeks-ago' if diff > 1 else 'last-week'
            diff = '{} '.format(diff) if diff > 1 else ''
            description = translator(description)
            description = '{}{}'.format(diff, description)
        elif now.day < self.value.day:
            diff = self.value.day - now.day
            description = 'days-from-now' if diff > 1 else 'tomorrow'
            diff = '{} '.format(diff) if diff > 1 else ''
            description = translator(description)
            description = '{}{}'.format(diff, description)
        elif now.day > self.value.day:
            diff = now.day - self.value.day
            description = 'days-ago' if diff > 1 else 'yesterday'
            diff = '{} '.format(diff) if diff > 1 else ''
            description = translator(description)
            description = '{}{}'.format(diff, description)
        else:
            description = translator('today').capitalize()

        value = self.value.strftime(TIME_DATETIME_FORMAT)

        return QueryResult(
            icon=images_dir('time.svg'),
            name=value,
            description=description,
            clipboard=value,
            value=self.value,
            order=self.order,
        )


class LocationTimeCalculation(TimeCalculation):
    def __init__(
        self, value: datetime, location: CityData, query: str, order: int = 0
    ):
        super().__init__(value, None, query, order)
        self.location = location

    def to_query_result(self) -> QueryResult:
        timezone_name = self.value.tzname()
        utc = int(self.value.utcoffset().total_seconds() / 60 / 60)
        utc = 'UTC{:+}'.format(utc)

        location_time = self.value.strftime(TIME_TIME_FORMAT)
        location_date = self.value.strftime(TIME_DATE_FORMAT)

        city_name = self.location['name']
        country_name = self.location['country']
        country_code = self.location['cc'].upper()
        if country_code == 'US':
            state_name = self.location['state'].upper()
            country_name = '{} {}'.format(state_name, country_name)

        name = '{}: {}'.format(city_name, location_time)
        description = '{} • {} • {} ({})'.format(
            location_date, country_name, timezone_name, utc
        )

        if country_code in FLAGS:
            icon = FLAGS[country_code]
            icon = images_dir('flags', icon)
        else:
            # Can't test this since we possible have all flags.
            icon = images_dir('country.svg')  # pragma: no cover

        return QueryResult(
            icon=icon,
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )


class TimedeltaCalculation(TimeCalculation):
    def __init__(
        self,
        value: timedelta,
        reference_date: datetime,
        target_date: datetime,
        query: str,
        order: int = 0,
    ) -> None:
        super().__init__(value, reference_date, query, order=order)
        self.target_date = target_date

    def _calculate_diff(self) -> Tuple[int, int, int, int, int, int]:
        target_date = self.target_date
        reference = self.reference_date
        if target_date < reference:
            target_date, reference = reference, target_date
            sign = -1
        else:
            sign = 1

        dyears = target_date.year - reference.year
        old_value = target_date
        # Check if target date is february 29 before replacing years
        # If not reference is leap year move to March 1st
        if (
            target_date.month == 2
            and target_date.day == 29
            and not is_leap_year(reference.year)
        ):
            value = target_date.replace(year=reference.year, month=3, day=1)
        else:
            value = target_date.replace(year=reference.year)
        if value < reference:
            value = old_value
            dyears = 0
        date_dt = value - reference
        ddays = date_dt.days
        dhours, remainder = divmod(date_dt.seconds, 3600)
        dmins, dsecs = divmod(remainder, 60)
        return sign, dyears, ddays, dhours, dmins, dsecs

    def to_query_result(self) -> QueryResult:
        sign, dyears, ddays, dhours, dmins, dsecs = self._calculate_diff()

        translator = LanguageService().get_translator('time')
        names = []
        if dyears > 0:
            text = 'year' if dyears == 1 else 'years'
            text = translator(text)
            name = '{} {}'.format(dyears, text)
            names.append(name)
        if ddays > 0:
            text = 'day' if ddays == 1 else 'days'
            text = translator(text)
            name = '{} {}'.format(ddays, text)
            names.append(name)
        if dhours > 0:
            text = 'hour' if dhours == 1 else 'hours'
            text = translator(text)
            name = '{} {}'.format(dhours, text)
            names.append(name)
        if dmins > 0:
            text = 'minute' if dmins == 1 else 'minutes'
            text = translator(text)
            name = '{} {}'.format(dmins, text)
            names.append(name)
        if dsecs > 0:
            text = 'second' if dsecs == 1 else 'seconds'
            text = translator(text)
            name = '{} {}'.format(dsecs, text)
            names.append(name)

        names = names[:3]
        name = ', '.join(names)
        if sign < 0:
            name = '- {}'.format(name)

        description_date = self.target_date.strftime(TIME_DATETIME_FORMAT)

        if sign > 0:
            is_on = '{} {}'.format(translator('is'), translator('on'))
        else:
            is_on = '{} {}'.format(translator('was'), translator('on'))

        description = '"{}" {} {}'.format(
            self.query.capitalize(), is_on, description_date
        )

        return QueryResult(
            icon=images_dir('time.svg'),
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )
