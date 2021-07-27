from calculate_anything.currency.providers import (
    CoinbaseCurrencyProvider, MyCurrencyNetCurrencyProvider,
    ECBCurrencyProvider, FixerIOCurrencyProvider
)
from calculate_anything.units import UnitsService
import pytest
from calculate_anything.currency import CurrencyService
from calculate_anything.lang import LanguageService
from calculate_anything.time import TimezoneService
from calculate_anything.preferences import Preferences
from tests.utils import reset_instance


def test_defaults():
    with reset_instance(Preferences, LanguageService,
                        TimezoneService, UnitsService,
                        CurrencyService):

        preferences = Preferences()
        preferences.commit()
        assert preferences.language.lang == LanguageService()._lang == 'en_US'

        assert preferences.time.default_cities == \
            TimezoneService().default_cities

        assert preferences.units.conversion_mode == \
            UnitsService()._conversion_mode == \
            UnitsService.CONVERSION_MODE_NORMAL

        assert preferences.currency.cache_enabled == \
            CurrencyService().cache_enabled == False
        assert preferences.currency.cache_update_frequency == \
            CurrencyService()._cache._update_frequency == 0
        assert preferences.currency.default_currencies == \
            CurrencyService().default_currencies == []
        assert sorted(map(str, preferences.currency.providers )) == \
            sorted(map(str, (
                ECBCurrencyProvider,
                MyCurrencyNetCurrencyProvider,
                CoinbaseCurrencyProvider
            )
        ))
        assert CurrencyService()._is_running == False


test_spec_normal_alts = [{
    'language': {
        'lang': 'en_US'
    },
    'time': {
        'default_cities': 'Athens GR, New York City US',
    },
    'units': {
        'conversion_mode': 'crazy',
    },
    'currency': {
        'cache_update_frequency': 100000,
        'providers': [
            ('fixerIO', '01010'),
            ('fixerIO', 'asasd'),
            ('fixerIO', 'some'),
            ('fixerIO', 'value'),
            ('fixerIO', '12345'),
        ],
        'default_currencies': 'eur, BTC, usd, RON',
    }
}, {
    'language': {
        'lang': 'en_US'
    },
    'time': {
        'default_cities': ['Athens GR', 'New York City US'],
    },
    'units': {
        'conversion_mode': UnitsService.CONVERSION_MODE_CRAZY,
    },
    'currency': {
        'cache_update_frequency': '100000',
        'providers': [
            (FixerIOCurrencyProvider(api_key='00001'), ''),
            (FixerIOCurrencyProvider(api_key='00002'), ''),
            (FixerIOCurrencyProvider(api_key='12345'), '')
        ],
        'default_currencies': ['EUR', 'btc', 'USD', 'ron'],
    }
}]


@pytest.mark.parametrize('test_spec', test_spec_normal_alts)
def test_normal(test_spec):
    with reset_instance(Preferences, LanguageService,
                        TimezoneService, UnitsService,
                        CurrencyService):

        lang = test_spec['language']['lang']
        default_cities = test_spec['time']['default_cities']
        units_conversion_mode = test_spec['units']['conversion_mode']
        currency_cache_update_frequency = test_spec['currency']['cache_update_frequency']
        currency_providers = test_spec['currency']['providers']
        default_currencies = test_spec['currency']['default_currencies']

        preferences = Preferences()
        # preferences.language.set(lang)
        preferences.time.set_default_cities(default_cities)
        return
        preferences.units.set_conversion_mode(units_conversion_mode)
        preferences.currency.enable_cache(currency_cache_update_frequency)
        for provider, api_key in currency_providers:
            preferences.currency.add_provider(provider, api_key)
        preferences.currency.set_default_currencies(default_currencies)
        preferences.commit()

        assert preferences.language.lang == LanguageService()._lang == 'en_US'

        assert preferences.time.default_cities == \
            TimezoneService().default_cities

        default_cities = preferences.time.default_cities
        default_cities = [
            {k: d[k] for k in ['name', 'country', 'cc', 'timezone']}
            for d in default_cities
        ]

        default_cities = map(dict.items, default_cities)
        default_cities = sorted(default_cities)

        default_cities_expected = [{
            'name': 'Athens',
            'country': 'Greece',
            'cc': 'GR',
            'timezone': 'Europe/Athens'
        }, {
            'name': 'New York City',
            'country': 'United States',
            'cc': 'US',
            'timezone': 'America/New_York'
        }]

        default_cities_expected = map(dict.items, default_cities_expected)
        default_cities_expected = sorted(default_cities_expected)

        assert default_cities == default_cities_expected

        assert preferences.units.conversion_mode == \
            UnitsService()._conversion_mode == \
            UnitsService.CONVERSION_MODE_CRAZY

        assert preferences.currency.cache_enabled == \
            CurrencyService().cache_enabled == True
        assert preferences.currency.cache_update_frequency == \
            CurrencyService()._cache._update_frequency == 100000
        assert preferences.currency.default_currencies == \
            CurrencyService().default_currencies == [
                'EUR', 'BTC', 'USD', 'RON']
        assert sorted(map(str, preferences.currency.providers)) == \
            sorted(map(str, (
                ECBCurrencyProvider,
                MyCurrencyNetCurrencyProvider,
                CoinbaseCurrencyProvider,
                FixerIOCurrencyProvider
            )
        ))
        assert CurrencyService()._provider._api_providers[FixerIOCurrencyProvider]._api_key == '12345'
        assert CurrencyService()._is_running == True
