from contextlib import contextmanager
from datetime import datetime
from queue import Queue
import pytest
from pytest_httpserver.httpserver import HTTPServer, Response
from calculate_anything.units import UnitsService
from calculate_anything.currency import CurrencyService
from calculate_anything.currency.providers import (
    CoinbaseCurrencyProvider, ECBCurrencyProvider,
    MyCurrencyNetCurrencyProvider, FixerIOCurrencyProvider
)
from calculate_anything.currency.providers.base import ApiKeyCurrencyProvider
from test.tutils import osremove, random_str, currency_data, temp_filepath


@pytest.fixture(scope='session')
def log_filepath():
    rand_name = random_str(5)
    rand_name = 'pytest-calculate-anything-{}.log'.format(rand_name)
    rand_filepath = temp_filepath(rand_name)
    yield rand_filepath
    osremove(rand_filepath)


@pytest.fixture(scope='function')
def httpserver_listen_address():
    return ('localhost', 31137)


@pytest.fixture(scope='function')
def coinbase_data():
    def _coinbase_data(base_currency, rates):
        return {
            'data': {
                'currency': base_currency,
                'rates': rates
            }
        }
    return _coinbase_data


@pytest.fixture(scope='function')
def fixerio_data():
    def _fixerio_data(base_currency, rates, timestamp):
        return {
            'success': True,
            'timestamp': timestamp,
            'base': base_currency,
            'rates': rates
        }
    return _fixerio_data


@pytest.fixture(scope='function')
def mycurrencynet_data():
    def _mycurrencynet_data(base_currency, rates):
        return {
            'baseCurrency': base_currency,
            'rates': rates
        }
    return _mycurrencynet_data


@pytest.fixture(scope='function')
def ecb_data():
    def _ecb_data(rates, time=datetime.today().strftime('%Y-%m-%d')):
        rates = ((k, v) for k, v in rates.items() if k != 'EUR')
        rates = [
            '<Cube currency="{}" rate="{}"/>'.format(c, r)
            for c, r in rates
        ]
        rates = '\n'.join(rates)

        return '''
        <gesmes:Envelope xmlns:gesmes="http://www.gesmes.org/xml/2002-08-01"
            xmlns="http://www.ecb.int/vocabulary/2002-08-01/eurofxref">
            <gesmes:subject>Reference rates</gesmes:subject>
        <gesmes:Sender>
            <gesmes:name>European Central Bank</gesmes:name>
        </gesmes:Sender>
        <Cube>
            <Cube time="{}">
                {}
            </Cube>
        </Cube>
        </gesmes:Envelope>
        '''.format(time, rates)
    return _ecb_data


@pytest.fixture(scope='function')
def mock_currency_provider(httpserver: HTTPServer):
    def store_data(klasses, api_key):
        instances = []
        storage = {}
        for klass in klasses:
            instance = klass()
            if isinstance(instance, ApiKeyCurrencyProvider):
                instance.set_api_key(api_key)
            instances.append(instance)
            storage[klass] = {
                'instance': instance,
                'url': klass.BASE_URL
            }
        return storage

    def restore_data(klasses):
        for klass, info in klasses.items():
            klass.BASE_URL = info['url']

    def _handle_no_response(klasses):
        base_url = 'http://localhost:1234/{}.{}'.format(
            random_str(100), random_str(5))

        instances = []
        for klass in klasses:
            klass.BASE_URL = base_url
            instances.append(klasses[klass]['instance'])
        if len(instances) == 1:
            return instances[0]
        else:
            return instances

    def _handle_response(klasses, data, status, use_json):
        if isinstance(use_json, bool):
            use_json = [use_json] * len(klasses)
        if not isinstance(data, (list, tuple)):
            data = [data] * len(klasses)
        instances = []
        for klass, data, use_json in zip(klasses, data, use_json):
            api_url = klass.API_URL
            base_url = httpserver.url_for(klasses[klass]['url'])
            klass.BASE_URL = base_url
            request = httpserver.expect_request(api_url)
            if status != 200:
                request.respond_with_response(Response(data, status=status))
            elif use_json:
                request.respond_with_json(data)
            else:
                request.respond_with_data(data)
            instances.append(klasses[klass]['instance'])
        if len(instances) == 1:
            return instances[0]
        else:
            return instances

    @contextmanager
    def _mock_currency_provider(klasses, data,
                                use_json, status=200,
                                respond=True,
                                api_key='mockey'):
        if not isinstance(klasses, (list, tuple)):
            klasses = [klasses]
        klasses = store_data(klasses, api_key)
        if not respond:
            yield _handle_no_response(klasses)
        else:
            yield _handle_response(klasses, data, status, use_json)
        restore_data(klasses)
    return _mock_currency_provider


_mock_currency_service_data = {}


@pytest.fixture(scope='function')
def mock_currency_service(mock_currency_provider, coinbase_data,
                          mycurrencynet_data, fixerio_data, ecb_data):

    @contextmanager
    def _mock_currency_service(error=False):
        if error in _mock_currency_service_data:
            yield _mock_currency_service_data[error]
            return

        coindata = coinbase_data('EUR', currency_data('EUR')['rates'])

        timestamp = datetime.now().timestamp()
        rates = currency_data()['rates']
        fixerdata = fixerio_data('EUR', rates, timestamp)

        rates = [
            {'currency_code': k, 'rate': v}
            for k, v in currency_data()['rates'].items()
        ]
        mycurrdata = mycurrencynet_data('EUR', rates)

        rates = currency_data()['rates']
        ecbdata = ecb_data(rates)

        klasses = [CoinbaseCurrencyProvider, FixerIOCurrencyProvider,
                   MyCurrencyNetCurrencyProvider, ECBCurrencyProvider]
        data = [coindata, fixerdata, mycurrdata, ecbdata]
        use_json = [True, True, True, False]
        if error:
            status = 500
        else:
            status = 200

        data_queue = Queue()

        def callback(data):
            data_queue.put_nowait(data)

        with mock_currency_provider(klasses, data, use_json, status=status):
            UnitsService().start(force=True)
            CurrencyService().remove_update_callback(callback)
            CurrencyService().add_update_callback(callback)
            CurrencyService().start(force=True)
            data = data_queue.get(block=True, timeout=None)
            yield data
            _mock_currency_service_data[error] = data
    return _mock_currency_service
