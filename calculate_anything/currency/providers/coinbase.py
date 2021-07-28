from datetime import datetime
from urllib.parse import urljoin
try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # pragma: no cover
from calculate_anything.currency.providers import FreeCurrencyProvider
from calculate_anything import logging
from calculate_anything.utils import get_or_default
from calculate_anything.exceptions import CurrencyProviderException


__all__ = ['CoinbaseCurrencyProvider']


class CoinbaseCurrencyProvider(FreeCurrencyProvider):
    BASE_URL = 'https://api.coinbase.com'
    API_URL = '/v2/exchange-rates?currency=EUR'

    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)

    @property
    def url(self):
        cls = CoinbaseCurrencyProvider
        return urljoin(cls.BASE_URL, cls.API_URL)

    def _validate_data(self, data):
        if not isinstance(data, dict):
            raise CurrencyProviderException('Data is not a JSON')

        if 'errors' in data:
            errors = data['errors']
            if not isinstance(errors, dict):
                msg = str(errors)
            else:
                msg = data['errors'].get('message')
            msg = 'Error in response: {}'.format(msg)
            raise CurrencyProviderException(msg)

        try:
            base_currency = data['data']['currency']
            rates = data['data']['rates']
        except KeyError:
            raise CurrencyProviderException('Missing keys from JSON response')

        rates = map(lambda r: (r[0], get_or_default(
            r[1], float, None)), rates.items())
        rates = filter(lambda r: r[1] is not None, rates)

        rates = {currency: rate for currency, rate in rates}

        if base_currency != 'EUR' and ('EUR' not in rates or
                                       base_currency not in rates):
            raise CurrencyProviderException(
                'EUR not base currency or not in rates')

        return base_currency, rates

    def _convert_rates(self, base_currency, rates):

        if base_currency != 'EUR':
            eur_rate = rates['EUR']
            def rate_conv(r): return r / eur_rate
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

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)
        try:
            response = requests.get(self.url)
        except Exception as e:
            self.had_error = True
            msg = 'Could not connect: {}'.format(e)
            self._logger.exception(msg)
            raise CurrencyProviderException(msg)

        if not str(response.status_code).startswith('2'):
            self.had_error = True
            msg = 'Response code not 2xx: {}'.format(response.status_code)
            self._logger.error(msg)
            raise CurrencyProviderException(msg)

        try:
            data = response.json()
        except Exception as e:
            self.had_error = True
            self._logger.exception('Could not decode json data: {}'.format(e))
            raise CurrencyProviderException('Could not decode json data')

        try:
            base_currency, rates = self._validate_data(data)
        except CurrencyProviderException as e:
            self.had_error = True
            self._logger.exception(e)
            raise e

        return self._convert_rates(base_currency, rates)
