from calculate_anything.calculation.currency import CurrencyData
from calculate_anything.exceptions import CurrencyProviderException, MissingRequestsException
from datetime import datetime
from .interface import QueryHandler
from ...currency.service import CurrencyService
from ...calculation import CurrencyCalculation
from ...lang import Language
from ...utils import Singleton
from ...constants import CURRENCY_QUERY_REGEX, CURRENCY_REGEX, CURRENCY_QUERY_DEFAULT_REGEX, EMPTY_AMOUNT, FLAGS

class CurrencyQueryHandler(QueryHandler, metaclass=Singleton):
    def _extract_query(self, query):

        matches = CURRENCY_QUERY_REGEX.findall(query)
        if not matches:
            matches_default = CURRENCY_QUERY_DEFAULT_REGEX.findall(query)
        else:
            matches_default = None

        if not matches and not matches_default:
            return

        service = CurrencyService()
        if matches_default and not matches and not service.cache_enabled:
            return None

        translator = Language().get_translator('currency')

        if matches:
            amount, currency_from, currencies_to = matches[0]
            currencies_to = currencies_to.split(',')
        else:
            amount, currency_from = matches_default[0]
            currencies_to = service.default_currencies
        
        amount = 1.0 if EMPTY_AMOUNT.match(amount) else float(amount)
        currency_from = translator(currency_from.strip()).upper()
        currencies_to = map(str.strip, currencies_to)
        currencies_to = map(translator, currencies_to)
        currencies_to = map(str.upper, currencies_to)
        currencies_to = filter(lambda c: CURRENCY_REGEX.match(c), currencies_to)
        currencies_to = list(dict.fromkeys(currencies_to))

        return amount, currency_from, currencies_to

    def handle(self, query, return_raw=False):
        query = self._extract_query(query)
        if not query:
            return
        
        amount, currency_from, currencies_to = query

        if len(currencies_to) == 0 or currency_from.strip() == '':
            return

        service = CurrencyService()
        try:
            rates = service.get_rates(currency_from, *currencies_to)
        except MissingRequestsException:
            result = CurrencyCalculation(error=MissingRequestsException, order=-1)
            return [result] if return_raw else [result.to_query_result()]

        if service.provider_had_error:
            result = CurrencyCalculation(error=CurrencyProviderException, order=-1)
            return [result] if return_raw else [result.to_query_result()]
        
        if currency_from not in rates:
            return

        currency_from_rate = rates[currency_from]['rate']

        items = []
        for currency_to in currencies_to:
            if currency_to not in rates:
                continue
            rate_data = rates[currency_to]
            rate = rate_data['rate'] / currency_from_rate
            converted_amount = amount * rate
            date = datetime.fromtimestamp(rate_data['timestamp_refresh']) if rate_data['timestamp_refresh'] else None
            item = CurrencyCalculation(
                value=CurrencyData(
                    converted_amount=converted_amount,
                    rate=rate,
                    date=date,
                    currency_from=currency_from,
                    currency_to=currency_to,
                ),
                order=len(items)
            )
            if not return_raw:
                item = item.to_query_result()
            items.append(item)
        return items
