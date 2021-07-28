from urllib.parse import urljoin
try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # pragma: no cover
from datetime import datetime
from xml.etree import ElementTree
from calculate_anything.currency.providers import FreeCurrencyProvider
from calculate_anything import logging
from calculate_anything.exceptions import CurrencyProviderException

__all__ = ['ECBCurrencyProvider']


class ECBCurrencyProvider(FreeCurrencyProvider):
    BASE_URL = 'https://www.ecb.europa.eu'
    API_URL = '/stats/eurofxref/eurofxref-daily.xml'

    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)

    @property
    def url(self):
        cls = ECBCurrencyProvider
        return urljoin(cls.BASE_URL, cls.API_URL)

    def _validate_data(self, data):
        try:
            xml_tree = ElementTree.fromstring(data)
        except ElementTree.ParseError as e:
            msg = 'Could not parse ECB xml response: {}'.format(e)
            self._logger.exception(msg)
            raise CurrencyProviderException(msg)

        try:
            timestamp = xml_tree[2][0].attrib['time']
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d').timestamp()
        except IndexError as e:
            msg = 'XML data not as expected: {}'.format(e)
            self._logger.exception(msg)
            raise CurrencyProviderException(msg)
        except Exception as e:
            msg = 'Could not read timestamp: {}'.format(e)
            self._logger.exception(msg)
            timestamp = datetime.now().timestamp()

        return xml_tree, timestamp

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)
        try:
            response = requests.get(self.url)
        except Exception as e:
            self.had_error = True
            msg = 'Could not connect: {}'.format(e)
            self._logger.exception(msg)
            raise CurrencyProviderException(msg)

        if not str(response.status_code).startswith('2'):
            self.had_error = True
            msg = 'Response code not 2xx ({})'.format(response.status_code)
            self._logger.error(msg)
            raise CurrencyProviderException(msg)

        data = response.text

        try:
            xml_tree, timestamp = self._validate_data(data)
        except CurrencyProviderException as e:
            self.had_error = True
            self._logger.exception(e)
            raise e

        currency_data = {'EUR': {'rate': 1.0, 'timestamp_refresh': timestamp}}
        for i, child in enumerate(xml_tree[2][0]):
            try:
                curr = child.attrib['currency']
                rate = float(child.attrib['rate'])
                currency_data[curr] = {'rate': rate,
                                       'timestamp_refresh': timestamp}
            except Exception as e:
                self._logger.exception(
                    'Could not read rate for currency at line {}: {}'
                    .format(i, e))
        self.had_error = False
        return currency_data
