import locale
from .base import BaseCalculation
from ..query.result import QueryResult
from ..constants import FLAGS

class CurrencyData:
    def __init__(self, converted_amount, rate, date, currency_from, currency_to):
        self.converted_amount = converted_amount
        self.rate = rate
        self.date = date
        self.currency_from = currency_from
        self.currency_to = currency_to

class CurrencyCalculation(BaseCalculation):
    
    @BaseCalculation.Decorators.handle_error_results
    def to_query_result(self):
        converted_amount = self.value.converted_amount
        rate = self.value.rate
        date = self.value.date
        currency_from = self.value.currency_from
        currency_to = self.value.currency_to

        if currency_from == currency_to:
            description = ''
        elif date:
            description = '1 {} = {:f} {} as of {}'.format(currency_from, rate, currency_to, date)
        else:
            description = '1 {} = {:f} {}'.format(currency_from, rate, currency_to)

        if currency_to in FLAGS:
            icon = 'images/flags/{}'.format(FLAGS[currency_to])
        else:
            icon = 'images/currency.svg'
        
        converted_amount = locale.currency(converted_amount, symbol='', grouping=True)
        name = '{} {}'.format(converted_amount, currency_to)
        
        return QueryResult(
            icon=icon,
            name=name,
            description=description,
            clipboard=name,
            value=converted_amount,
            order=self.order
        )
