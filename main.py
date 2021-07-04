from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from calculate_anything.currency.service import CurrencyService
from calculate_anything.query_handlers import QueryHandler

class ConverterExtension(Extension):

    def __init__(self):
        super(ConverterExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent, PreferencesUpdateEventListener())

class KeywordQueryEventListener(EventListener):
    def _no_match_item(self, name=None, description=None):
        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.svg',
                name=name or 'Keep typing your query ...',
                description=description or 'Try expressions like "10 euros to dollars", "sqrt(10) + 2 ^ 2.5", "20 cm to inches"',
                highlightable=False,
                on_enter=HideWindowAction()
            )
        ])

    def on_event(self, event, extension):
        items = []
        error_num = 0
        results = QueryHandler.get_instance().handle(event.get_argument() or '')
        for result in results:
            icon = result.get('icon', 'images/icon.svg')
            value = result['value']
            is_error = result['is_error']
            error_num += is_error
            name = result['name']
            description = result['description']

            if is_error:
                highlightable=False,
            else:
                highlightable=True,
            items.append(ExtensionResultItem(
                icon=icon,
                name=name,
                description=description,
                highlightable=highlightable,
                on_enter=CopyToClipboardAction(str(value))
            ))
        
        if len(items) == error_num:
            return self._no_match_item()

        return RenderResultListAction(items)

class PreferencesEventListener(EventListener):
    def on_event(self, event, extension):
        super().on_event(event, extension)
        cache_update = int(event.preferences['cache'])

        service = CurrencyService.get_instance()
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

class PreferencesUpdateEventListener(EventListener):
    def on_event(self, event, extension):
        super().on_event(event, extension)
        

        service = CurrencyService.get_instance()
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

if __name__ == '__main__':
    ConverterExtension().run()