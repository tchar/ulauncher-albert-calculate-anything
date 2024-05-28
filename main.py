# -*- coding: utf-8 -*-
from calculate_anything.utils.misc import images_dir
from calculate_anything import logging
from ulauncher.api.shared.action.CopyToClipboardAction import (
    CopyToClipboardAction,
)
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RenderResultListAction import (
    RenderResultListAction,
)
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.event import (
    KeywordQueryEvent,
    PreferencesEvent,
    PreferencesUpdateEvent,
    SystemExitEvent,
)
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from calculate_anything.utils import safe_operation
from calculate_anything.preferences import Preferences
from calculate_anything.query.handlers import (
    PercentagesQueryHandler,
    UnitsQueryHandler,
    CalculatorQueryHandler,
    TimeQueryHandler,
    Base10QueryHandler,
    Base16QueryHandler,
    Base2QueryHandler,
    Base8QueryHandler,
)
from calculate_anything.query.handlers import MultiHandler
from calculate_anything.time import TimezoneService
from calculate_anything.lang import LanguageService
from calculate_anything.currency import CurrencyService


# See what I did for Ulauncher.
# You won't let use my own formatter, due to duplicate logs
logging.disable_stdout_handler()


class CalculateAnythingExtension(Extension):
    def __init__(self):
        super(CalculateAnythingExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent, PreferencesUpdateEventListener())
        self.subscribe(SystemExitEvent, SystemExitEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query_nokw = event.get_argument() or ''
        query = event.get_query() or ''
        query = query.replace(event.get_keyword() + ' ', '', 1)
        mode = 'calculator'
        if event.get_keyword() == extension.preferences['time_kw']:
            query = TimeQueryHandler().keyword + query
            handlers = [TimeQueryHandler]
            mode = 'time'
        elif event.get_keyword() == extension.preferences['dec_kw']:
            query = Base10QueryHandler().keyword + query
            handlers = [Base10QueryHandler]
            mode = 'dec'
        elif event.get_keyword() == extension.preferences['hex_kw']:
            query = Base16QueryHandler().keyword + query
            handlers = [Base16QueryHandler]
            mode = 'hex'
        elif event.get_keyword() == extension.preferences['oct_kw']:
            query = Base8QueryHandler().keyword + query
            handlers = [Base8QueryHandler]
            mode = 'oct'
        elif event.get_keyword() == extension.preferences['bin_kw']:
            query = Base2QueryHandler().keyword + query
            handlers = [Base2QueryHandler]
            mode = 'bin'
        else:
            query = CalculatorQueryHandler().keyword + query
            handlers = [
                UnitsQueryHandler,
                CalculatorQueryHandler,
                PercentagesQueryHandler,
            ]

        items = []
        results = MultiHandler().handle(query, *handlers)
        for result in results:
            if result.clipboard is not None:
                on_enter = CopyToClipboardAction(result.clipboard)
            else:
                on_enter = HideWindowAction()

            items.append(
                ExtensionResultItem(
                    icon=result.icon or images_dir('icon.svg'),
                    name=result.name,
                    description=result.description,
                    highlightable=False,
                    on_enter=on_enter,
                )
            )

        should_show_placeholder = (
            query_nokw.strip() == '' and len(items) == 0
        ) or (
            len(items) == 0
            and extension.preferences['show_empty_placeholder'] == 'y'
        )

        if should_show_placeholder:
            items.append(
                ExtensionResultItem(
                    icon=images_dir('icon.svg'),
                    name=LanguageService().translate('no-result', 'misc'),
                    description=LanguageService().translate(
                        'no-result-{}-description'.format(mode), 'misc'
                    ),
                    highlightable=False,
                    on_enter=HideWindowAction(),
                )
            )

        return RenderResultListAction(items)


class PreferencesEventListener(EventListener):
    def on_event(self, event, extension):
        super().on_event(event, extension)

        preferences = Preferences()

        with safe_operation('Set language'):
            preferences.language.set('en_US')

        with safe_operation('Set default cities'):
            default_cities = event.preferences['default_cities']
            preferences.time.set_default_cities(default_cities)

        with safe_operation('Set units conversion mode'):
            mode = event.preferences['units_conversion_mode']
            preferences.units.set_conversion_mode(mode)

        with safe_operation('Set currency provider protocol'):
            protocol = event.preferences['currency_provider_protocol']
            preferences.currency.set_currency_provider_protocol(protocol)

        with safe_operation('Set currency providers'):
            provider = event.preferences['currency_provider']
            api_key = event.preferences['api_key']
            preferences.currency.add_provider(provider, api_key)

        with safe_operation('Set cache interval'):
            frequency = event.preferences['cache']
            preferences.currency.set_cache_update_frequency(frequency)

        with safe_operation('Set default currencies'):
            default_currencies = event.preferences['default_currencies']
            preferences.currency.set_default_currencies(default_currencies)

        preferences.commit()


class PreferencesUpdateEventListener(EventListener):
    @safe_operation('Update preferences')
    def on_event(self, event, extension):
        super().on_event(event, extension)

        preferences = Preferences()

        if event.id == 'cache':
            preferences.currency.set_cache_update_frequency(event.new_value)
        elif event.id == 'default_currencies':
            preferences.currency.set_default_currencies(event.new_value)
        elif event.id == 'api_key':
            currency_provider = extension.preferences['currency_provider']
            preferences.currency.add_provider(
                currency_provider, event.new_value
            )
        elif event.id == 'currency_provider':
            old_provider = event.old_value
            preferences.currency.remove_provider(old_provider)
            api_key = extension.preferences['api_key']
            preferences.currency.add_provider(event.new_value, api_key)
        elif event.id == 'currency_provider_protocol':
            preferences.currency.set_currency_provider_protocol(event.new_value)
        elif event.id == 'default_cities':
            preferences.time.set_default_cities(event.new_value)
        elif event.id == 'units_conversion_mode':
            preferences.units.set_conversion_mode(event.new_value)

        preferences.commit()


class SystemExitEventListener(EventListener):
    def on_event(self, event, extension):
        TimezoneService().stop()
        CurrencyService().stop()
        return super().on_event(event, extension)


if __name__ == '__main__':
    CalculateAnythingExtension().run()
