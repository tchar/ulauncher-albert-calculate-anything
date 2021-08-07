'''All exceptions found in this module

All exceptions are subclass of ExtendedException
'''

from typing import Any, Optional


class ExtendedException(Exception):
    order = -10
    '''An extended Exception which apart from message
    holds extra information
    '''

    def __init__(self, message: str = '', extra: Optional[Any] = None) -> None:
        '''Args:
        message (str): The message for this exception
        extra (any, optional): Any extra information to be kept
            and used later
        '''
        super().__init__(message)
        self.extra = extra or {}


class CurrencyException(ExtendedException):
    order = -100


class CurrencyProviderException(CurrencyException):
    order = -110


# Exceptions for unit conversion


class UnitException(ExtendedException):
    order = -200


# Calculator exceptions


class CalculatorException(ExtendedException):
    order = -300


class ZeroDivisionException(CalculatorException):
    order = -310


class BooleanPercetageException(CalculatorException):
    order = -320


class WrongBaseException(CalculatorException):
    order = -330


class BaseFloatingPointException(CalculatorException):
    order = -340


class BooleanComparisonException(CalculatorException):
    order = -350


# Exceptions for Time conversion


class TimeException(ExtendedException):
    order = -400


class DateOverflowException(TimeException):
    order = -410


class MisparsedDateTimeException(TimeException):
    order = -420


# Exceptions for missing modules


class MissingModuleException(ExtendedException):
    order = -1000


class MissingPintException(MissingModuleException):
    order = -1100


class MissingSimpleevalException(MissingModuleException):
    order = -1200


class MissingParsedatetimeException(MissingModuleException):
    order = -1300
