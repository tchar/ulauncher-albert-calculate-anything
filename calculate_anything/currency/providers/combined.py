import sys
if sys.version_info[:2] < (3, 7):
    from collections import OrderedDict
else:
    OrderedDict = dict
from concurrent.futures import ThreadPoolExecutor
from calculate_anything.currency.providers.provider import FreeCurrencyProvider, ApiKeyCurrencyProvider, _MockCurrencyProvider
from calculate_anything.currency.providers.european_central_bank import ECBCurrencyProvider
from calculate_anything.currency.providers.mycurrencynet import MyCurrencyNetCurrencyProvider
from calculate_anything.currency.providers.coinbase import CoinbaseCurrencyProvider
import calculate_anything.log as logging
from calculate_anything.exceptions import CurrencyProviderException, CurrencyProviderRequestException


class CombinedCurrencyProvider(ApiKeyCurrencyProvider):
    def __init__(self):
        super().__init__()
        free_providers = [
            ECBCurrencyProvider(),
            MyCurrencyNetCurrencyProvider(),
            CoinbaseCurrencyProvider(),
        ]

        self._free_providers = OrderedDict()
        for provider in free_providers:
            self._free_providers[provider.__class__] = provider
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
        if isinstance(provider, (_MockCurrencyProvider, FreeCurrencyProvider)):
            pass
        elif isinstance(provider, ApiKeyCurrencyProvider):
            self._api_providers[provider.__class__] = provider
        return self

    def remove_provider(self, provider):
        provider_cls = provider.__class__
        if isinstance(provider, _MockCurrencyProvider):
            pass
        elif isinstance(provider, FreeCurrencyProvider):
            if provider_cls in self._free_providers:
                del self._free_providers[provider_cls]
        elif isinstance(provider, ApiKeyCurrencyProvider):
            if provider_cls in self._api_providers:
                del self._api_providers[provider_cls]
        return self

    def _thread_request(self, provider_cls, provider, *currencies, force):
        provider_name = provider_cls.__name__
        try:
            return provider.request_currencies(*currencies, force=force)
        except (CurrencyProviderException, CurrencyProviderRequestException) as e:
            self._logger.error(
                'Got exception when requesting from provider {}: {}'.format(provider_name, e))
        except Exception as e:
            self._logger.exception(
                'An unexpected exception occured when requesting from provider {}: {}'.format(provider_name, e))
        return {}

    def _request_free(self, currencies, force):
        if not self._free_providers:
            return []

        with ThreadPoolExecutor(max_workers=len(self._free_providers)) as executor:
            tasks = []
            for provider_cls, provider in self._free_providers.items():
                task = executor.submit(
                    self._thread_request, provider_cls, provider, *currencies, force=force)
                tasks.append(task)
        return tasks

    def _request_api(self, currencies, force):
        if not self._api_providers:
            return []

        with ThreadPoolExecutor(max_workers=len(self._api_providers)) as executor:
            tasks = []
            for provider_cls, provider in self._api_providers.items():
                task = executor.submit(
                    self._thread_request, provider_cls, provider, *currencies, force=force)
                tasks.append(task)
        return tasks

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)

        tasks_free = self._request_free(currencies, force)
        tasks_api = self._request_api(currencies, force)

        providers_currencies = {}

        for task in tasks_free:
            result = task.result()
            if result is not None:
                providers_currencies.update(result)

        for task in tasks_api:
            result = task.result()
            if result is not None:
                providers_currencies.update(result)

        self.had_error = (
            all(map(lambda provider: provider.had_error, self._free_providers.values())) and
            all(map(lambda provider: provider.had_error, self._api_providers.values()))
        )
        if self.had_error:
            raise CurrencyProviderException(
                'Could not fetch any currency data from any provider')

        return providers_currencies
