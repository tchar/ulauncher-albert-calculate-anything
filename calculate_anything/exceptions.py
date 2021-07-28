'''All exceptions found in this module

All exceptions are subclass of ExtendedException
'''

from typing import Any, Optional


class ExtendedException(Exception):
    order = -10
    '''An extended Exception which apart from message
    holds extra information
    '''

    def __init__(self, message='', extra: Optional[Any] = None):
        '''Args:
            message (str): The message for this exception
            extra (any, optional): Any extra information to be kept
                and used later
        '''
        super().__init__(message)
        self.extra = extra


class CurrencyException(ExtendedException):
    order = -100
    pass


class CurrencyProviderException(CurrencyException):
    order = -110
    pass


# Exceptions for unit conversion


class UnitException(ExtendedException):
    order = -200
    pass

# Calculator exceptions


class CalculatorException(ExtendedException):
    order = -300
    pass


class ZeroDivisionException(CalculatorException):
    order = -310
    pass


class BooleanPercetageException(CalculatorException):
    order = -320
    pass


class WrongBaseException(CalculatorException):
    order = -330
    pass


class BaseFloatingPointException(CalculatorException):
    order = -340
    pass


class BooleanComparisonException(CalculatorException):
    order = -350
    pass

# Exceptions for Time conversion


class TimeException(ExtendedException):
    order = -400
    pass


class DateOverflowException(TimeException):
    order = -410
    pass


class MisparsedDateTimeException(TimeException):
    order = -420
    pass

# Exceptions for missing modules


class MissingModuleException(ExtendedException):
    order = -1000
    pass


class MissingPintException(MissingModuleException):
    order = -1100
    pass


class MissingSimpleevalException(MissingModuleException):
    order = -1200
    pass


class MissingParsedatetimeException(MissingModuleException):
    order = -1300
    pass
