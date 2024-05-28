from calculate_anything.currency.cache import CurrencyCache
from contextlib import contextmanager
from datetime import datetime
from queue import Queue
from urllib.parse import urljoin, urlparse
import trustme
import ssl
import pytest
from pytest_httpserver.httpserver import HTTPServer, Response
from calculate_anything.units import UnitsService
from calculate_anything.currency import CurrencyService
from calculate_anything.currency.providers import (
    CoinbaseCurrencyProvider,
    ECBCurrencyProvider,
    MyCurrencyNetCurrencyProvider,
    FixerIOCurrencyProvider,
)
from calculate_anything.currency.providers.base import (
    CurrencyProvider,
    ApiKeyCurrencyProvider,
)
from test.tutils import osremove, random_str, currency_data, temp_filepath


SERVER = 'localhost'
PORT = 31137
CERT_ISSUE = 'tchar.calculate-anything.com'


@pytest.fixture(scope='session')
def log_filepath():
    rand_name = random_str(5)
    rand_name = 'pytest-calculate-anything-{}.log'.format(rand_name)
    rand_filepath = temp_filepath(rand_name)
    yield rand_filepath
    osremove(rand_filepath)


@pytest.fixture(scope='session')
def httpserver_listen_address():
    return (SERVER, PORT)


@pytest.fixture(scope='session')
def httpserver_ssl_context():
    ca = trustme.CA()
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_cert = ca.issue_cert(CERT_ISSUE)
    server_cert = ca.issue_cert(SERVER)
    ca.configure_trust(client_context)
    server_cert.configure_cert(server_context)

    def default_context():
        return client_context

    ssl._create_default_https_context = default_context

    return server_context


@pytest.fixture(scope='function')
def coinbase_data():
    def _coinbase_data(base_currency, rates):
        return {'data': {'currency': base_currency, 'rates': rates}}

    return _coinbase_data


@pytest.fixture(scope='function')
def fixerio_data():
    def _fixerio_data(base_currency, rates, timestamp):
        return {
            'success': True,
            'timestamp': timestamp,
            'base': base_currency,
            'rates': rates,
        }

    return _fixerio_data


@pytest.fixture(scope='function')
def mycurrencynet_data():
    def _mycurrencynet_data(base_currency, rates):
        return {'baseCurrency': base_currency, 'rates': rates}

    return _mycurrencynet_data


@pytest.fixture(scope='function')
def ecb_data():
    def _ecb_data(rates, time=datetime.today().strftime('%Y-%m-%d')):
        rates = ((k, v) for k, v in rates.items() if k != 'EUR')
        rates = [
            '<Cube currency="{}" rate="{}"/>'.format(c, r) for c, r in rates
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
        '''.format(
            time, rates
        )

    return _ecb_data


@pytest.fixture(scope='function')
def mock_currency_provider(httpserver: HTTPServer):
    def store_data(klasses, api_key):
        instances = []
        storage = {}
        for klass in klasses:
            instance = klass()
            if isinstance(instance, ApiKeyCurrencyProvider):
                instance.api_key = api_key
            instances.append(instance)
            storage[klass] = {
                'instance': instance,
                'protocol': klass.PROTOCOL,
                'hostname': klass.HOSTNAME,
                'api_url': klass.API_URL,
            }
        return storage

    def restore_data(klasses: CurrencyProvider):
        for klass, info in klasses.items():
            klass.PROTOCOL = info['protocol']
            klass.HOSTNAME = info['hostname']
            klass.API_URL = info['api_url']

    def _handle_no_response(klasses):
        path = random_str(100)
        tld = random_str(5)
        hostname = '{}:{}'.format(SERVER, PORT + 1)
        api_url = '{}.{}'.format(path, tld)

        instances = []
        for klass in klasses:
            klass.PROTOCOL = 'https'
            klass.HOSTNAME = hostname
            klass.API_URL = api_url
            instances.append(klasses[klass]['instance'])
        if len(instances) == 1:
            return instances[0]
        return instances

    def _handle_response(klasses, datas, status, use_jsons):
        if isinstance(use_jsons, bool):
            use_jsons = [use_jsons] * len(klasses)
        if not isinstance(datas, (list, tuple)):
            datas = [datas] * len(klasses)
        instances = []
        for klass, data, use_json in zip(klasses, datas, use_jsons):
            api_url = urljoin('/', klass.__name__)
            klass.API_URL = api_url
            parsed_url = urlparse(httpserver.url_for(klass.__name__))
            klass.PROTOCOL = parsed_url.scheme
            klass.HOSTNAME = parsed_url.netloc
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
        return instances

    @contextmanager
    def _mock_currency_provider(
        klasses, data, use_json, status=200, respond=True, api_key='mockey'
    ):
        if not isinstance(klasses, (list, tuple)):
            klasses = [klasses]
        klasses = store_data(klasses, api_key)
        if not respond:
            yield _handle_no_response(klasses)
        else:
            yield _handle_response(klasses, data, status, use_json)
        restore_data(klasses)

    return _mock_currency_provider


@pytest.fixture(scope='function')
def in_memory_cache():
    @contextmanager
    def _in_memory_cache():
        old_cache = CurrencyService()._cache
        new_cache = CurrencyCache()
        new_cache._use_only_memory = True
        CurrencyService()._cache = new_cache
        if CurrencyService()._thread is not None:
            CurrencyService()._thread._cache = new_cache
        yield
        if CurrencyService()._thread is not None:
            CurrencyService()._thread._cache = old_cache
        CurrencyService()._cache = old_cache

    return _in_memory_cache


_mock_currency_service_data = {}


@pytest.fixture(scope='function')
def mock_currency_service(
    mock_currency_provider,
    coinbase_data,
    mycurrencynet_data,
    fixerio_data,
    ecb_data,
    in_memory_cache,
):
    def callback(queue: Queue):
        def _callback(data, _):
            queue.put_nowait(data)

        return _callback

    @contextmanager
    def uncached_data(rates, error):
        coindata = coinbase_data('EUR', rates)

        timestamp = datetime.now().timestamp()
        fixerdata = fixerio_data('EUR', rates, timestamp)

        mycurrdata = mycurrencynet_data(
            'EUR', [{'currency_code': k, 'rate': v} for k, v in rates.items()]
        )

        ecbdata = ecb_data(rates)

        klasses = [
            CoinbaseCurrencyProvider,
            FixerIOCurrencyProvider,
            MyCurrencyNetCurrencyProvider,
            ECBCurrencyProvider,
        ]
        data = [coindata, fixerdata, mycurrdata, ecbdata]
        use_json = [True, True, True, False]
        if error:
            status = 500
        else:
            status = 200
        with in_memory_cache(), mock_currency_provider(
            klasses, data, use_json, status=status
        ):
            data_queue = Queue()
            cb = callback(data_queue)
            UnitsService().start(force=True)
            CurrencyService().add_update_callback(cb)
            CurrencyService().start(force=True)
            data = data_queue.get(block=True, timeout=None)
            exc = None
            try:
                yield data
            except Exception as e:
                exc = e
            CurrencyService().remove_update_callback(cb)
            CurrencyService().stop()
            if exc:
                raise exc

    @contextmanager
    def cached_data(default_currencies, error=False, **extra_rates):
        rates = currency_data('EUR', **extra_rates)['rates']
        CurrencyService().set_default_currencies(default_currencies)
        key = (tuple(default_currencies), error, *rates.items())
        if key in _mock_currency_service_data:
            yield _mock_currency_service_data[key]
            return

        with uncached_data(rates, error) as data:
            yield data
            _mock_currency_service_data[key] = data

    @contextmanager
    def _mock_currency_service(default_currencies, error=False, **extra_rates):
        with cached_data(default_currencies, error, **extra_rates) as data:
            yield data

    return _mock_currency_service
