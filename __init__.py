# -*- coding: utf-8 -*-
'''Converter for currency, units and calculator.

Current backends: fixer.io.

Synopsis: "10 dollars to eur, cad" "10 meters to inches" "10 + sqrt(2)" "cos(pi + 3i)"'''

################################### SETTINGS #######################################
# Below are the settings for this extension
# Currency provider: One of "fixerio", "ecb (European Central Bank)
CURRENCY_PROVIDER='fixerio'
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
__py_deps__ = ['requests', 'requests', 'pint' ,'simpleeval', 'parsedatetime']

class AlbertLogger:
    def __init__(self, name):
        self._name = name

    def _log(self, func, message, *args):
        message = str(message)
        if args:
            message = message % args
        message = '{}: {}'.format(self._name, message)
        func(message)

    def debug(self, message, *args):
        self._log(debug, message, *args)

    def info(self, message, *args):
        self._log(info, message, *args)

    def warning(self, message, *args):
        self._log(warning, message, *args)

    def error(self, message, *args):
        self._log(critical, message, *args)
    
class AlbertLogging:
    def getLogger(name=''):
        return AlbertLogger(name)

import locale
locale.setlocale(locale.LC_ALL, '')
import os
import sys
try:
    from calculate_anything.constants import MAIN_DIR
except ImportError as e:
    MAIN_DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(MAIN_DIR)

from calculate_anything import logging
logging.set_logging(AlbertLogging)
from calculate_anything.currency.service import CurrencyService
from calculate_anything.currency.providers import CurrencyProviderFactory
from calculate_anything.units.service import UnitsService
from calculate_anything.time.service import TimezoneService
from calculate_anything.query.handlers import (
    UnitsQueryHandler, CalculatorQueryHandler, CurrencyQueryHandler,
    PercentagesQueryHandler, TimeQueryHandler, Base10QueryHandler,
    Base2QueryHandler, Base8QueryHandler, Base16QueryHandler
)
from calculate_anything.query import QueryHandler
from calculate_anything.lang import Language
from calculate_anything.utils import get_or_default
from albert import ClipAction, Item, critical, debug, info, warning, critical

CURRENCY_PROVIDER = globals().get('CURRENCY_PROVIDER', '').lower()
CURRENCY_PROVIDER = get_or_default(CURRENCY_PROVIDER, str, 'ecb', ['fixerio', 'ecb'])

API_KEY = globals().get('API_KEY') or ''

UNITS_CONVERSION_MODE = globals().get('UNITS_CONVERSION_MODE') or ''
UNITS_CONVERSION_MODE = get_or_default(
    UNITS_CONVERSION_MODE.lower(),
    str, 'normal', ['normal', 'crazy']
)
if UNITS_CONVERSION_MODE == 'normal':
    UNITS_CONVERSION_MODE = UnitsService.MODE_NORMAL
elif UNITS_CONVERSION_MODE == 'crazy':
    UNITS_CONVERSION_MODE = 'crazy'

CACHE = globals().get('CACHE') or '86400'
CACHE = get_or_default(CACHE, int, 86400)

TRIGGERS = globals().get('__triggers__') or []
if isinstance(TRIGGERS, str):
    TRIGGERS = [TRIGGERS]

def initialize():
    currency_service = CurrencyService()
    units_service = UnitsService()

    currency_service.set_provider(CurrencyProviderFactory.get_provider(CURRENCY_PROVIDER))
    api_key = API_KEY or os.environ.get('CALCULATE_ANYTHING_API_KEY') or ''
    currency_service.set_api_key(api_key)
    if CACHE > 0:
        currency_service.enable_cache(CACHE)
    else:
        currency_service.disable_cache()
    default_currencies = DEFAULT_CURRENCIES.split(',')
    default_currencies = map(str.strip, default_currencies)
    default_currencies = map(str.upper, default_currencies)
    default_currencies = list(default_currencies)
    currency_service.set_default_currencies(default_currencies)

    units_service.set_unit_conversion_mode(UNITS_CONVERSION_MODE)

    default_cities = TimezoneService.parse_default_cities(DEFAULT_CITIES)
    TimezoneService().set_default_cities(default_cities)

    units_service.enable().run()
    currency_service.enable().run()

def finalize():
    UnitsService().disable().stop()
    CurrencyService().disable_cache()

def is_trigger(query, index):
    try: return TRIGGERS[index] == query.trigger
    except IndexError: return False

is_calculator_trigger = lambda query: is_trigger(query, 0)
is_time_trigger = lambda query: is_trigger(query, 1)
is_dec_trigger = lambda query: is_trigger(query, 2)
is_bin_trigger = lambda query: is_trigger(query, 3)
is_hex_trigger = lambda query: is_trigger(query, 4)
is_oct_trigger = lambda query: is_trigger(query, 5)

def handleQuery(query):
    if TRIGGERS and not query.isTriggered:
        return
    query_str = query.string
    query.disableSort()
    items = []
    errors_num = 0

    mode = 'calculator'
    if not TRIGGERS:
        handlers = []
    elif is_time_trigger(query):
        query_str = 'time ' + query_str
        handlers = [TimeQueryHandler]
        mode = 'time'
    elif is_dec_trigger(query):
        handlers = [Base10QueryHandler]
        mode = 'dec'
    elif is_hex_trigger(query):
        handlers = [Base16QueryHandler]
        mode = 'hex'
    elif is_oct_trigger(query):
        handlers = [Base8QueryHandler]
        mode = 'oct'
    elif is_bin_trigger(query):
        handlers = [Base2QueryHandler]
        mode = 'bin'
    else:
        handlers = [
            CalculatorQueryHandler,
            PercentagesQueryHandler,
            UnitsQueryHandler,
            CurrencyQueryHandler,
        ]
    results = QueryHandler().handle(query_str, *handlers)
    for result in results:

        errors_num += result.error is not None
        icon = result.icon or 'images/icon.svg'
        icon = os.path.join(MAIN_DIR, icon)

        if result.clipboard is not None:
            actions = [ClipAction(text=result.clipboard, clipboardText=result.clipboard)]
        else:
            actions = []

        items.append(Item(
            id=__title__,
            icon=icon,
            text=result.name,
            subtext=result.description,
            actions=actions
        ))
    
    should_show_placeholder = (
        query_str == '' or (
            SHOW_EMPTY_PLACEHOLDER and (
                TRIGGERS or query_str
            ) and len(items) == errors_num
        )
    )
    if should_show_placeholder:
        items.append(
            Item(
                id=__title__,
                icon=os.path.join(MAIN_DIR, 'images/icon.svg'),
                text=Language().translate('no-result', 'misc'),
                subtext=Language().translate('no-result-{}-description'.format(mode), 'misc')
            )
        )
    if not items:
        return None
    return items
