from functools import wraps
from calculate_anything.currency.providers import CombinedCurrencyProvider
from calculate_anything.currency.cache import CurrencyCache
from threading import RLock, Timer
from calculate_anything.exceptions import CurrencyProviderRequestException, MissingRequestsException
from calculate_anything.utils.singleton import Singleton
from calculate_anything.utils.misc import safe_operation, lock
import calculate_anything.log as logging


class CurrencyService(metaclass=Singleton):
    def __init__(self):
        self._default_currencies = []
        self._lock = RLock()
        self._logger = logging.getLogger(__name__)
        self._cache = CurrencyCache()
        self._provider = CombinedCurrencyProvider()
        self._thread_id = 0
        self._is_running = False
        self._enabled = True
        self._update_callbacks = []
        self._missing_requests = False

    def __get_currencies(self, *currencies, force=False):
        provider = self._provider.__class__.__name__
        if force or not self._cache.enabled or self._cache.should_update():
            self._logger.info('Will load currencies')
            try:
                self._cache.clear()
                currency_rates = self._provider.request_currencies(
                    *currencies, force=force)
            except MissingRequestsException as e:
                self._missing_requests = True
                raise e
            self._cache.save(currency_rates, provider)
        else:
            currency_rates = self._cache.get_rates(*currencies)

        return currency_rates

    @lock
    def _update_thread(self, thread_id, force=False):
        if force:
            pass
        elif not self._is_running:
            self._logger.info(
                'Stopping thread (id={}). Service stopped'.format(thread_id))
            return
        elif thread_id != self._thread_id:
            self._logger.info('Stopping thread (id={}). Another thread is running (id={})'.format(
                thread_id, self._thread_id))
            return
        elif not self._cache.enabled:
            self._logger.info(
                'Stopping thread (id={}). Cache not enabled'.format(thread_id))
            self._is_running = False
            return
        try:
            currency_rates = self.__get_currencies(force=force)
            for callback in self._update_callbacks:
                with safe_operation():
                    callback(currency_rates)
        except CurrencyProviderRequestException as e:
            self._logger.error('Error when contacting provider: {}'.format(e))
        except MissingRequestsException as e:
            self._logger.error(e)
            self._missing_requests = True
            return

        if force and not self._cache.enabled:
            self._logger.info(
                'Stopping thread (id={}). Cache not enabled'.format(thread_id))
            self._is_running = False
            return

        next_update_seconds = 60
        if not self._provider.had_error:
            next_update_seconds = max(
                self._cache.next_update_seconds(), next_update_seconds)
            timer_thread = Timer(next_update_seconds,
                                 self._update_thread, args=(thread_id,))
        else:
            self._cache.clear()
            timer_thread = Timer(next_update_seconds,
                                 self._update_thread, args=(thread_id,))

        timer_thread.setDaemon(True)
        timer_thread.start()

    @property
    def provider_had_error(self):
        return self._provider.had_error

    @lock
    def enable_cache(self, update_frequency):
        if not self._enabled:
            self._logger.warning('Service is disabled, cannot enable cache')
            return
        self._logger.info(
            'Enabling cache with update frequence = {}'.format(update_frequency))
        self._cache.enable(update_frequency)
        return self

    @lock
    def disable_cache(self):
        self._logger.info('Disabling cache')
        self._cache.disable()
        return self

    @property
    @lock
    def cache_enabled(self):
        return self._cache.enabled

    @property
    @lock
    def enabled(self):
        return self._enabled

    @lock
    def add_provider(self, provider):
        self._logger.info('Adding provider {}'.format(
            provider.__class__.__name__))
        self._provider.add_provider(provider)
        return self

    @lock
    def remove_provider(self, provider):
        self._logger.info('Removing provider {}'.format(
            provider.__class__.__name__))
        self._provider.remove_provider(provider)
        return self

    @lock
    def set_default_currencies(self, default_currencies):
        self._logger.info(
            'Updating default currencies = {}'.format(default_currencies))
        self._default_currencies = default_currencies
        return self

    @property
    @lock
    def default_currencies(self):
        return self._default_currencies

    @lock
    def add_update_callback(self, callback):
        self._update_callbacks.append(callback)

    @lock
    def remove_update_callback(self, callback):
        callbacks = self._update_callbacks
        callbacks = [cb for cb in callbacks if cb != callback]
        self._update_callbacks = callbacks

    @lock
    def get_rate_timestamp(self, currency):
        return self._cache.get_rate_timestamp(currency)

    @property
    @lock
    def missing_requests(self):
        return self._missing_requests

    # @lock
    # def get_rates(self, *currencies, force=False):
    #     if not self._enabled:
    #         self._logger.warning('Service is disabled cannot get rates')
    #         return {}
    #     try:
    #         return self.__get_currencies(*currencies, force=force)
    #     except CurrencyProviderRequestException:
    #         return {}

    # @lock
    # def get_available_currencies(self):
    #     try:
    #         available_currencies = list(self.__get_currencies().keys())
    #     except CurrencyProviderRequestException as e:
    #         self._logger.error('Error when contacting provider: {}'.format(e))
    #         available_currencies = []
    #     return available_currencies

    @lock
    def run(self, force=False):
        if force:
            pass
        elif not self._cache.enabled or self._is_running:
            return
        self._is_running = True
        self._logger.info('Currency Service is running')
        self._thread_id += 1
        timer_thread = Timer(0.0, self._update_thread, args=(
            self._thread_id,), kwargs={'force': force})
        timer_thread.setDaemon(True)
        timer_thread.start()

    @lock
    def enable(self):
        self._enabled = True
        return self

    @lock
    def disable(self):
        self.disable_cache()
        self._enabled = False
        return self

    @lock
    def stop(self):
        self._is_running = False
        return self
