from datetime import datetime
from urllib.parse import urljoin
try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # pragma: no cover
from calculate_anything.currency.providers import FreeCurrencyProvider
from calculate_anything import logging
from calculate_anything.exceptions import CurrencyProviderException


__all__ = ['MyCurrencyNetCurrencyProvider']


class MyCurrencyNetCurrencyProvider(FreeCurrencyProvider):
    BASE_URL = 'https://www.mycurrency.net'
    API_URL = '/US.json'

    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)

    @property
    def url(self):
        cls = MyCurrencyNetCurrencyProvider
        return urljoin(cls.BASE_URL, cls.API_URL)

    def _convert_rates(self, data):
        try:
            base_currency = data['baseCurrency']
            rates = data['rates']
        except TypeError:
            self.had_error = True
            raise CurrencyProviderException('Data is not a JSON')
        except KeyError:
            self.had_error = True
            raise CurrencyProviderException('Missing keys from JSON response')

        timestamp = datetime.now().timestamp()
        rates_ret = {}
        found_eur = False
        found_base = False
        for rate in rates:
            if 'rate' not in rate or 'currency_code' not in rate:
                continue
            r = rate['rate']
            cc = rate['currency_code']
            if base_currency == 'EUR':
                found_eur = True
            if cc == 'EUR':
                found_eur = True
            if rate['currency_code'] == base_currency:
                found_base = True
            rates_ret[cc] = {'rate': r, 'timestamp_refresh': timestamp}

        if not found_eur or not found_base:
            self.had_error = True
            raise CurrencyProviderException(
                'EUR not base currency or not in rates')

        base_rate = rates_ret['EUR']['rate']
        request_base_rate = rates_ret[base_currency]['rate']
        if base_rate == request_base_rate:
            return rates_ret

        rates_ret = {
            currency: {
                'rate': rate['rate'] * request_base_rate / base_rate,
                'timestamp_refresh': rate['timestamp_refresh']
            }
            for currency, rate in rates_ret.items()
        }
        return rates_ret

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)
        try:
            response = requests.get(self.url)
        except Exception as e:
            msg = 'Could not connect: {}'.format(e)
            self._logger.exception(msg)
            self.had_error = True
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
            raise CurrencyProviderException(
                'Could not decode json data')

        currencies = self._convert_rates(data)
        return currencies
