from calculate_anything.utils.datetime import is_leap_year
from calculate_anything.lang import LanguageService
from calculate_anything.calculation.base import _Calculation
from calculate_anything.constants import FLAGS, TIME_DATETIME_FORMAT, TIME_DATE_FORMAT, TIME_TIME_FORMAT
from calculate_anything.query.result import QueryResult


class TimeCalculation(_Calculation):
    def __init__(self, value=None, reference_date=None, query='', error=None, order=0):
        super().__init__(value=value, query=query, error=error, order=order)
        self.reference_date = reference_date

    @_Calculation.Decorators.handle_error_results
    def to_query_result(self):
        translator = LanguageService().get_translator('time')

        now = self.reference_date
        now_week = now.isocalendar()[1]
        date_week = self.value.isocalendar()[1]

        if now == self.value:
            description = translator('now').capitalize()
        elif now.year - 1 == self.value.year:
            description = translator('last-year').capitalize()
        elif now.year + 1 == self.value.year:
            description = translator('next-year').capitalize()
        elif now.year != self.value.year:
            if self.value.year > now.year:
                description = translator('years-from-now')
            else:
                description = translator('years-ago')
            description = '{} {}'.format(
                abs(now.year - self.value.year), description)
        elif now.month - 1 == self.value.month:
            description = translator('last-month').capitalize()
        elif now.month + 1 == self.value.month:
            description = translator('next-month').capitalize()
        elif now.month != self.value.month:
            if self.value.month > now.month:
                description = translator('months-from-now')
            else:
                description = translator('months ago')
            description = '{} {}'.format(
                abs(now.month - self.value.month), description)
        elif now_week - 1 == date_week:
            description = translator('last-week').capitalize()
        elif now_week + 1 == date_week:
            description = translator('next-week').capitalize()
        elif now_week != date_week:
            if date_week > now_week:
                description = translator('weeks-from-now')
            else:
                description = translator('weeks-ago')
            description = '{} {}'.format(
                abs(now_week - date_week), description)
        elif now.day - 1 == self.value.day:
            description = translator('yesterday').capitalize()
        elif now.day + 1 == self.value.day:
            description = translator('tomorrow').capitalize()
        elif now.day != self.value.day:
            if self.value.day > now.day:
                description = translator('days-from-now')
            else:
                description = translator('days-ago')
            description = '{} {}'.format(
                abs(now.day - self.value.day), description)
        else:
            description = translator('today').capitalize()

        value = self.value.strftime(TIME_DATETIME_FORMAT)

        return QueryResult(
            icon='images/time.svg',
            name=value,
            description=description,
            clipboard=value,
            value=self.value,
            order=self.order
        )


class LocationTimeCalculation(TimeCalculation):
    def __init__(self, value=None, location=None, query='', error=None, order=-1):
        super().__init__(value=value, query=query, error=error, order=order)
        self.location = location

    @TimeCalculation.Decorators.handle_error_results
    def to_query_result(self):
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
            location_date, country_name, timezone_name, utc)

        if country_code in FLAGS:
            icon = 'images/flags/{}'.format(FLAGS[country_code])
        else:
            # Can't test this since we possible have all flags, leave it just in case
            icon = 'images/country.svg'  # pragma: no cover

        return QueryResult(
            icon=icon,
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order
        )


class TimedeltaCalculation(TimeCalculation):
    def __init__(self, value=None, reference_date=None, target_date=None, query='', error=None, order=0):
        super().__init__(value=value, reference_date=reference_date,
                         query=query, error=error, order=order)
        self.target_date = target_date

    def _calculate_diff(self):
        target_date = self.target_date
        reference = self.reference_date
        if target_date < reference:
            target_date, reference = reference, target_date
            sign = -1
        else:
            sign = 1

        years_diff = target_date.year - reference.year
        old_value = target_date
        # Check if target date is february 29 before replacing years
        # If not reference is leap year move to March 1st
        if target_date.month == 2 and target_date.day == 29 \
                and not is_leap_year(reference.year):
            value = target_date.replace(year=reference.year, month=3, day=1)
        else:
            value = target_date.replace(year=reference.year)
        if value < reference:
            value = old_value
            years_diff = 0
        date_dt = value - reference
        days_diff = date_dt.days
        hours_diff, remainder = divmod(date_dt.seconds, 3600)
        minutes_diff, seconds_diff = divmod(remainder, 60)
        return sign, years_diff, days_diff, hours_diff, minutes_diff, seconds_diff

    @TimeCalculation.Decorators.handle_error_results
    def to_query_result(self):
        sign, years_diff, days_diff, hours_diff, minutes_diff, seconds_diff = self._calculate_diff()

        translator = LanguageService().get_translator('time')
        names = []
        if years_diff > 0:
            text = 'year' if years_diff == 1 else 'years'
            text = translator(text)
            name = '{} {}'.format(years_diff, text)
            names.append(name)
        if days_diff > 0:
            text = 'day' if days_diff == 1 else 'days'
            text = translator(text)
            name = '{} {}'.format(days_diff, text)
            names.append(name)
        if hours_diff > 0:
            text = 'hour' if hours_diff == 1 else 'hours'
            text = translator(text)
            name = '{} {}'.format(hours_diff, text)
            names.append(name)
        if minutes_diff > 0:
            text = 'minute' if minutes_diff == 1 else 'minutes'
            text = translator(text)
            name = '{} {}'.format(minutes_diff, text)
            names.append(name)
        if seconds_diff > 0:
            text = 'second' if seconds_diff == 1 else 'seconds'
            text = translator(text)
            name = '{} {}'.format(seconds_diff, text)
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
            self.query.capitalize(), is_on, description_date)

        return QueryResult(
            icon='images/time.svg',
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order
        )
