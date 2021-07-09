from functools import wraps
from .cache import CurrencyCache
from threading import RLock, Timer
from .providers import ProviderFactory
from ..exceptions import CurrencyProviderRequestException, MissingRequestsException
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
        self._logger = logging.getLogger(__name__)
        self._cache = CurrencyCache()
        self._provider = ProviderFactory.get_provider('fixerio')
        self._thread_id = 0
        self._is_running = False

    def __get_currencies(self, *currencies, force=False):
        if force or not self._cache.enabled or self._cache.should_update():
            self._logger.info('Will load currencies')
            try: 
                currency_rates = self._provider.request_currencies(*currencies, force=force)
            except MissingRequestsException as e:
                self._cache.clear()
                raise e
            self._cache.save(currency_rates)
        else:
            currency_rates = self._cache.get_rates(*currencies)
        
        return currency_rates

    @property
    def provider_had_error(self):
        return self._provider.had_error

    @lock
    def enable_cache(self, update_frequency, force_run=False):
        self._logger.info('Enabling cache with update frequence = {}'.format(update_frequency))
        self._cache.enable(update_frequency)
        if self._cache.enabled:
            self.run(force=force_run)

    @lock
    def disable_cache(self):
        self._logger.info('Disabling cache')
        self._cache.disable()

    @property
    @lock
    def cache_enabled(self):
        return self._cache.enabled

    @lock
    def set_api_key(self, api_key, force_run=False):
        self._logger.info('Updating api key = {}'.format(api_key))
        self._provider.set_api_key(api_key)
        if self._provider.api_key_valid:
            self.run(force=force_run)

    @lock
    def get_rates(self, *currencies, force=False):
        try:
            return self.__get_currencies(*currencies, force=force)
        except CurrencyProviderRequestException:
            return {}

    @lock
    def _update_thread(self, thread_id, force=False):
        if thread_id != self._thread_id:
            self._logger.info('Stopping thread (id={}). Another thread is running (id={})'.format(thread_id, self._thread_id))
            return
        if not self._cache.enabled:
            self._logger.info('Stopping thread (id={}). Cache not enabled'.format(thread_id))
            self._is_running = False
            return
        try:
            self.__get_currencies(force=force)
        except CurrencyProviderRequestException as e:
            self._logger.error('Error when contacting provider: {}'.format(e))
        except MissingRequestsException as e:
            self._logger.error(e)
            return

        if not self._provider.had_error:
            timer_thread = Timer(self._cache.next_update_seconds(), self._update_thread, args=(thread_id,))
        else:
            self._cache.clear()
            timer_thread = Timer(60, self._update_thread, args=(thread_id,))

        timer_thread.setDaemon(True)
        timer_thread.start()

    @lock
    def get_available_currencies(self):
        try:
            available_currencies = list(self.__get_currencies().keys())
        except CurrencyProviderRequestException as e:
            self._logger.error('Error when contacting provider: {}'.format(e))
            available_currencies = []
        return available_currencies

    @lock
    def set_default_currencies(self, default_currencies):
        self._logger.info('Updating default currencies = {}'.format(default_currencies))
        self.default_currencies =  default_currencies

    @lock
    def run(self, force=False):
        if force: pass
        elif not self._cache.enabled or self._is_running or not self._provider.api_key_valid:
            return
        self._is_running = True
        self._logger.info('Currency Service is running')
        self._thread_id += 1
        timer_thread = Timer(0.0, self._update_thread, args=(self._thread_id,), kwargs={'force': force})
        timer_thread.setDaemon(True)
        timer_thread.start()
