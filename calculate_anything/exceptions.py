'''All exceptions found in this module

All exceptions are subclass of ExtendedException
'''

from typing import Any, Optional


class ExtendedException(Exception):
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
    pass


class CurrencyProviderException(CurrencyException):
    order = -60
    pass


# Exceptions for unit conversion


class UnitException(ExtendedException):
    pass

# Calculator exceptions


class CalculatorException(ExtendedException):
    pass


class ZeroDivisionException(CalculatorException):
    order = -70
    pass


class BooleanPercetageException(CalculatorException):
    order = -20
    pass


class WrongBaseException(CalculatorException):
    order = -40
    pass


class BaseFloatingPointException(CalculatorException):
    order = -30
    pass

# Exceptions for boolean representation in calculator


class BooleanException(ExtendedException):
    pass


class BooleanComparisonException(BooleanException):
    order = -10
    pass

# Exceptions for Time conversion


class TimeException(ExtendedException):
    pass


class DateOverflowException(TimeException):
    order = -50
    pass


class MisparsedDateTimeException(TimeException):
    order = -80
    pass

# Exceptions for missing modules


class MissingModuleException(ExtendedException):
    pass


class MissingPintException(MissingModuleException):
    order = -1020
    pass


class MissingSimpleevalException(MissingModuleException):
    order = -1010
    pass


class MissingParsedatetimeException(MissingModuleException):
    order = -1000
    pass
