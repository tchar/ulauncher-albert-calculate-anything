from datetime import datetime
try:
    import requests
except ImportError:
    requests = None
from calculate_anything.currency.providers import FreeCurrencyProvider
from calculate_anything import logging
from calculate_anything.exceptions import CurrencyProviderException, CurrencyProviderRequestException


__all__ = ['MyCurrencyNetCurrencyProvider']


class MyCurrencyNetCurrencyProvider(FreeCurrencyProvider):
    BASE_URL = 'https://www.mycurrency.net/US.json'

    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)

    @staticmethod
    def _convert_rates_to_dict(rates):
        timestamp = datetime.now().timestamp()
        rates_dict = {}
        for rate in rates:
            if 'currency_code' not in rate or 'rate' not in rate:
                continue

            currency_code = rate['currency_code']
            if currency_code == 'EUR':
                rate = 1.0
            else:
                rate = rate['rate']

            rates_dict[currency_code] = {
                'rate': rate,
                'timestamp_refresh': timestamp
            }
        return rates_dict

    @staticmethod
    def _convert_rates(data):
        if 'baseCurrency' not in data or 'rates' not in data:
            raise CurrencyProviderException('Could not get currency data')

        base_currency = data['baseCurrency']
        rates = data['rates']

        if base_currency == 'EUR':
            return MyCurrencyNetCurrencyProvider._convert_rates_to_dict(rates)

        base_rate = None
        request_base_rate = None
        for rate in rates:
            if 'currency_code' not in rate or 'rate' not in rate:
                continue
            if rate['currency_code'] == 'EUR':
                base_rate = rate['rate']
            if rate['currency_code'] == base_currency:
                request_base_rate = rate['rate']
            if base_rate is not None and request_base_rate is not None:
                break
        else:
            raise CurrencyProviderException('Could not find ')

        if base_rate == request_base_rate:
            return MyCurrencyNetCurrencyProvider._convert_rates_to_dict(rates)

        rates = map(
            lambda r: {**r, 'rate': r['rate'] * request_base_rate / base_rate}, rates)
        return MyCurrencyNetCurrencyProvider._convert_rates_to_dict(rates)

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)
        try:
            response = requests.get(MyCurrencyNetCurrencyProvider.BASE_URL)
        except Exception as e:
            self._logger.exception(
                'Could not connect to mycurrency.net: {}'.format(e))
            self.had_error = True
            raise CurrencyProviderRequestException(
                'Could not connect to conversion service')
        if not str(response.status_code).startswith('2'):
            self.had_error = True
            raise CurrencyProviderRequestException(
                'mycurrency.net response code was {}'.format(response.status_code))

        data = response.json()
        currencies = MyCurrencyNetCurrencyProvider._convert_rates(data)
        return currencies
