# Exceptions for Currency conversion
class ExtendedException(Exception):
    def __init__(self, message='', extra=None):
        super().__init__(message)
        self.extra = extra

class CurrencyException(ExtendedException):
    pass

class CurrencyProviderException(CurrencyException):
    pass

class CurrencyProviderRequestException(CurrencyProviderException):
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

class DateAddDateException(TimeException):
    pass

class MisparsedTimeException(TimeException):
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