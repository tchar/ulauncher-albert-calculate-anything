from datetime import datetime
try:
    import requests
except ImportError:
    requests = None
from calculate_anything.currency.providers.provider import FreeCurrencyProvider
from calculate_anything.logging_wrapper import LoggingWrapper as logging
from calculate_anything.utils import get_or_default
from calculate_anything.exceptions import CurrencyProviderException, CurrencyProviderRequestException


class CoinbaseCurrencyProvider(FreeCurrencyProvider):
    BASE_URL = 'https://api.coinbase.com/v2/exchange-rates?currency=EUR'

    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)

    def request_currencies(self, *currencies, force=False):
        try:
            response = requests.get(CoinbaseCurrencyProvider.BASE_URL)
        except Exception as e:
            self._logger.error(
                'Could not connect to mycurrency.net: {}'.format(e))

        if not str(response.status_code).startswith('2'):
            self.had_error = True
            raise CurrencyProviderRequestException(
                'Coinbase response code was {}'.format(response.status_code))

        data = response.json()
        if 'errors' in data:
            message = data['errors'].get(
                'message', 'Could not connect to coinbase')
            raise CurrencyProviderRequestException(message)

        base_currency = data['data']['currency']
        rates = data['data']['rates']

        rates = map(lambda r: (r[0], get_or_default(
            r[1], float, None)), rates.items())
        rates = filter(lambda r: r[1] is not None, rates)

        rates = {currency: rate for currency, rate in rates}

        if base_currency != 'EUR' and ('EUR' not in rates or base_currency not in rates):
            raise CurrencyProviderException(
                'Could not convert to base currency')

        if base_currency != 'EUR':
            base_rate = rates['EUR']
            request_base_rate = rates[base_currency]
            def rate_conv(r): return r * request_base_rate / base_rate
        else:
            def rate_conv(r): return r

        timestamp = datetime.now().timestamp()
        return {
            currency: {
                'rate': rate_conv(rate) if currency != 'EUR' else 1.0,
                'timestamp_refresh': timestamp
            }
            for currency, rate in rates.items()
        }
