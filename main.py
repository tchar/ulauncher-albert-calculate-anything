from calculate_anything.units.service import UnitsService
import locale
locale.setlocale(locale.LC_ALL, '')
from calculate_anything.query.handlers.percentages import PercentagesQueryHandler
from calculate_anything.query.handlers.units import UnitsQueryHandler
from calculate_anything.query.handlers.calculator import CalculatorQueryHandler
from calculate_anything.query.handlers.currency import CurrencyQueryHandler
from calculate_anything.query.handlers.time import TimeQueryHandler
from calculate_anything.query.handlers.base_n import (
    Base10QueryHandler, Base16QueryHandler,
    Base2QueryHandler, Base8QueryHandler
)
from calculate_anything.time.service import TimezoneService
from calculate_anything.exceptions import MissingRequestsException
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from calculate_anything.currency.service import CurrencyService
from calculate_anything.query import QueryHandler
from calculate_anything.lang import Language
from calculate_anything.utils import get_or_default

class ConverterExtension(Extension):

    def __init__(self):
        super(ConverterExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent, PreferencesUpdateEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        error_num = 0
        query = event.get_argument() or ''
        mode = 'calculator'
        if event.get_keyword() == extension.preferences['time_kw']:
            query = 'now ' + query
            handlers = [TimeQueryHandler]
            mode = 'time'
        elif event.get_keyword() == extension.preferences['dec_kw']:
            handlers = [Base10QueryHandler]
            mode = 'dec'
        elif event.get_keyword() == extension.preferences['hex_kw']:
            handlers = [Base16QueryHandler]
            mode = 'hex'
        elif event.get_keyword() == extension.preferences['oct_kw']:
            handlers = [Base8QueryHandler]
            mode = 'oct'
        elif event.get_keyword() == extension.preferences['bin_kw']:
            handlers = [Base2QueryHandler]
            mode = 'bin'
        else:
            handlers = [
                CalculatorQueryHandler,
                PercentagesQueryHandler,
                UnitsQueryHandler,
                CurrencyQueryHandler,
            ]
        results = QueryHandler().handle(query, *handlers)
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
                extension.preferences['show_empty_placeholder'] == 'y' and len(items) == error_num
            )
        )
        if should_show_placeholder and len(items) == error_num:
            items.append(ExtensionResultItem(
                icon='images/icon.svg',
                name=Language().translate('no-result', 'misc'),
                description=Language().translate('no-result-{}-description'.format(mode), 'misc'),
                highlightable=False,
                on_enter=HideWindowAction()
            ))

        return RenderResultListAction(items)

class PreferencesEventListener(EventListener):
    def on_event(self, event, extension):
        super().on_event(event, extension)

        cache_update = event.preferences['cache']
        cache_update = get_or_default(cache_update, int, 0)

        units_mode = event.preferences['unit_conversion_mode']
        units_mode = get_or_default(units_mode.lower(), str, 'normal',['normal', 'crazy'])

        units_service = UnitsService()
        currency_service = CurrencyService()
        if not cache_update:
            currency_service.disable_cache()
        else:
            currency_service.enable_cache(cache_update)
        
        if units_mode == 'normal':
            units_service.set_unit_conversion_mode(UnitsService.MODE_NORMAL)
        else:
            units_service.set_unit_conversion_mode(UnitsService.MODE_CRAZY)

        default_currencies = event.preferences['default_currencies'].split(',')
        default_currencies = map(str.strip, default_currencies)
        default_currencies = map(str.upper, default_currencies)
        default_currencies = list(default_currencies)
        currency_service.set_default_currencies(default_currencies)

        currency_service.set_api_key(event.preferences['api_key'])
        
        units_service.enable().run()
        currency_service.enable().run()

        default_cities = TimezoneService.parse_default_cities(event.preferences['default_cities'])
        TimezoneService().set_default_cities(default_cities)

class PreferencesUpdateEventListener(EventListener):
    def on_event(self, event, extension):
        super().on_event(event, extension)

        service = CurrencyService()
        if event.id == 'cache':
            new_value = get_or_default(event.new_value, int, 86400)
            if new_value > 0:
                service.enable_cache(new_value).run(force=True)
            else:
                service.disable_cache()
        elif event.id == 'default_currencies':
            default_currencies = event.new_value.split(',')
            default_currencies = map(str.strip, default_currencies)
            default_currencies = map(str.upper, default_currencies)
            default_currencies = list(default_currencies)
            service.set_default_currencies(default_currencies)
        elif event.id == 'api_key':
            service.set_api_key(event.new_value)
            try: service.run(force=True)
            except MissingRequestsException: pass
        elif event.id == 'default_cities':
            default_cities = TimezoneService.parse_default_cities(event.new_value)
            TimezoneService().set_default_cities(default_cities)
        elif event.id == 'unit_conversion_mode':
            units_mode = get_or_default(event.new_value.lower(), str, 'normal',['normal', 'crazy'])
            if units_mode == 'normal':
                units_mode = UnitsService.MODE_NORMAL
            else:
                units_mode = UnitsService.MODE_CRAZY
            UnitsService().set_unit_conversion_mode(units_mode)

if __name__ == '__main__':
    ConverterExtension().run()