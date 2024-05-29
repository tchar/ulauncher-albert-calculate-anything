from typing import Tuple
from urllib.parse import urljoin
from urllib.request import urlopen
from urllib.error import HTTPError
from datetime import datetime

# Look I have taken every measure I can for this.
# If you install a malicious cert and let them mitm
# European Central Bank, that's on you.
from xml.etree import ElementTree  # nosec
from calculate_anything.currency.data import CurrencyData
from calculate_anything.currency.providers import FreeCurrencyProvider
from calculate_anything import logging
from calculate_anything.exceptions import CurrencyProviderException

__all__ = ['ECBCurrencyProvider']


logger = logging.getLogger(__name__)


class ECBCurrencyProvider(FreeCurrencyProvider):
    PROTOCOL = 'https'
    HOSTNAME = 'www.ecb.europa.eu'
    API_URL = '/stats/eurofxref/eurofxref-daily.xml'

    @property
    def url(self):
        cls = ECBCurrencyProvider
        return urljoin(cls.PROTOCOL + '://' + cls.HOSTNAME, cls.API_URL)

    def _validate_data(
        self, data: str
    ) -> Tuple[ElementTree.ElementTree, float]:
        try:
            xml_tree = ElementTree.fromstring(data)  # nosec
        except ElementTree.ParseError as e:
            msg = 'Could not parse ECB xml response: {}'.format(e)
            logger.exception(msg)
            raise CurrencyProviderException(msg)

        try:
            timestamp = xml_tree[2][0].attrib['time']
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d').timestamp()
        except IndexError as e:
            msg = 'XML data not as expected: {}'.format(e)
            logger.exception(msg)
            raise CurrencyProviderException(msg)
        except Exception as e:
            msg = 'Could not read timestamp: {}'.format(e)
            logger.exception(msg)
            timestamp = datetime.now().timestamp()

        return xml_tree, timestamp

    def _convert_data(
        self, xml_tree: ElementTree.Element, timestamp: float
    ) -> CurrencyData:
        currency_data = {'EUR': {'rate': 1.0, 'timestamp_refresh': timestamp}}

        valid_cnt = 0
        all_cnt = 0
        for i, child in enumerate(xml_tree[2][0]):
            try:
                curr = child.attrib['currency']
                rate = float(child.attrib['rate'])
                currency_data[curr] = {
                    'rate': rate,
                    'timestamp_refresh': timestamp,
                }
                valid_cnt += 1
            except Exception as e:
                logger.exception(
                    'Could not read rate for currency at line {}: {}'.format(
                        i, e
                    )
                )
            all_cnt += 1

        if valid_cnt == 0 and all_cnt != 0:
            self.had_error = True
            raise CurrencyProviderException('Could not get any data')

        return currency_data

    @FreeCurrencyProvider.Decorators.with_ratelimit
    def request_currencies(
        self, *currencies: str, force: bool = False
    ) -> CurrencyData:
        try:
            request = self.get_request()
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
            msg = 'Response code not 2xx ({})'.format(response_code)
            logger.error(msg)
            raise CurrencyProviderException(msg)

        try:
            xml_tree, timestamp = self._validate_data(data)
        except CurrencyProviderException as e:
            self.had_error = True
            logger.exception(e)
            raise e

        currency_data = self._convert_data(xml_tree, timestamp)
        self.had_error = False
        return currency_data
