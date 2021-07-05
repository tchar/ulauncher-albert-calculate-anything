# -*- coding: utf-8 -*-
'''Converter for currency, units and calculator.

Current backends: fixer.io.

Synopsis: "10 dollars to eur, cad" "10 meters to inches" "10 + sqrt(2)" "cos(pi + 3i)"'''

################################### SETTINGS #######################################
# Below are the settings for this extension
# API Key is your fixer.io API key
API_KEY = ''
# Cache update interval in seconds (defaults to 1 day = 86400 seconds)
CACHE = 86400
# Default currencies to show when no target currency is provided
DEFAULT_CURRENCIES = 'USD,EUR,GBP,CAD'
# Uncomment below line to set a trigger keyword to your choice (put a space after your keyword)
# __triggers__ = 'calc '
####################################################################################

__title__ = 'Calculate Anything'
__version__ = '0.0.1'
__authors__ = 'Tilemachos Charalampous'

class AlbertLogger:
    def __init__(self, name):
        self._name = name

    def debug(self, message, *args):
        debug('{}: {}'.format(self._name, str(message) % args))

    def info(self, message, *args):
        info('{}: {}'.format(self._name, str(message) % args))

    def warning(self, message, *args):
        warning('{}: {}'.format(self._name, str(message) % args))

    def error(self, message, *args):
        critical('{}: {}'.format(self._name, str(message) % args))
    
class AlbertLogging:
    def getLogger(name=''):
        return AlbertLogger(name)

import os
import sys
try:
    from calculate_anything.constants import MAIN_DIR
except ImportError as e:
    MAIN_DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(MAIN_DIR)

from calculate_anything.logging_wrapper import LoggingWrapper as logging
logging.set_logging(AlbertLogging)
from calculate_anything.currency.service import CurrencyService
from calculate_anything.query_handlers import QueryHandler
from albert import ClipAction, Item, critical, debug, info, warning, critical

try:
    API_KEY = API_KEY or ''
    CACHE = int(CACHE)
except (ValueError, TypeError):
    CACHE = 86400

def initialize():
    service = CurrencyService.get_instance()
    service.set_api_key(API_KEY)
    if CACHE > 0:
        service.enable_cache(CACHE)
    else:
        service.disable_cache()
    default_currencies = DEFAULT_CURRENCIES.split(',')
    default_currencies = map(str.strip, default_currencies)
    default_currencies = map(str.upper, default_currencies)
    default_currencies = list(default_currencies)
    service.set_default_currencies(default_currencies)

def finalize():
    CurrencyService.get_instance().disable_cache()

def handleQuery(query):
    has_trigger = '__triggers__' in globals()
    if has_trigger and not query.isTriggered:
        return
    items = []
    error_num = 0
    results = QueryHandler.get_instance().handle(query.string.strip() or '')
    for result in results:
        error_num += result.is_error
        icon = result.icon or 'images/icon.svg'
        icon = os.path.join(MAIN_DIR, icon)
        value = str(result.value)
        actions = [ClipAction(text=value, clipboardText=value) if result.clipboard else None]
        items.append(Item(
            id=__title__,
            icon=icon,
            text=result.name,
            subtext=result.description,
            actions=actions
        ))
    if not items:
        return None
    return items