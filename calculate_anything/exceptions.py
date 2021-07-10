class CurrencyException(Exception):
    pass

class CurrencyProviderException(CurrencyException):
    pass

class CurrencyProviderRequestException(CurrencyProviderException):
    pass

class UnitException(Exception):
    pass

class CalculatorException(Exception):
    pass

class ZeroDivisionException(CalculatorException):
    pass

class BooleanPercetageException(CalculatorException):
    pass

class BooleanException(Exception):
    pass

class BooleanComparisonException(BooleanException):
    pass

class TimeException(Exception):
    pass

class DateOverflowException(TimeException):
    pass

class MissingModuleException(Exception):
    pass

class MissingRequestsException(CurrencyException):
    pass

class MissingSimpleevalException(CalculatorException):
    pass

class MissingPintException(Exception):
    pass

class MissingParsedatetimeException(MissingModuleException):
    pass