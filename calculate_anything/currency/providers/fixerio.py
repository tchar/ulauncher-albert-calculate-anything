import logging
import urllib.parse
import requests
from .interface import CurrencyProvider
from ...exceptions import ProviderRequestException

class FixerIOCurrencyProvider(CurrencyProvider):
    BASE_URL = 'http://data.fixer.io/api/'
    PATH_URL = '/latest'
    
    def __init__(self, api_key=''):
        self._api_key = api_key
        self._logger = logging.getLogger(__name__)

    def set_api_key(self, api_key):
        self._api_key = api_key

    def request_currencies(self, *currencies):
        url = urllib.parse.urljoin(FixerIOCurrencyProvider.BASE_URL, FixerIOCurrencyProvider.PATH_URL)
        params = {'access_key': self._api_key, 'base': 'EUR'}
        if currencies:
            params['symbols'] = ','.join(currencies)

        try:
            result = requests.get(url, params=params)
            data = result.json()
        except Exception as e:
            self._logger.error('Could not connect to fixer.io: {}'.format(e))
            raise ProviderRequestException('Could not connect to conversion service')
        
        if not str(result.status_code).startswith('2'):
            raise ProviderRequestException('Could not connect to conversion service')
        elif not data['success']:
            raise ProviderRequestException(data['error']['info'])
        
        currency_data = {
            currency: {'rate': data['rates'].get(currency, None), 'timestamp_refresh': data['timestamp']}
            for currency in data['rates']
        }
        return currency_data
