from calculate_anything.query.handlers.percentages import PercentagesQueryHandler
from calculate_anything.query.handlers.units import UnitsQueryHandler
from calculate_anything.query.handlers.calculator import CalculatorQueryHandler
from calculate_anything.query.handlers.currency import CurrencyQueryHandler
from calculate_anything.query.handlers.time import TimeQueryHandler
from calculate_anything.time.service import TimezoneService
import locale
locale.setlocale(locale.LC_ALL, '')
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from calculate_anything.currency.service import CurrencyService
from calculate_anything.query import QueryHandler
from calculate_anything.query.lang import Language

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
        if event.get_keyword() == extension.preferences['time_kw']:
            query = 'now ' + query
            handlers = set([TimeQueryHandler])
        else:
            handlers = set([CalculatorQueryHandler, PercentagesQueryHandler,UnitsQueryHandler, CurrencyQueryHandler])

        results = QueryHandler().handle(query, *handlers)
        for result in results:
            error_num += result.is_error
            highlightable = result.is_error
            on_enter = CopyToClipboardAction(str(result.value)) if result.clipboard else HideWindowAction()

            items.append(ExtensionResultItem(
                icon=result.icon or 'images/icon.svg',
                name=result.name,
                description=result.description,
                highlightable=highlightable,
                on_enter=on_enter
            ))
        
        if len(items) == error_num:
            items.append(ExtensionResultItem(
                icon='images/icon.svg',
                name=Language().translate('no-result', 'misc'),
                description=Language().translate('no-result-description', 'misc'),
                highlightable=False,
                on_enter=HideWindowAction()
            ))

        return RenderResultListAction(items)

class PreferencesEventListener(EventListener):
    def on_event(self, event, extension):
        super().on_event(event, extension)
        cache_update = int(event.preferences['cache'])

        service = CurrencyService()
        if not cache_update:
            service.disable_cache()
        else:
            service.enable_cache(cache_update)

        default_currencies = event.preferences['default_currencies'].split(',')
        default_currencies = map(str.strip, default_currencies)
        default_currencies = map(str.upper, default_currencies)
        default_currencies = list(default_currencies)
        service.set_default_currencies(default_currencies)

        service.set_api_key(event.preferences['api_key'])

        default_cities = TimezoneService.parse_default_cities(event.preferences['default_cities'])
        TimezoneService().set_default_cities(default_cities)

class PreferencesUpdateEventListener(EventListener):
    def on_event(self, event, extension):
        super().on_event(event, extension)
        
        service = CurrencyService()
        if event.id == 'cache':
            old_value = int(event.old_value)
            new_value = int(event.new_value)
            if old_value <= 0 and new_value > 0:
                service.enable_cache(new_value)
            elif old_value > 0 and new_value <= 0:
                service.disable_cache()
        elif event.id == 'default_currencies':
            default_currencies = event.new_value.split(',')
            default_currencies = map(str.strip, default_currencies)
            default_currencies = map(str.upper, default_currencies)
            default_currencies = list(default_currencies)
            service.set_default_currencies(default_currencies)
        elif event.id == 'api_key':
            service.set_api_key(event.new_value)
            if service.provider_had_error:
                service.get_rates()
        elif event.id == 'default_cities':
            default_cities = TimezoneService.parse_default_cities(event.new_value)
            TimezoneService().set_default_cities(default_cities)
        service.run()

if __name__ == '__main__':
    ConverterExtension().run()