from calculate_anything.logging_wrapper import LoggingWrapper as logging
from calculate_anything.lang import LanguageService
from calculate_anything.currency import CurrencyService
from calculate_anything.time import TimezoneService
from calculate_anything.units import UnitsService


def init():
    """Define correct sequence of initializing services"""
    UnitsService()
    CurrencyService()
    TimezoneService()
    LanguageService()
