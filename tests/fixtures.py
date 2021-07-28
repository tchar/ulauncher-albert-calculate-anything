from contextlib import contextmanager
import pytest
import os
from pytest_httpserver.httpserver import HTTPServer
from werkzeug.wrappers.response import Response
from calculate_anything.currency.providers import (
    CoinbaseCurrencyProvider, ECBCurrencyProvider,
    MyCurrencyNetCurrencyProvider, FixerIOCurrencyProvider
)
from tests.utils import random_str


@pytest.fixture(scope='session')
def log_filepath():
    rand_name = random_str(5)
    rand_name = 'pytest-calculate-anything-{}.log'.format(rand_name)
    rand_filepath = os.path.join('/dev/shm', rand_name)
    yield rand_filepath
    if os.path.exists(rand_filepath):
        os.remove(rand_filepath)


@pytest.fixture(scope='function')
def httpserver_listen_address():
    return ('localhost', 31137)


@ pytest.fixture(scope='function')
def mock_coinbase(httpserver: HTTPServer):
    @contextmanager
    def _mock_coinbase(data, use_json, status=200, respond=True):
        old_url = CoinbaseCurrencyProvider.BASE_URL
        if not respond:
            base_url = 'http://localhost:1234/{}.{}'.format(
                random_str(100), random_str(5))
            CoinbaseCurrencyProvider.BASE_URL = base_url
            yield CoinbaseCurrencyProvider()
            CoinbaseCurrencyProvider.BASE_URL = old_url
            return

        api_url = CoinbaseCurrencyProvider.API_URL
        base_url = httpserver.url_for(old_url)
        api_url_no_qs, qs = api_url.split('?')
        qs = (q.split('=') for q in qs.split('&'))
        qs = {q[0]: q[1] for q in qs}

        CoinbaseCurrencyProvider.BASE_URL = base_url

        request = httpserver.expect_request(api_url_no_qs, query_string=qs)
        if status != 200:
            request.respond_with_response(Response(data, status=status))
        elif use_json:
            request.respond_with_json(data)
        else:
            request.respond_with_data(data)

        yield CoinbaseCurrencyProvider()
        CoinbaseCurrencyProvider.BASE_URL = old_url
    return _mock_coinbase


@pytest.fixture(scope='function')
def mock_ecb(httpserver: HTTPServer):
    @contextmanager
    def _mock_ecb(data, status=200, respond=True):
        old_url = ECBCurrencyProvider.BASE_URL
        if not respond:
            base_url = 'http://localhost:1234/{}.{}'.format(
                random_str(100), random_str(5))
            ECBCurrencyProvider.BASE_URL = base_url
            yield ECBCurrencyProvider()
            ECBCurrencyProvider.BASE_URL = old_url
            return

        api_url = ECBCurrencyProvider.API_URL
        base_url = httpserver.url_for(old_url)

        ECBCurrencyProvider.BASE_URL = base_url

        request = httpserver.expect_request(api_url)
        if status != 200:
            request.respond_with_response(Response(data, status=status))
        else:
            request.respond_with_data(data)

        yield ECBCurrencyProvider()
        ECBCurrencyProvider.BASE_URL = old_url
    return _mock_ecb


@pytest.fixture(scope='function')
def mock_mycurrencynet(httpserver: HTTPServer):
    @contextmanager
    def _mock_mycurrencynet(data, use_json, status=200, respond=True):
        old_url = MyCurrencyNetCurrencyProvider.BASE_URL
        if not respond:
            base_url = 'http://localhost:1234/{}.{}'.format(
                random_str(100), random_str(5))
            MyCurrencyNetCurrencyProvider.BASE_URL = base_url
            yield MyCurrencyNetCurrencyProvider()
            MyCurrencyNetCurrencyProvider.BASE_URL = old_url
            return

        api_url = MyCurrencyNetCurrencyProvider.API_URL
        base_url = httpserver.url_for(old_url)

        MyCurrencyNetCurrencyProvider.BASE_URL = base_url

        request = httpserver.expect_request(api_url)
        if status != 200:
            request.respond_with_response(Response(data, status=status))
        elif use_json:
            request.respond_with_json(data)
        else:
            request.respond_with_data(data)

        yield MyCurrencyNetCurrencyProvider()
        MyCurrencyNetCurrencyProvider.BASE_URL = old_url
    return _mock_mycurrencynet


@ pytest.fixture(scope='function')
def mock_fixerio(httpserver: HTTPServer):
    fixed_api_key = 'mockkey'

    @contextmanager
    def _mock_fixerio(data, use_json, api_key=fixed_api_key,
                      status=200, respond=True):
        old_url = FixerIOCurrencyProvider.BASE_URL
        if not respond:
            base_url = 'http://localhost:1234/{}.{}'.format(
                random_str(100), random_str(5))
            FixerIOCurrencyProvider.BASE_URL = base_url
            yield FixerIOCurrencyProvider(api_key)
            FixerIOCurrencyProvider.BASE_URL = old_url
            return

        api_url = FixerIOCurrencyProvider.API_URL
        base_url = httpserver.url_for(old_url)

        FixerIOCurrencyProvider.BASE_URL = base_url

        request = httpserver.expect_request(api_url)
        if status != 200:
            request.respond_with_response(Response(data, status=status))
        elif use_json:
            request.respond_with_json(data)
        else:
            request.respond_with_data(data)

        provider = FixerIOCurrencyProvider()
        provider.set_api_key(api_key)
        yield provider
        FixerIOCurrencyProvider.BASE_URL = old_url
    return _mock_fixerio
