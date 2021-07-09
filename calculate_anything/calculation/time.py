from datetime import datetime
from .base import BaseCalculation
from ..lang import Language
from ..constants import FLAGS, TIME_DATETIME_FORMAT, TIME_DATE_FORMAT, TIME_TIME_FORMAT
from ..query.result import QueryResult

class TimeCalculation(BaseCalculation):

    @BaseCalculation.Decorators.handle_error_results
    def to_query_result(self):
        translator = Language().get_translator('time')
                
        now = datetime.now()
        now_week = now.isocalendar()[1]
        date_week = self.value.isocalendar()[1]

        if now.year - 1 == self.value.year:
            description = translator('last-year')
        elif now.year + 1 == self.value.year:
            description = translator('next-year')
        elif now.year != self.value.year:
            if self.value.year > now.year:
                description = translator('years-from-now')
            else:
                description = translator('years-ago')
            description = '{} {}'.format(abs(now.year - self.value.year), description)
        elif now.month - 1 == self.value.month:
            description = translator('last-month')
        elif now.month + 1 == self.value.month:
            description = translator('next-month')
        elif now.month != self.value.month:
            if self.value.month > now.month:
                description = translator('months-from-now')
            else:
                description = translator('months ago')
            description = '{} {}'.format(abs(now.month - self.value.month), description)
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
        elif now.day - 1 == self.value.day:
            description = translator('yesterday')
        elif now.day + 1 == self.value.day:
            description = translator('tomorrow')
        elif now.day != self.value.day:
            if self.value.day > now.day:
                description = translator('days-from-now')
            else:
                description = translator('days-ago')
            description = '{} {}'.format(abs(now.day - self.value.day), description)
        else:
            description = translator('today')

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
    def __init__(self, value=None, location=None, error=None, order=-1):
        super().__init__(value=value, error=error, order=order)
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
        description = '{} - {} - {} ({}) '.format(location_date, country_name, timezone_name, utc)

        if country_code in FLAGS:
            icon = 'images/flags/{}'.format(FLAGS[country_code])
        else:
            icon = 'images/country.svg'

        return QueryResult(
            icon=icon,
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order
        )
