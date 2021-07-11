# Exceptions for Currency conversion

class CurrencyException(Exception):
    pass

class CurrencyProviderException(CurrencyException):
    pass

class CurrencyProviderRequestException(CurrencyProviderException):
    pass

# Exceptions for unit conversion

class UnitException(Exception):
    pass

# Calculator exceptions

class CalculatorException(Exception):
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

class BooleanException(Exception):
    pass

class BooleanComparisonException(BooleanException):
    pass

# Exceptions for Time conversion

class TimeException(Exception):
    pass

class DateOverflowException(TimeException):
    pass

# Exceptions for missing modules

class MissingModuleException(Exception):
    pass

class MissingRequestsException(MissingModuleException):
    pass

class MissingSimpleevalException(MissingModuleException):
    pass

class MissingPintException(MissingModuleException):
    pass

class MissingParsedatetimeException(MissingModuleException):
    pass