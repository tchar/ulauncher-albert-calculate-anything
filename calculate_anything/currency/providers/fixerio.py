import urllib.parse
try:
    import requests
except ImportError:
    requests = None
from calculate_anything.currency.providers import ApiKeyCurrencyProvider
from calculate_anything.exceptions import CurrencyProviderRequestException
from calculate_anything import logging


__all__ = ['FixerIOCurrencyProvider']


class FixerIOCurrencyProvider(ApiKeyCurrencyProvider):
    BASE_URL = 'http://data.fixer.io/api/'
    PATH_URL = '/latest'

    def __init__(self, api_key=''):
        super().__init__(api_key)
        self._logger = logging.getLogger(__name__)

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)
        url = urllib.parse.urljoin(
            FixerIOCurrencyProvider.BASE_URL, FixerIOCurrencyProvider.PATH_URL)
        params = {'access_key': self._api_key, 'base': 'EUR'}
        if currencies:
            params['symbols'] = ','.join(currencies)

        try:
            response = requests.get(url, params=params)
        except Exception as e:
            self._logger.error('Could not connect to fixer.io: {}'.format(e))
            self.had_error = True
            raise CurrencyProviderRequestException(
                'Could not connect to fixerio')

        if not str(response.status_code).startswith('2'):
            self.had_error = True
            raise CurrencyProviderRequestException(
                'Fixerio response code was {}'.format(response.status_code))

        data = response.json()
        if not data['success']:
            self.had_error = True
            raise CurrencyProviderRequestException(data['error']['info'])

        self.had_error = False
        currency_data = {
            currency: {'rate': data['rates'].get(
                currency, None), 'timestamp_refresh': data['timestamp']}
            for currency in data['rates']
        }
        return currency_data
