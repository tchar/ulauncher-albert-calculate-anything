from datetime import datetime
import json
from json.decoder import JSONDecodeError
from typing import Any, Dict, Tuple
from urllib.parse import urljoin
from urllib.request import urlopen
from urllib.error import HTTPError
from calculate_anything.currency.data import CurrencyData
from calculate_anything.currency.providers import FreeCurrencyProvider
from calculate_anything import logging
from calculate_anything.utils import get_or_default
from calculate_anything.exceptions import CurrencyProviderException


__all__ = ['CoinbaseCurrencyProvider']


logger = logging.getLogger(__name__)


class CoinbaseCurrencyProvider(FreeCurrencyProvider):
    PROTOCOL = 'https'
    HOSTNAME = 'api.coinbase.com'
    API_URL = '/v2/exchange-rates'

    @property
    def url(self) -> str:
        cls = CoinbaseCurrencyProvider
        return urljoin(cls.PROTOCOL + '://' + cls.HOSTNAME, cls.API_URL)

    def _validate_data(self, data: Any) -> Tuple[str, Dict]:
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

        rates = map(
            lambda r: (r[0], get_or_default(r[1], float, None)), rates.items()
        )
        rates = filter(lambda r: r[1] is not None, rates)

        rates = {currency: rate for currency, rate in rates}

        if base_currency != 'EUR' and (
            'EUR' not in rates or base_currency not in rates
        ):
            raise CurrencyProviderException(
                'EUR not base currency or not in rates'
            )

        return base_currency, rates

    def _convert_rates(self, base_currency: str, rates: Dict) -> CurrencyData:

        if base_currency != 'EUR':
            eur_rate = rates['EUR']

            def rate_conv(r):
                return r / eur_rate if eur_rate else float('inf')

        else:

            def rate_conv(r):
                return r

        timestamp = datetime.now().timestamp()
        return {
            currency: {
                'rate': rate_conv(rate) if currency != 'EUR' else 1.0,
                'timestamp_refresh': timestamp,
            }
            for currency, rate in rates.items()
        }

    @FreeCurrencyProvider.Decorators.with_ratelimit
    def request_currencies(
        self, *currencies: str, force: bool = False
    ) -> CurrencyData:
        params = {'currency': 'EUR'}
        try:
            request = self.get_request(params)
            logger.info('Making request to: {}'.format(request.full_url))
            with urlopen(request) as response:  # nosec
                data = response.read().decode()
                response_code = response.getcode()
        except HTTPError as e:
            response_code = e.code
        except Exception as e:
            self.had_error = True
            msg = 'Could not connect: {}'.format(e)
            logger.exception(msg)
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

        try:
            base_currency, rates = self._validate_data(data)
        except CurrencyProviderException as e:
            self.had_error = True
            logger.exception(e)
            raise e

        return self._convert_rates(base_currency, rates)
