import locale  # noqa: E402
locale.setlocale(locale.LC_ALL, '')  # noqa: E402
from calculate_anything import init
from calculate_anything import logging
from calculate_anything.utils import get_or_default, safe_operation
from calculate_anything.lang import LanguageService
from calculate_anything.query import MultiHandler
from calculate_anything.query.handlers import (
    PercentagesQueryHandler, UnitsQueryHandler,
    CalculatorQueryHandler, TimeQueryHandler,
    Base10QueryHandler, Base16QueryHandler,
    Base2QueryHandler, Base8QueryHandler
)
from calculate_anything.currency.service import CurrencyService
from calculate_anything.currency.providers import CurrencyProviderFactory
from calculate_anything.units.service import UnitsService
from calculate_anything.time.service import TimezoneService
from calculate_anything.exceptions import MissingRequestsException
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent, SystemExitEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)


class ConverterExtension(Extension):

    def __init__(self):
        super(ConverterExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent,
                       PreferencesUpdateEventListener())
        self.subscribe(SystemExitEvent, SystemExitEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        error_num = 0
        query = event.get_argument() or ''
        mode = 'calculator'
        if event.get_keyword() == extension.preferences['time_kw']:
            query = TimeQueryHandler().keyword + ' ' + query
            handlers = [TimeQueryHandler]
            mode = 'time'
        elif event.get_keyword() == extension.preferences['dec_kw']:
            query = Base10QueryHandler().keyword + ' ' + query
            handlers = [Base10QueryHandler]
            mode = 'dec'
        elif event.get_keyword() == extension.preferences['hex_kw']:
            query = Base16QueryHandler().keyword + ' ' + query
            handlers = [Base16QueryHandler]
            mode = 'hex'
        elif event.get_keyword() == extension.preferences['oct_kw']:
            query = Base8QueryHandler().keyword + ' ' + query
            handlers = [Base8QueryHandler]
            mode = 'oct'
        elif event.get_keyword() == extension.preferences['bin_kw']:
            query = Base2QueryHandler().keyword + ' ' + query
            handlers = [Base2QueryHandler]
            mode = 'bin'
        else:
            query = CalculatorQueryHandler().keyword + ' ' + query
            handlers = [
                CalculatorQueryHandler,
                PercentagesQueryHandler,
                UnitsQueryHandler,
            ]
        results = MultiHandler().handle(query, *handlers)
        for result in results:
            error_num += result.error is not None
            highlightable = result.error is not None
            if result.clipboard is not None:
                on_enter = CopyToClipboardAction(result.clipboard)
            else:
                on_enter = HideWindowAction()

            items.append(ExtensionResultItem(
                icon=result.icon or 'images/icon.svg',
                name=result.name,
                description=result.description,
                highlightable=highlightable,
                on_enter=on_enter
            ))

        should_show_placeholder = (
            query.strip() == '' or (
                extension.preferences['show_empty_placeholder'] == 'y' and len(
                    items) == error_num
            )
        )
        if should_show_placeholder and len(items) == error_num:
            items.append(ExtensionResultItem(
                icon='images/icon.svg',
                name=LanguageService().translate('no-result', 'misc'),
                description=LanguageService().translate(
                    'no-result-{}-description'.format(mode), 'misc'),
                highlightable=False,
                on_enter=HideWindowAction()
            ))

        return RenderResultListAction(items)


class PreferencesEventListener(EventListener):
    def on_event(self, event, extension):
        super().on_event(event, extension)
        init()

        language_service = LanguageService()
        units_service = UnitsService()
        currency_service = CurrencyService()

        with safe_operation('Set language'):
            language_service.set('en_US')

        with safe_operation('Set currency providers'):
            currency_provider = event.preferences['currency_provider']
            currency_provider = get_or_default(
                currency_provider, str, 'internal', CurrencyProviderFactory.get_available_providers())

            currency_provider = currency_provider.lower()
            currency_provider = CurrencyProviderFactory.get_provider(
                currency_provider, api_key=event.preferences['api_key'])
            currency_service.add_provider(currency_provider)

        with safe_operation('Set cache interval'):
            cache_update = event.preferences['cache']
            cache_update = get_or_default(cache_update, int, 0)

            if not cache_update:
                currency_service.disable_cache()
            else:
                currency_service.enable_cache(cache_update)

        with safe_operation('Set units conversion mode'):
            units_mode = event.preferences['units_conversion_mode']
            units_mode = get_or_default(
                units_mode.lower(), str, 'normal', ['normal', 'crazy'])

            if units_mode == 'normal':
                units_service.set_unit_conversion_mode(
                    UnitsService.MODE_NORMAL)
            else:
                units_service.set_unit_conversion_mode(UnitsService.MODE_CRAZY)

        with safe_operation('Set default currencies'):
            default_currencies = event.preferences['default_currencies'].split(
                ',')
            default_currencies = map(str.strip, default_currencies)
            default_currencies = map(str.upper, default_currencies)
            default_currencies = list(default_currencies)
            currency_service.set_default_currencies(default_currencies)

        with safe_operation('Set default cities'):
            default_cities = TimezoneService.parse_default_cities(
                event.preferences['default_cities'])
            TimezoneService().set_default_cities(default_cities)

        units_service.enable().run()
        currency_service.enable().run()


class PreferencesUpdateEventListener(EventListener):
    @safe_operation('Update preferences')
    def on_event(self, event, extension):
        super().on_event(event, extension)

        currency_service = CurrencyService()
        if event.id == 'cache':
            new_value = get_or_default(event.new_value, int, 86400)
            if new_value > 0:
                currency_service.enable_cache(new_value).run(force=True)
            else:
                currency_service.disable_cache()
        elif event.id == 'default_currencies':
            default_currencies = event.new_value.split(',')
            default_currencies = map(str.strip, default_currencies)
            default_currencies = map(str.upper, default_currencies)
            default_currencies = list(default_currencies)
            currency_service.set_default_currencies(default_currencies)
        elif event.id == 'api_key':
            currency_provider = extension.preferences['currency_provider']
            currency_provider = get_or_default(
                currency_provider, str, 'internal', CurrencyProviderFactory.get_available_providers())
            currency_provider = currency_provider.lower()

            api_key = event.new_value
            currency_provider = CurrencyProviderFactory.get_provider(
                currency_provider, api_key)
            currency_service.add_provider(currency_provider)

            try:
                currency_service.run(force=True)
            except MissingRequestsException:
                pass
        elif event.id == 'default_cities':
            default_cities = TimezoneService.parse_default_cities(
                event.new_value)
            TimezoneService().set_default_cities(default_cities)
        elif event.id == 'units_conversion_mode':
            units_mode = get_or_default(
                event.new_value.lower(), str, 'normal', ['normal', 'crazy'])
            if units_mode == 'normal':
                units_mode = UnitsService.MODE_NORMAL
            else:
                units_mode = UnitsService.MODE_CRAZY
            UnitsService().set_unit_conversion_mode(units_mode)
        elif event.id == 'currency_provider':
            old_currency_provider = event.old_value

            old_currency_provider = get_or_default(
                old_currency_provider, str, 'internal', CurrencyProviderFactory.get_available_providers())
            old_currency_provider = old_currency_provider.lower()
            old_currency_provider = CurrencyProviderFactory.get_provider(
                old_currency_provider)
            currency_service.remove_provider(old_currency_provider)

            currency_provider = event.new_value
            currency_provider = get_or_default(
                currency_provider, str, 'internal', CurrencyProviderFactory.get_available_providers())
            currency_provider = currency_provider.lower()
            api_key = extension.preferences.get('api_key', '')
            currency_provider = CurrencyProviderFactory.get_provider(
                currency_provider, api_key)
            currency_service.add_provider(currency_provider)
            try:
                currency_service.run(force=True)
            except MissingRequestsException:
                pass


class SystemExitEventListener(EventListener):
    def on_event(self, event, extension):
        TimezoneService().stop()
        return super().on_event(event, extension)


if __name__ == '__main__':
    ConverterExtension().run()
