from datetime import datetime
import json
from json.decoder import JSONDecodeError
from typing import Dict
from urllib.request import urlopen
from urllib.error import HTTPError
from calculate_anything.currency.data import CurrencyData
from calculate_anything.currency.providers import FreeCurrencyProvider
from calculate_anything import logging
from calculate_anything.exceptions import CurrencyProviderException


__all__ = ['MyCurrencyNetCurrencyProvider']


logger = logging.getLogger(__name__)


class MyCurrencyNetCurrencyProvider(FreeCurrencyProvider):
    PROTOCOL = 'https'
    HOSTNAME = 'www.mycurrency.net'
    API_URL = '/US.json'

    def _convert_rates(self, data: Dict) -> CurrencyData:
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
            if 'EUR' in [base_currency, cc]:
                found_eur = True
            if rate['currency_code'] == base_currency:
                found_base = True
            rates_ret[cc] = {'rate': r, 'timestamp_refresh': timestamp}

        if not found_eur or not found_base:
            self.had_error = True
            raise CurrencyProviderException(
                'EUR not base currency or not in rates'
            )

        base_rate = rates_ret['EUR']['rate']
        request_base_rate = rates_ret[base_currency]['rate']
        if base_rate == request_base_rate:
            return rates_ret

        rates_ret = {
            currency: {
                'rate': (
                    rate['rate'] * request_base_rate / base_rate
                    if base_rate
                    else float('inf')
                ),
                'timestamp_refresh': rate['timestamp_refresh'],
            }
            for currency, rate in rates_ret.items()
        }
        return rates_ret

    def request_currencies(
        self, *currencies: str, force: bool = False
    ) -> CurrencyData:
        super().request_currencies(*currencies, force=force)
        try:
            request = self.get_request()
            logger.info('Making request to: {}'.format(request.full_url))
            with urlopen(request) as response:  # nosec
                data = response.read().decode()
                response_code = response.getcode()
        except HTTPError as e:
            response_code = e.code
        except Exception as e:
            msg = 'Could not connect: {}'.format(e)
            logger.exception(msg)
            self.had_error = True
            raise CurrencyProviderException(msg)

        if not str(response_code).startswith('2'):
            self.had_error = True
            msg = 'Response code not 2xx: {}'.format(response_code)
            logger.error(msg)
            raise CurrencyProviderException(msg)

        try:
            data = json.loads(data)
        except JSONDecodeError as e:
            self.had_error = True
            logger.exception('Could not decode json data: {}'.format(e))
            raise CurrencyProviderException('Could not decode json data')

        currencies = self._convert_rates(data)
        return currencies
