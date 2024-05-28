'''A module to initiate preferences and services properly'''

from abc import abstractmethod
from typing import Any, Iterable, List, Tuple, Union
from calculate_anything.units import UnitsService
from calculate_anything.currency.providers import CurrencyProviderFactory
from calculate_anything.currency.providers.base import CurrencyProvider
from calculate_anything.currency import CurrencyService
from calculate_anything.lang import LanguageService
from calculate_anything.time import TimezoneService
from calculate_anything.utils import (
    Singleton,
    get_or_default,
    is_not_types,
    safe_operation,
)


__all__ = ['Preferences']


class _Preferences:
    def __init__(self):
        self._uncomitted_keys = set()
        self._uncomitted = []
        self._commits = 0

    def _to_commit(self, key: str, value: Any) -> None:
        self._uncomitted.append((key, value))
        self._uncomitted_keys.add(key)

    @abstractmethod
    def _commit_one(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def _pre_commit(self, *args: Any, **kwargs: Any) -> None:
        pass

    def commit(self) -> None:
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
    '''The language preferences class

    Attributes:
        lang (str): The language currently in use
    '''

    @property
    def lang(self) -> str:
        return LanguageService().lang

    def set(self, lang: str) -> None:
        '''Language to be changed. The language is not set immediately,
        but only after 'commit()' is called

        Args:
            lang (str): The language to set. The name must be a file from
                data/lang without the extension.
        '''
        super()._to_commit('lang', lang)

    def _commit_one(self, key: str, value: Any) -> None:
        if key == 'lang':
            LanguageService().set(value)

    def _pre_commit(self) -> None:
        # Set en_US if no lang has been specified and its first start
        if self._commits == 0 and 'lang' not in self._uncomitted_keys:
            LanguageService().set('en_US')


class TimePreferences(_Preferences):
    '''The timezone preferences class

    Attributes:
        default_cities (str): The default cities currently in use
    '''

    @property
    def default_cities(self) -> str:
        return TimezoneService().default_cities

    def set_default_cities(
        self, default_cities: Union[str, Iterable[str]]
    ) -> None:
        '''Default cities to be set. The cities are not set immediately,
        but only after 'commit()' is called

        Args:
            default_cities (Union[str, Iterable[str]]): The default cities to
                set. If str is provided it must be comma separated cities.
                (i.e 'Athens GR,New York City US')
                (i.e ['Athens GR', 'New York City US'])
        '''
        if not isinstance(default_cities, str):
            default_cities = ','.join(default_cities)
        default_cities = TimezoneService().parse_default_cities_str(
            default_cities, save=False
        )
        super()._to_commit('default_cities', default_cities)

    def _commit_one(self, key: str, value: Any) -> None:
        if key == 'default_cities':
            TimezoneService().set_default_cities(value)

    def _pre_commit(self) -> None:
        if self._commits == 0:
            TimezoneService().start()


class CurrencyPreferences(_Preferences):
    '''The currency preferences class

    Attributes:
        default_currencies (list of str): The default currencies currently in
            use
        cache_update_frequency (int): An integer representing the current
            interval of cache update in seconds
        cache_enabled (bool): Wether cache is currently enabled or not
        providers (tuple of str): A tuple of currently enabled currency
            providers.
    '''

    @property
    def default_currencies(self) -> List[str]:
        return CurrencyService().default_currencies

    @property
    def cache_update_frequency(self) -> int:
        return CurrencyService()._cache._update_frequency

    @property
    def cache_enabled(self) -> bool:
        return CurrencyService().cache_enabled

    @property
    def providers(self) -> Tuple[str]:
        free_providers = CurrencyService()._provider._free_providers
        api_providers = CurrencyService()._provider._api_providers
        return tuple([*free_providers, *api_providers])

    def set_default_currencies(
        self, default_currencies: Union[str, Iterable[str]]
    ) -> None:
        '''Default currencies to set. The currencies are not set immediately,
        but only after 'commit()' is called

        Args:
            default_currencies (Union[str, Iterable[str]]): The default
                currencies to set in iso3 format. If str is provided it must
                be comma separated currencies. (i.e 'EUR,CAD,BTC,USD'),
                (i.e ['EUR', 'CAD', 'BTC', 'USD])
        '''
        if isinstance(default_currencies, str):
            default_currencies = default_currencies.split(',')
        default_currencies = map(str.strip, default_currencies)
        default_currencies = map(str.upper, default_currencies)
        default_currencies = list(default_currencies)
        super()._to_commit('default_currencies', default_currencies)

    def set_cache_update_frequency(self, update_frequency: int) -> None:
        '''Update frequency to set. The update frequency is not set immediately,
        but only after 'commit()' is called

        Args:
            update_frequency (int): An integer representing an interval
                in seconds in which cache will be updated.
        '''
        update_frequency = get_or_default(update_frequency, int, 86400)
        update_frequency = max(update_frequency, 0)
        super()._to_commit('cache_update_frequency', update_frequency)

    def enable_cache(self, update_frequency: int) -> None:
        '''Alias of 'set_cache_update_frequency()'.'''
        self.set_cache_update_frequency(update_frequency)

    def disable_cache(self) -> None:
        '''Disables the cache after 'commit()' is called.'''
        super()._to_commit('cache_update_frequency', 0)

    def _get_provider(
        self, provider: Union[str, CurrencyProvider], api_key: str
    ) -> CurrencyProvider:
        if is_not_types(CurrencyProvider)(provider):
            provider = str(provider).lower()
            provider = get_or_default(
                provider,
                str,
                'internal',
                CurrencyProviderFactory.get_available_providers(),
            )
            provider = CurrencyProviderFactory.get_provider(provider, api_key)
        return provider

    def add_provider(
        self, provider: Union[str, CurrencyProvider], api_key: str = ''
    ) -> None:
        '''A currency provider to be added with an asociated api_key.
        The provider is not set immediately, but only after 'commit()' is
        called

        Args:
            provider (Union[str, CurrencyProvider]): If str is provided it
                must represent a provider name str as returned by
                'CurrencyProviderFactory.get_available_providers()'. if a
                CurrencyProvider is provided, api_key is ignored
            api_key (str): The api_key to set if provider is a str.
        '''
        provider = self._get_provider(provider, api_key)
        super()._to_commit('add_provider', provider)

    def remove_provider(self, provider: Union[str, CurrencyProvider]) -> None:
        '''A currency provider to be removed. The provider is not removed
        immediately, but only after 'commit()' is called

        Args:
            provider (Union[str, CurrencyProvider]): If str is provided it
                must represent a provider name str as returned by
                'CurrencyProviderFactory.get_available_providers()'. if a
                CurrencyProvider is provided, api_key is ignored
        '''
        provider = self._get_provider(provider, '')
        super()._to_commit('remove_provider', provider)

    def set_currency_provider_protocol(self, protocol) -> None:
        '''The protocol to be updated. The update happens after 'commit()' is
        called.

        Args:
            protocol (str one of {http, https})
        '''
        super()._to_commit('set_currency_provider_protocol', protocol)

    def _commit_one(self, key: str, value: Any) -> None:
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
        elif key == 'set_currency_provider_protocol':
            CurrencyService().set_currency_provider_protocol(value)

    def _pre_commit(self) -> None:
        # If first start, start service
        if self._commits == 0:
            CurrencyService().start()
        # Else if currency_provider has been provided start with force
        elif 'add_provider' in self._uncomitted_keys:
            CurrencyService().start(force=True)


class UnitsPreferences(_Preferences):
    '''The units preferences class

    Attributes:
        conversion_mode (UnitsService.ConversionMode): The conversion mode
            currently in use as in UnitsService.ConversionMode.
    '''

    @property
    def conversion_mode(self) -> UnitsService.ConversionMode:
        return UnitsService().conversion_mode

    def set_conversion_mode(
        self, mode: Union[str, UnitsService.ConversionMode]
    ) -> None:
        '''A conversion mode to be set. The mode is not removed immediately,
        but only after 'commit()' is called

        Args:
            mode (Union[str, UnitsService.ConversionMode]): If str is provided
                it must represent a conversion mode (i.e 'normal', 'crazy').
                If int is provided it must be one of
                UnitsService.ConversionMode.
        '''
        if isinstance(mode, str):
            mode = mode.lower()
            mode = get_or_default(mode, str, 'normal', ['normal', 'crazy'])
            if mode == 'crazy':
                mode = UnitsService.ConversionMode.CRAZY
            else:
                mode = UnitsService.ConversionMode.NORMAL

        mode = get_or_default(
            mode,
            UnitsService.ConversionMode,
            UnitsService.ConversionMode.NORMAL,
            [
                UnitsService.ConversionMode.NORMAL,
                UnitsService.ConversionMode.CRAZY,
            ],
        )
        super()._to_commit('units_conversion_mode', mode)

    def _commit_one(self, key: str, value: Any) -> None:
        if key == 'units_conversion_mode':
            UnitsService().set_conversion_mode(value)

    def _pre_commit(self) -> None:
        if self._commits == 0:
            UnitsService().start()


class Preferences(metaclass=Singleton):
    '''The Preferences class is a Singleton class which holds all other
    preferences, like language, timezone, units and currency.

    Attributes:
        language (LanguagePreferences): The language preferences reference.
        time (TimePreferences): The time preferences reference.
        units (UnitsPreferences): The units preferences reference.
        currency (CurrencyPreferences): The currency preferences reference.
    '''

    def __init__(self):
        self.language = LanguagePreferences()
        self.time = TimePreferences()
        self.units = UnitsPreferences()
        self.currency = CurrencyPreferences()

    def commit(self) -> None:
        '''Commits preference changes in proper order'''
        self.language.commit()
        self.time.commit()
        self.units.commit()
        self.currency.commit()
