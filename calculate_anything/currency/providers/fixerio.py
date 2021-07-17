import urllib.parse
try:
    import requests
except ImportError:
    requests = None
from .provider import CurrencyProvider
from ...exceptions import CurrencyProviderRequestException, MissingRequestsException
from ... import logging

class FixerIOCurrencyProvider(CurrencyProvider):
    BASE_URL = 'http://data.fixer.io/api/'
    PATH_URL = '/latest'
    
    def __init__(self, api_key=''):
        super().__init__(api_key)
        self._logger = logging.getLogger(__name__)

    def request_currencies(self, *currencies, force=False):
        if requests is None:
            raise MissingRequestsException('requests is not installed')
        super().request_currencies(*currencies, force=force)
        url = urllib.parse.urljoin(FixerIOCurrencyProvider.BASE_URL, FixerIOCurrencyProvider.PATH_URL)
        params = {'access_key': self._api_key, 'base': 'EUR'}
        if currencies:
            params['symbols'] = ','.join(currencies)

        try:
            result = requests.get(url, params=params)
            data = result.json()
        except Exception as e:
            self._logger.error('Could not connect to fixer.io: {}'.format(e))
            self.had_error = True
            raise CurrencyProviderRequestException('Could not connect to conversion service')
        
        if not str(result.status_code).startswith('2'):
            self.had_error = True
            raise CurrencyProviderRequestException('Could not connect to conversion service')
        elif not data['success']:
            self.had_error = True
            raise CurrencyProviderRequestException(data['error']['info'])
        
        self.had_error = False
        currency_data = {
            currency: {'rate': data['rates'].get(currency, None), 'timestamp_refresh': data['timestamp']}
            for currency in data['rates']
        }
        return currency_data
