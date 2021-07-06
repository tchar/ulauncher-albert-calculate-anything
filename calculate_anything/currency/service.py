from functools import wraps
from .cache import CurrencyCache
from threading import RLock, Timer
from .providers import ProviderFactory
from ..exceptions import ProviderRequestException
from ..utils import Singleton
from ..logging_wrapper import LoggingWrapper as logging

def lock(func):
    @wraps(func)
    def _wrapper(self, *args, **kwargs):
        with self._lock:
            return func(self, *args, **kwargs)
    return _wrapper

class CurrencyService(metaclass=Singleton):
    def __init__(self):
        self.default_currencies = []
        self._lock = RLock()
        self.provider_had_error = False
        self._logger = logging.getLogger(__name__)
        self._cache = CurrencyCache()
        self._provider = ProviderFactory.get_provider('fixerio')
        self._is_running = False

    def __get_currencies(self, *currencies):
        if not self._cache.enabled or self._cache.should_update():
            self._logger.info('Will load currencies')
            currency_rates = self._provider.request_currencies()
            self._cache.save(currency_rates)
        else:
            currency_rates = self._cache.get_rates(*currencies)
        
        self.provider_had_error = False
        return currency_rates

    @lock
    def enable_cache(self, update_frequency):
        self._cache.enable(update_frequency)
        if self._cache.enabled:
            self.run()

    @lock
    def disable_cache(self):
        self._cache.disable()

    @property
    @lock
    def cache_enabled(self):
        return self._cache.enabled

    @lock
    def set_api_key(self, api_key):
        self._provider.set_api_key(api_key)
        self.run()

    @lock
    def get_rates(self, *currencies):
        try:
            return self.__get_currencies(*currencies)
        except ProviderRequestException:
            self.provider_had_error = True
            return {}

    @lock
    def _update_thread(self):
        if not self._cache.enabled:
            self._is_running = False
            return
        try:
            self.__get_currencies()
            provider_had_error = False
        except ProviderRequestException as e:
            self._logger.error('Error when contacting provider: {}'.format(e))
            provider_had_error = True
        
        self.provider_had_error = provider_had_error
        if not provider_had_error:
            timer_thread = Timer(self._cache.next_update_seconds(), self._update_thread)
        else:
            timer_thread = Timer(60, self._update_thread)

        timer_thread.setDaemon(True)
        timer_thread.start()

    @lock
    def get_available_currencies(self):
        try:
            available_currencies = list(self.__get_currencies().keys())
            self.provider_had_error = False
        except ProviderRequestException as e:
            self.provider_had_error = True
            self._logger.error('Error when contacting provider: {}'.format(e))
            available_currencies = []
        return available_currencies

    @lock
    def set_default_currencies(self, default_currencies):
        self.default_currencies =  default_currencies

    def run(self):
        if not self._cache.enabled or self._is_running or not self._provider.api_key_valid:
            return
        self._is_running = True
        self._logger.info('Currency Service is running')
        timer_thread = Timer(0.0, self._update_thread)
        timer_thread.setDaemon(True)
        timer_thread.start()
