from .logging_wrapper import LoggingWrapper as logging
from .lang import LanguageService
from .currency import CurrencyService
from .time import TimezoneService
from .units import UnitsService

def init():
    """Define correct sequence of initializing services"""
    UnitsService()
    CurrencyService()
    TimezoneService()
    LanguageService()

