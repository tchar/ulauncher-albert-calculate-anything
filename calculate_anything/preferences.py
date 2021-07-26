"""A module to initiate preferences and services properly"""

from abc import abstractmethod
from calculate_anything.units import UnitsService
from calculate_anything.currency.providers import CurrencyProviderFactory
from calculate_anything.currency.providers.base import _CurrencyProvider
from calculate_anything.currency import CurrencyService
from calculate_anything.lang import LanguageService
from calculate_anything.time import TimezoneService
from calculate_anything.utils import (
    Singleton, get_or_default, is_not_types, is_types,
    safe_operation
)


__all__ = ['Preferences']


class _Preferences:
    def __init__(self):
        self._uncomitted_keys = set()
        self._uncomitted = []
        self._commits = 0

    def _to_commit(self, key, value):
        self._uncomitted.append((key, value))
        self._uncomitted_keys.add(key)

    @abstractmethod
    def _commit_one(self):
        pass

    @abstractmethod
    def _pre_commit(self):
        pass

    def commit(self):
        cls_name = self.__class__.__name__
        for key, value in self._uncomitted:
            update_str = '{}: {} = {}'.format(cls_name, key, value)
            with safe_operation(update_str):
                self._commit_one(key, value)
        self._pre_commit()
        self._uncomitted = []
        self._uncomitted_keys = set()
        self._commits += 1


class LanguagePreferences(_Preferences):
    @property
    def lang(self):
        return LanguageService()._lang

    def set(self, lang):
        super()._to_commit('lang', lang)

    def _commit_one(self, key, value):
        if key == 'lang':
            LanguageService().set(value)

    def _pre_commit(self):
        # Set en_US if no lang has been specified and its first run
        if self._commits == 0 and 'lang' not in self._uncomitted_keys:
            LanguageService().set('en_US')


class TimezonePreferences(_Preferences):
    @property
    def default_cities(self):
        return TimezoneService().default_cities

    def set_default_cities(self, default_cities):
        if not isinstance(default_cities, str):
            default_cities = ','.join(default_cities)
        default_cities = TimezoneService.parse_default_cities(default_cities)
        super()._to_commit('default_cities', default_cities)

    def _commit_one(self, key, value):
        if key == 'default_cities':
            TimezoneService().set_default_cities(value)


class CurrencyPreferences(_Preferences):
    @property
    def default_currencies(self):
        return CurrencyService().default_currencies

    @property
    def cache_update_frequency(self):
        return CurrencyService()._cache._update_frequency

    @property
    def cache_enabled(self):
        return CurrencyService().cache_enabled

    @property
    def providers(self):
        free_providers = CurrencyService()._provider._free_providers
        api_providers = CurrencyService()._provider._api_providers
        return tuple([*free_providers, *api_providers])

    def set_default_currencies(self, default_currencies):
        if is_types(str)(default_currencies):
            default_currencies = default_currencies.split(',')
        default_currencies = map(str.strip, default_currencies)
        default_currencies = map(str.upper, default_currencies)
        default_currencies = list(default_currencies)
        super()._to_commit('default_currencies', default_currencies)

    def set_cache_update_frequency(self, update_frequency):
        update_frequency = get_or_default(update_frequency, int, 86400)
        update_frequency = max(update_frequency, 0)
        super()._to_commit('cache_update_frequency', update_frequency)

    def enable_cache(self, update_frequency):
        self.set_cache_update_frequency(update_frequency)

    def disable_cache(self):
        super()._to_commit('cache_update_frequency', 0)

    def _get_provider(self, provider, api_key):
        if is_not_types(_CurrencyProvider)(provider):
            provider = str(provider).lower()
            provider = get_or_default(
                provider, str, 'internal',
                CurrencyProviderFactory.get_available_providers()
            )
            provider = CurrencyProviderFactory.get_provider(provider, api_key)
        return provider

    def add_provider(self, provider, api_key=''):
        provider = self._get_provider(provider, api_key)
        super()._to_commit('add_provider', provider)

    def remove_provider(self, provider):
        provider = self._get_provider(provider, '')
        super()._to_commit('remove_provider', provider)

    def _commit_one(self, key, value):
        if key == 'default_currencies':
            CurrencyService().set_default_currencies(value)
        elif key == 'cache_update_frequency':
            if value > 0:
                CurrencyService().enable_cache(value)
            else:
                CurrencyService().disable_cache()
        elif key == 'add_provider':
            CurrencyService().remove_provider(value)
            CurrencyService().add_provider(value)
        elif key == 'remove_provider':
            CurrencyService().remove_provider(value)

    def _pre_commit(self):
        # If first run, run service
        if self._commits == 0:
            CurrencyService().run()
        # Else if currency_provider has been provided run with force
        elif 'add_provider' in self._uncomitted_keys:
            CurrencyService().run(force=True)


class UnitsPreferences(_Preferences):
    @property
    def conversion_mode(self):
        return UnitsService().conversion_mode

    def set_conversion_mode(self, mode):
        if isinstance(mode, str):
            mode = mode.lower()
            mode = get_or_default(mode, str, 'normal', ['normal', 'crazy'])
            if mode == 'crazy':
                mode = UnitsService.CONVERSION_MODE_CRAZY
            else:
                mode = UnitsService.CONVERSION_MODE_NORMAL

        mode = get_or_default(
            mode, int, UnitsService.CONVERSION_MODE_NORMAL, [
                UnitsService.CONVERSION_MODE_NORMAL,
                UnitsService.CONVERSION_MODE_CRAZY
            ]
        )
        super()._to_commit('units_conversion_mode', mode)

    def _commit_one(self, key, value):
        if key == 'units_conversion_mode':
            UnitsService().set_conversion_mode(value)

    def _pre_commit(self):
        if self._commits == 0:
            UnitsService().run()


class Preferences(metaclass=Singleton):
    def __init__(self):
        self.language = LanguagePreferences()
        self.time = TimezonePreferences()
        self.units = UnitsPreferences()
        self.currency = CurrencyPreferences()

    def commit(self):
        """Commits preference changes in proper order"""
        self.language.commit()
        self.time.commit()
        self.units.commit()
        self.currency.commit()
