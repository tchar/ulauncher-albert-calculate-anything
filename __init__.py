from abc import abstractmethod
from albert import (
    GeneratorQueryHandler,
    PluginInstance,
    StandardItem,
    Action,
    Icon,
    setClipboardText,
    # debug,
    # info,
    # warning,
    # critical,
)

md_iid = '5.0'
md_version = '0.2'
md_name = 'Calculate Anything'
md_description = 'A ULauncher/Albert extension that supports currency, units '
'and date time conversion, as well as a calculator that supports complex '
'numbers and functions.'
md_license = 'MIT'
md_url = 'https://github.com/tchar/ulauncher-albert-calculate-anything'
md_authors = ['@tchar']
md_bin_dependencies = []

import os
import sys
import locale

try:
    from calculate_anything.constants import MAIN_DIR
except ImportError:
    MAIN_DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(MAIN_DIR)

from calculate_anything.lang import LanguageService
from calculate_anything.query.handlers import MultiHandler
from calculate_anything.query.handlers import (
    UnitsQueryHandler,
    CalculatorQueryHandler,
    PercentagesQueryHandler,
    TimeQueryHandler,
    Base10QueryHandler,
    Base2QueryHandler,
    Base8QueryHandler,
    Base16QueryHandler,
)
from calculate_anything.utils import images_dir


class _BaseCalculateQueryHandler(GeneratorQueryHandler):
    """
    Shared base for all Calculate Anything query handlers.

    Subclasses must implement all abstractmethod / properties.
    """

    def __init__(self, show_empty_placeholder: bool):
        GeneratorQueryHandler.__init__(self)
        self.show_empty_placeholder = show_empty_placeholder
        # Resolve once at construction on the main thread — avoids
        # re-instantiating ca-handlers on every keystroke from the
        # background query thread.
        self._query_prefix  = self.query_prefix
        self._ca_handlers   = self.ca_handlers
        self._multi_handler = MultiHandler()

    @property
    @abstractmethod
    def mode(self) -> str:
        """Used for calculate_anything LanguageService translation key."""
        ...

    @property
    @abstractmethod
    def ca_handlers(self) -> list:
        """List of calculate_anything handler classes to be used in MultiHandler."""
        ...

    @property
    @abstractmethod
    def query_prefix(self) -> str:
        """Prefix to be prepended to context.query to form the internal query string."""
        ...

    def id(self) -> str:
        return f'{md_name}/{self.mode}'

    def name(self) -> str:
        return f'{md_name} ({self.mode.capitalize()})'

    def description(self) -> str:
        return f'{md_description} [{self.mode}]'

    def items(self, context):
        query_str = self._query_prefix + context.query

        batch = []
        results = self._multi_handler.handle(query_str, *self._ca_handlers)
        for result in results:
            icon_path = result.icon or images_dir('icon.svg')
            icon_path = os.path.join(MAIN_DIR, icon_path)

            actions = []
            if result.clipboard is not None:
                actions = [
                    Action(
                        'clipboard',
                        'Copy to clipboard',
                        lambda c=result.clipboard: setClipboardText(c),
                    )
                ]

            batch.append(
                StandardItem(
                    id=f"{self.id()}/{result.name}",
                    icon_factory=lambda p=icon_path: Icon.image(p),
                    text=result.name,
                    subtext=result.description,
                    actions=actions,
                )
            )

        should_show_placeholder = (
            context.query.strip() == '' or len(batch) == 0
        ) and self.show_empty_placeholder

        if should_show_placeholder:
            icon_path = os.path.join(MAIN_DIR, images_dir('icon.svg'))
            batch.append(
                StandardItem(
                    id=f"{self.id()}/placeholder",
                    icon_factory=lambda path=icon_path: Icon.image(path),
                    text=LanguageService().translate('no-result', 'misc'),
                    subtext=LanguageService().translate(
                        'no-result-{}-description'.format(self.mode), 'misc'
                    ),
                )
            )

        yield batch


class _CalculatorHandler(_BaseCalculateQueryHandler):
    def defaultTrigger(self): return '= '

    @property
    def mode(self): return 'calculator'

    @property
    def ca_handlers(self): return [UnitsQueryHandler(), CalculatorQueryHandler(), PercentagesQueryHandler()]

    @property
    def query_prefix(self): return CalculatorQueryHandler().keyword + ' '


class _TimeHandler(_BaseCalculateQueryHandler):
    def defaultTrigger(self): return 'time '

    @property
    def mode(self): return 'time'

    @property
    def ca_handlers(self): return [TimeQueryHandler()]

    @property
    def query_prefix(self): return TimeQueryHandler().keyword


class _DecHandler(_BaseCalculateQueryHandler):
    def defaultTrigger(self): return 'dec '

    @property
    def mode(self): return 'dec'

    @property
    def ca_handlers(self): return [Base10QueryHandler()]

    @property
    def query_prefix(self): return Base10QueryHandler().keyword


class _BinHandler(_BaseCalculateQueryHandler):
    def defaultTrigger(self): return 'bin '

    @property
    def mode(self): return 'bin'

    @property
    def ca_handlers(self): return [Base2QueryHandler()]

    @property
    def query_prefix(self): return Base2QueryHandler().keyword


class _HexHandler(_BaseCalculateQueryHandler):
    def defaultTrigger(self): return 'hex '

    @property
    def mode(self): return 'hex'

    @property
    def ca_handlers(self): return [Base16QueryHandler()]

    @property
    def query_prefix(self): return Base16QueryHandler().keyword


class _OctHandler(_BaseCalculateQueryHandler):
    def defaultTrigger(self): return 'oct '

    @property
    def mode(self): return 'oct'

    @property
    def ca_handlers(self): return [Base8QueryHandler()]

    @property
    def query_prefix(self): return Base8QueryHandler().keyword


class Plugin(PluginInstance):

    DEFAULT_SETTINGS = {
        'currency_provider': 'internal',
        'api_key': '',
        'cache': 86400,
        'default_currencies': 'USD,EUR,GBP,CAD',
        'default_cities': 'New York City US, London GB, Madrid ES, Vancouver CA, Athens GR',
        'units_conversion_mode': 'normal',
        'show_empty_placeholder': False,
        'language': locale.getlocale()[0],
    }

    def __init__(self):
        PluginInstance.__init__(self)

        # initialize settings with defaults if they don't exist
        for setting, default in self.DEFAULT_SETTINGS.items():
            if self.readConfig(setting, type(default)) is None:
                self.writeConfig(setting, default)

        self._apply_preferences()
        self._handlers = [
            _CalculatorHandler(self.show_empty_placeholder),
            _TimeHandler(self.show_empty_placeholder),
            _DecHandler(self.show_empty_placeholder),
            _BinHandler(self.show_empty_placeholder),
            _HexHandler(self.show_empty_placeholder),
            _OctHandler(self.show_empty_placeholder),
        ]

    # ------------------------------------------------------------------ config properties

    @property
    def currency_provider(self) -> str:
        return self.readConfig('currency_provider', str)

    @currency_provider.setter
    def currency_provider(self, value: str):
        self.writeConfig('currency_provider', value)
        self._apply_preferences()

    @property
    def api_key(self) -> str:
        return self.readConfig('api_key', str)

    @api_key.setter
    def api_key(self, value: str):
        self.writeConfig('api_key', value)
        self._apply_preferences()

    @property
    def cache(self) -> int:
        return self.readConfig('cache', int)

    @cache.setter
    def cache(self, value: int):
        self.writeConfig('cache', value)
        self._apply_preferences()

    @property
    def default_currencies(self) -> str:
        return self.readConfig('default_currencies', str)

    @default_currencies.setter
    def default_currencies(self, value: str):
        self.writeConfig('default_currencies', value)
        self._apply_preferences()

    @property
    def default_cities(self) -> str:
        return self.readConfig('default_cities', str)

    @default_cities.setter
    def default_cities(self, value: str):
        self.writeConfig('default_cities', value)
        self._apply_preferences()

    @property
    def units_conversion_mode(self) -> str:
        return self.readConfig('units_conversion_mode', str)

    @units_conversion_mode.setter
    def units_conversion_mode(self, value: str):
        self.writeConfig('units_conversion_mode', value)
        self._apply_preferences()

    @property
    def show_empty_placeholder(self) -> bool:
        return self.readConfig('show_empty_placeholder', bool)

    @show_empty_placeholder.setter
    def show_empty_placeholder(self, value: bool):
        self.writeConfig('show_empty_placeholder', value)
        for handler in self._handlers:
            handler.show_empty_placeholder = value

    @property
    def language(self) -> str:
        return self.readConfig('language', str)

    @language.setter
    def language(self, value: str):
        self.writeConfig('language', value)
        self._apply_preferences()

    # ------------------------------------------------------------------ albert config widget

    def configWidget(self):
        return [
            {
                'type': 'combobox',
                'label': 'Currency provider',
                'property': 'currency_provider',
                'items': ['internal', 'fixerio'],
            },
            {
                'type': 'lineedit',
                'label': 'Fixer.io API key',
                'property': 'api_key',
                'widget_properties': {'placeholderText': 'Required for fixerio provider'},
            },
            {
                'type': 'spinbox',
                'label': 'Currency cache (seconds)',
                'property': 'cache',
                'widget_properties': {'minimum': 0, 'maximum': 604800},
            },
            {
                'type': 'lineedit',
                'label': 'Default currencies',
                'property': 'default_currencies',
                'widget_properties': {'placeholderText': 'e.g. USD,EUR,GBP,CAD'},
            },
            {
                'type': 'lineedit',
                'label': 'Default cities',
                'property': 'default_cities',
                'widget_properties': {'placeholderText': 'e.g. New York City US, London GB'},
            },
            {
                'type': 'lineedit',
                'label': 'Language',
                'property': 'language',
                'widget_properties': {'placeholderText': 'e.g. en_US, de_DE'},
            },
            {
                'type': 'combobox',
                'label': 'Units conversion mode',
                'property': 'units_conversion_mode',
                'items': ['normal', 'crazy'],
            },
            {
                'type': 'checkbox',
                'label': 'Show placeholder on empty results',
                'property': 'show_empty_placeholder',
            },
        ]

    # ------------------------------------------------------------------ internal

    def _apply_preferences(self):
        from calculate_anything.preferences import Preferences

        api_key = self.api_key or os.environ.get('CALCULATE_ANYTHING_API_KEY') or ''

        # preferences.language.set() expects the CLDR short form e.g. 'en_US'.
        # Validate the user-configured value by checking whether calculate_anything
        # has a translation file for it; fall back to the system locale otherwise.
        def _lang_file_exists(lang: str) -> bool:
            path = os.path.join(MAIN_DIR, 'data', 'lang', f'{lang}.json')
            return os.path.isfile(path)

        configured = self.language.split('.')[0] if self.language else ''  # strip encoding
        system_lang = locale.getlocale()[0]
        lang_cldr = system_lang

        if configured and _lang_file_exists(configured):
            lang_cldr = configured
        else:
            warning("Could not find translation file for language '{}'; falling back to system locale '{}'.".format(configured, system_lang))

        preferences = Preferences()
        preferences.language.set(lang_cldr)
        preferences.currency.add_provider(self.currency_provider, api_key)
        preferences.currency.set_cache_update_frequency(self.cache)
        preferences.currency.set_default_currencies(self.default_currencies)
        preferences.units.set_conversion_mode(self.units_conversion_mode)
        preferences.time.set_default_cities(self.default_cities)
        preferences.commit()

        # parsedatetime has its own independent locale system — it must be
        # told the locale explicitly. Neither locale.setlocale() nor
        # LanguageService propagate into it.
        TimeQueryHandler.LOCALE_ID = lang_cldr

    def extensions(self):
        return self._handlers