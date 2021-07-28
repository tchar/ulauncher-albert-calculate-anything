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
    pass


# Exceptions for unit conversion


class UnitException(ExtendedException):
    pass

# Calculator exceptions


class CalculatorException(ExtendedException):
    pass


class ZeroDivisionException(CalculatorException):
    pass


class BooleanPercetageException(CalculatorException):
    pass


class WrongBaseException(CalculatorException):
    pass


class BaseFloatingPointException(CalculatorException):
    pass

# Exceptions for boolean representation in calculator


class BooleanException(ExtendedException):
    pass


class BooleanComparisonException(BooleanException):
    pass

# Exceptions for Time conversion


class TimeException(ExtendedException):
    pass


class DateOverflowException(TimeException):
    pass


class MisparsedDateTimeException(TimeException):
    pass

# Exceptions for missing modules


class MissingModuleException(ExtendedException):
    pass


class MissingRequestsException(MissingModuleException):
    pass


class MissingSimpleevalException(MissingModuleException):
    pass


class MissingPintException(MissingModuleException):
    pass


class MissingParsedatetimeException(MissingModuleException):
    pass
