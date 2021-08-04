from threading import Event, RLock, Thread
from typing import Callable
import time
import uuid
from calculate_anything.currency.providers import CombinedCurrencyProvider
from calculate_anything.currency.cache import CurrencyCache
from calculate_anything.utils import Singleton, safe_operation, with_lock
from calculate_anything import logging
from calculate_anything.currency.providers.base import CurrencyData


__all__ = ['CurrencyService']


logger = logging.getLogger(__name__)


class UpdateThread(Thread):
    def __init__(self, cache: CurrencyCache,
                 provider: CombinedCurrencyProvider,
                 callback: Callable[[CurrencyData, bool], None],
                 lock: RLock):
        super().__init__()
        self._cache = cache
        self._provider = provider
        self._callback = callback
        self._lock = lock
        self._stopped_event = Event()
        self._woke_event = Event()
        self._ran = False
        self._thread_id = uuid.uuid4()
        name = 'UpdateThread(id={})'.format(self.thread_id)
        self._logger = logger.getChild(name)

    @property
    def thread_id(self):
        return str(self._thread_id).split('-')[-1]

    @property
    def is_sleeping(self):
        return not self._woke_event.is_set()

    def wake(self):
        self._woke_event.set()

    def stop(self):
        self._stopped_event.set()
        self.wake()

    def _get_currencies(self, *currencies, force) -> CurrencyData:
        if force:
            pass
        elif self._cache.enabled and not self._cache.should_update():
            return self._cache.get_rates(*currencies)

        self._logger.info('Will load currencies')
        self._cache.clear()
        currency_rates = self._provider.request_currencies(
            *currencies, force=force)
        if not self._stopped_event.is_set():
            provider_name = self._provider.__class__.__name__
            self._cache.save(currency_rates, provider_name)
        return currency_rates

    @with_lock
    def _run(self, force) -> int:
        next_update = 60

        currency_rates = {}
        try:
            currency_rates = self._get_currencies(force=force)
        except Exception as e:
            self._logger.exception('Could not get currencies: {}'.format(e))

        with safe_operation():
            self._callback(currency_rates, self._provider.had_error)

        if not self._provider.had_error:
            cache_next_update = self._cache.next_update_seconds()
            next_update = max(next_update, cache_next_update)
        return next_update

    def run(self):
        self._logger.info('Starting thread')
        if not self._ran:
            force = self._woke_event.is_set()
            next_update = self._run(force)

        while not self._stopped_event.is_set():
            self._logger.info('Sleeping for {:.0f}s'.format(next_update))

            start = time.time()
            self._woke_event.wait(next_update)
            duration = time.time() - start

            force = self._woke_event.is_set()
            if force:
                msg = 'Forcefully woke up after {:.0f}s'.format(duration)
            else:
                msg = 'Normally woke up after {:.0f}s'.format(duration)
            self._logger.info(msg)

            if self._stopped_event.is_set():
                break
            next_update = self._run(force)
            self._woke_event.clear()

        self._logger.info('Stopping thread')


class CurrencyService(metaclass=Singleton):
    def __init__(self):
        self._default_currencies = []
        self._lock = RLock()
        self._cache = CurrencyCache()
        self._provider = CombinedCurrencyProvider()
        self._is_running = False
        self._enabled = True
        self._thread = None
        self._update_callbacks = []

    @property
    @with_lock
    def is_running(self):
        return self._is_running

    @is_running.setter
    @with_lock
    def is_running(self, is_running):
        self._is_running = is_running

    @property
    @with_lock
    def provider_had_error(self):
        return self._provider.had_error

    @with_lock
    def enable_cache(self, update_frequency):
        if not self._enabled:
            logger.warning('Service is disabled, cannot enable cache')
            return
        logger.info(
            'Enabling cache with update frequency = {}'
            .format(update_frequency))
        self._cache.enable(update_frequency)
        return self

    @with_lock
    def disable_cache(self):
        logger.info('Disabling cache')
        self._cache.disable()
        return self

    @property
    @with_lock
    def cache_enabled(self):
        return self._cache.enabled

    @property
    @with_lock
    def enabled(self):
        return self._enabled

    @with_lock
    def add_provider(self, provider):
        logger.info('Adding provider {}'.format(
            provider.__class__.__name__))
        self._provider.add_provider(provider)
        return self

    @with_lock
    def remove_provider(self, provider):
        logger.info('Removing provider {}'.format(
            provider.__class__.__name__))
        self._provider.remove_provider(provider)
        return self

    @with_lock
    def set_default_currencies(self, default_currencies):
        logger.info(
            'Updating default currencies = {}'.format(default_currencies))
        self._default_currencies = default_currencies
        return self

    @property
    @with_lock
    def default_currencies(self):
        return self._default_currencies

    @with_lock
    def add_update_callback(self, callback):
        self._update_callbacks.append(callback)

    @with_lock
    def remove_update_callback(self, callback):
        callbacks = self._update_callbacks
        callbacks = [cb for cb in callbacks if cb != callback]
        self._update_callbacks = callbacks

    def _stop_thread(self):
        if self._thread is None:
            return
        self._thread.stop()
        self._thread.join()
        self._thread = None

    def _update_callback(self, data: CurrencyData, had_error: bool) -> None:
        for callback in self._update_callbacks:
            with safe_operation():
                callback(data, had_error)

    @with_lock
    def start(self, force=False):
        if force:
            pass
        elif not self._cache.enabled or self._is_running:
            return
        else:
            logger.info('Currency Service is running')

        if self._thread is None:
            cache = self._cache
            provider = self._provider
            callback = self._update_callback
            lock = self._lock
            self._thread = UpdateThread(cache, provider, callback, lock)

        if not self._thread.is_alive():
            self._thread.start()
        elif force and self._thread.is_sleeping:
            self._thread.wake()
        self._is_running = True

    @with_lock
    def enable(self):
        self._enabled = True
        return self

    @with_lock
    def disable(self):
        self.disable_cache()
        self._enabled = False
        return self

    # Don't use a lock because it blocks the thread if it is just before run
    def stop(self):
        self._stop_thread()
        self.is_running = False
        return self
