import locale
from .base import BaseCalculation
from ..query.result import QueryResult
from ..constants import FLAGS

class CurrencyCalculation(BaseCalculation):
    def __init__(self, value=None, error=None, order=0, rate=None, date=None, currency_from=None, currency_to=None):
        super().__init__(value=value, error=error, order=order)
        self.rate = rate
        self.date = date
        self.currency_from = currency_from
        self.currency_to = currency_to

    @BaseCalculation.Decorators.handle_error_results
    def to_query_result(self):
        converted_amount = self.value
        rate = self.rate
        date = self.date
        currency_from = self.currency_from
        currency_to = self.currency_to

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
