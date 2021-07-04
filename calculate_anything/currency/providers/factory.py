from .fixerio import FixerIOCurrencyProvider 
from ...exceptions import ProviderException

class ProviderFactory:
    @staticmethod
    def get_provider(provider_name, api_key=''):
        if provider_name == 'fixerio':
            return FixerIOCurrencyProvider(api_key)
        raise ProviderException('No provider found with name "{}"'.format(provider_name))