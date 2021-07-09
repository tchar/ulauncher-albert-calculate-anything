from .fixerio import FixerIOCurrencyProvider 
from ...exceptions import CurrencyProviderException

class ProviderFactory:
    @staticmethod
    def get_provider(provider_name, api_key=''):
        if provider_name == 'fixerio':
            return FixerIOCurrencyProvider(api_key)
        raise CurrencyProviderException('No provider found with name "{}"'.format(provider_name))