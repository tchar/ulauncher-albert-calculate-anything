from calculate_anything.currency.providers.european_central_bank import ECBProvider
from .fixerio import FixerIOCurrencyProvider 
from ...exceptions import CurrencyProviderException

class CurrencyProviderFactory:
    @staticmethod
    def get_provider(provider_name, api_key=''):
        if provider_name == 'fixerio':
            return FixerIOCurrencyProvider(api_key)
        if provider_name == 'ecb':
            return ECBProvider()
        raise CurrencyProviderException('No provider found with name "{}"'.format(provider_name))