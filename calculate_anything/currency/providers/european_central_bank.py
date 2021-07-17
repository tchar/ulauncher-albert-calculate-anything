try:
    import requests
except ImportError:
    requests = None
from datetime import datetime
from xml.etree import ElementTree
from . import CurrencyProvider
from ... import logging
from ...exceptions import CurrencyProviderRequestException

class ECBProvider(CurrencyProvider):
    BASE_URL = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)

    @property
    def api_key_valid(self):
        return True

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)
        try:
            result = requests.get(ECBProvider.BASE_URL)
            # data = result.json()
            data = result.text
        except Exception as e:
            self._logger.error('Could not connect to European Central Bank: {}'.format(e))
            self.had_error = True
            raise CurrencyProviderRequestException('Could not connect to conversion service')
        
        if not str(result.status_code).startswith('2'):
            self.had_error = True
            raise CurrencyProviderRequestException('Could not connect to conversion service')
        
        try:
            tree = ElementTree.fromstring(data)
            timestamp = tree[2][0].attrib['time']
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d').timestamp()
        except (IndexError, KeyError) as e:
            self._logger.error('Could not read update timestamp: {}'.format(e))
            timestamp = datetime.now().timestamp()
        except Exception as e:
            self._logger.error('An unexpected exception occured when reading update timestamp: {}'.format(e))
            timestamp = datetime.now().timestamp()

        try:
            tree[2][0]
        except IndexError as e:
            self._logger.error('Could not read currencies: {}'.format(e))
            raise CurrencyProviderRequestException(e)
        except Exception as e:
            self._logger.error('An unexpected exception occured when reading currencies: {}'.format(e))
            raise CurrencyProviderRequestException(e)

        currency_data = {}
        for i, child in enumerate(tree[2][0]):
            try:
                curr = child.attrib['currency']
                rate = float(child.attrib['rate'])
                currency_data[curr] = {'rate': rate, 'timestamp_refresh': timestamp}
            except (TypeError, ValueError):
                self._logger.error('Could not read rate for currency at line {}: {}'.format(i, e))
            except Exception as e:
                self._logger.error('An unexpected exception occured when reading rate for currency at line {}: {}'.format(i, e))

        self.had_error = False
        return currency_data