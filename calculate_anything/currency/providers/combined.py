import sys
if sys.version_info[:2] < (3, 7):
    from collections import OrderedDict
else:
    OrderedDict = dict
from concurrent.futures import ThreadPoolExecutor, as_completed
from .provider import FreeCurrencyProvider, ApiKeyCurrencyProvider, _MockCurrencyProvider, _CurrencyProvider
from .european_central_bank import ECBProvider
from .mycurrencynet import MyCurrencyNetCurrencyProvider
from .coinbase import CoinbaseCurrencyProvider
from ... import logging
from ...utils import is_types
from ...exceptions import CurrencyProviderException, CurrencyProviderRequestException


class CombinedCurrencyProvider(ApiKeyCurrencyProvider):
    def __init__(self):
        super().__init__()
        free_providers = [
            ECBProvider(),
            MyCurrencyNetCurrencyProvider(),
            CoinbaseCurrencyProvider(),
        ]

        self._free_providers = OrderedDict()
        for provider in free_providers:
            self._free_providers[provider.__class__.__name__] = provider

        self._api_providers = OrderedDict()

        self._logger = logging.getLogger(__name__)

    @property
    def api_key_valid(self):
        return True

    @property
    def api_key_valid(self):
        return True

    def add_provider(self, provider):
        # No need to add MockCurrencyProvider or FreeCurrencyProvider
        if is_types(_MockCurrencyProvider, FreeCurrencyProvider)(provider):
            pass
        elif isinstance(provider, ApiKeyCurrencyProvider):
            self._api_providers[provider.__class__.__name__] = provider
        return self

    def remove_provider(self, provider):
        provider_name = provider.__class__.__name__
        if isinstance(provider, _MockCurrencyProvider):
            pass
        elif isinstance(provider, FreeCurrencyProvider):
            if provider_name in self._free_providers:
                del self._free_providers[provider_name]
        elif isinstance(provider, ApiKeyCurrencyProvider):
            if provider_name in self._api_providers:
                del self._api_providers[provider_name]
        return self

    def _thread_request(self, provider_name, provider, *currencies, force):
        try:
            return provider.request_currencies(*currencies, force=force)
        except (CurrencyProviderException, CurrencyProviderRequestException) as e:
            self._logger.error(
                'Got exception when requesting from provider {}: {}'.format(provider_name, e))
        except Exception as e:
            self._logger.exception(
                'An unexpected exception occured when requesting from provider {}: {}'.format(provider_name, e))
        return {}

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)

        providers_currencies = {}
        with ThreadPoolExecutor(max_workers=len(self._free_providers)) as executor:
            free_tasks = []
            for provider_name, provider in self._free_providers.items():
                task = executor.submit(
                    self._thread_request, provider_name, provider, *currencies, force=force)
                free_tasks.append(task)

            api_key_tasks = []
            for provider_name, provider in self._api_providers.items():
                task = executor.submit(
                    self._thread_request, provider_name, provider, *currencies, force=force)
                api_key_tasks.append(task)

            for task in as_completed(free_tasks):
                result = task.result()
                if result is not None:
                    providers_currencies.update(result)

            for task in as_completed(api_key_tasks):
                result = task.result()
                if result is not None:
                    providers_currencies.update(result)

        self._had_error = (
            all(map(lambda provider: provider.had_error, self._free_providers.values())) and
            all(map(lambda provider: provider.had_error, self._api_providers.values()))
        )
        if self._had_error:
            raise CurrencyProviderException(
                'Could not fetch any currency data from any provider')

        return providers_currencies
