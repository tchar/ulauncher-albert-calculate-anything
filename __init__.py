# -*- coding: utf-8 -*-
'''Converter for currency, units and calculator.

Current backends: fixer.io.

Synopsis: "10 dollars to eur, cad" "10 meters to inches" "10 + sqrt(2)" "cos(pi + 3i)"'''

################################### SETTINGS #######################################
# Below are the settings for this extension
# Currency provider: One of "internal", "fixerio")
CURRENCY_PROVIDER = 'internal'
# API Key is your fixer.io API key
API_KEY = ''
# Cache update interval in seconds (defaults to 1 day = 86400 seconds)
CACHE = 86400
# Default currencies to show when no target currency is provided
DEFAULT_CURRENCIES = 'USD,EUR,GBP,CAD'
# Default cities to show when converting timezones
DEFAULT_CITIES = 'New York City US, London GB, Madrid ES, Vancouver CA, Athens GR'
# Units conversion mode (normal or crazy)
UNITS_CONVERSION_MODE = 'normal'
# Set the following to True if you want to enable placeholder for empty results
SHOW_EMPTY_PLACEHOLDER = False
# Below line is the trigger keywords to your choice (put a space after your keyword)
# Order of triggers: 'Calculator, Time, Decimal, Hexadecimal, Binary, Octal
__triggers__ = ['=', 'time', 'dec', 'bin', 'hex', 'oct']
####################################################################################

__title__ = 'Calculate Anything'
__version__ = '0.0.1'
__authors__ = 'Tilemachos Charalampous'
__py_deps__ = ['requests', 'requests', 'pint', 'simpleeval', 'parsedatetime']


import locale  # noqa: E402
locale.setlocale(locale.LC_ALL, '')
import os  # noqa: E402
import sys  # noqa: E402
try:
    from calculate_anything.constants import MAIN_DIR  # noqa: E402
except ImportError as e:
    MAIN_DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(MAIN_DIR)

from calculate_anything import logging  # noqa: E402
from calculate_anything.preferences import Preferences  # noqa: E402
from calculate_anything.lang import LanguageService  # noqa: E402
from calculate_anything.time import TimezoneService  # noqa: E402
from calculate_anything.query import MultiHandler  # noqa: E402
from calculate_anything.query.handlers import (  # noqa: E402
    UnitsQueryHandler, CalculatorQueryHandler,
    PercentagesQueryHandler, TimeQueryHandler, Base10QueryHandler,
    Base2QueryHandler, Base8QueryHandler, Base16QueryHandler
)
from albert import ClipAction, Item, debug, info, warning, critical  # noqa: E402

# Thanks albert for making me hack the shit out of logging
handler = logging.CustomHandler(debug, info, warning, critical, critical)
handler.setFormatter(logging.ColorFormatter(
    fmt='[{BLUE}{{name}}.{{funcName}}:{{lineno}}{RESET}]: {{message}}',
    use_color=True
))
logging.set_stdout_handler(handler)

CURRENCY_PROVIDER = globals().get('CURRENCY_PROVIDER', '').lower()
API_KEY = globals().get('API_KEY') or ''
UNITS_CONVERSION_MODE = globals().get('UNITS_CONVERSION_MODE') or ''
CACHE = globals().get('CACHE') or 86400
TRIGGERS = globals().get('__triggers__') or []
if isinstance(TRIGGERS, str):
    TRIGGERS = [TRIGGERS]


def initialize():
    if not TRIGGERS:
        CalculatorQueryHandler.keyword = ''
        UnitsQueryHandler.keyword = ''
        PercentagesQueryHandler.keyword = ''

    preferences = Preferences()

    preferences.language.set('en_US')

    api_key = API_KEY or os.environ.get('CALCULATE_ANYTHING_API_KEY') or ''
    preferences.currency.add_provider(CURRENCY_PROVIDER, api_key)
    preferences.currency.set_cache_update_frequency(CACHE)
    preferences.currency.set_default_currencies(DEFAULT_CURRENCIES)

    preferences.units.set_conversion_mode(UNITS_CONVERSION_MODE)

    preferences.time.set_default_cities(DEFAULT_CITIES)
    preferences.commit()


def finalize():
    TimezoneService.stop()


def is_trigger(query, index):
    try:
        return TRIGGERS[index] == query.trigger
    except IndexError:
        return False


def is_calculator_trigger(query): return is_trigger(query, 0)
def is_time_trigger(query): return is_trigger(query, 1)
def is_dec_trigger(query): return is_trigger(query, 2)
def is_bin_trigger(query): return is_trigger(query, 3)
def is_hex_trigger(query): return is_trigger(query, 4)
def is_oct_trigger(query): return is_trigger(query, 5)


def handleQuery(query):
    if TRIGGERS and not query.isTriggered:
        return
    query_nokw = query.string
    query.disableSort()

    mode = 'calculator'
    if not TRIGGERS:
        handlers = []
        query_str = query_nokw
    elif is_time_trigger(query):
        query_str = TimeQueryHandler.keyword + query_nokw
        handlers = [TimeQueryHandler]
        mode = 'time'
    elif is_dec_trigger(query):
        query_str = Base10QueryHandler.keyword + query_nokw
        handlers = [Base10QueryHandler]
        mode = 'dec'
    elif is_hex_trigger(query):
        query_str = Base16QueryHandler.keyword + query_nokw
        handlers = [Base16QueryHandler]
        mode = 'hex'
    elif is_oct_trigger(query):
        query_str = Base8QueryHandler.keyword + query_nokw
        handlers = [Base8QueryHandler]
        mode = 'oct'
    elif is_bin_trigger(query):
        query_str = Base2QueryHandler.keyword + query_nokw
        handlers = [Base2QueryHandler]
        mode = 'bin'
    else:
        query_str = CalculatorQueryHandler().keyword + ' ' + query_nokw
        handlers = [
            CalculatorQueryHandler,
            PercentagesQueryHandler,
            UnitsQueryHandler
        ]

    items = []
    had_any_non_error = False
    results = MultiHandler.handle(query_str, *handlers)
    for result in results:
        had_any_non_error = had_any_non_error or result.error is not None
        icon = result.icon or 'images/icon.svg'
        icon = os.path.join(MAIN_DIR, icon)

        if result.clipboard is not None:
            actions = [ClipAction(text=result.clipboard,
                                  clipboardText=result.clipboard)]
        else:
            actions = []

        items.append(Item(
            id=__title__,
            icon=icon,
            text=result.name,
            subtext=result.description,
            actions=actions
        ))

    should_show_placeholder = query_nokw.strip() == '' and TRIGGERS or (
            not had_any_non_error and
            SHOW_EMPTY_PLACEHOLDER)

    if should_show_placeholder:
        items.append(
            Item(
                id=__title__,
                icon=os.path.join(MAIN_DIR, 'images/icon.svg'),
                text=LanguageService.translate('no-result', 'misc'),
                subtext=LanguageService.translate(
                    'no-result-{}-description'.format(mode), 'misc')
            )
        )
    if not items:
        return None

    return items
