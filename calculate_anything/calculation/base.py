from functools import wraps
from ..query.result import QueryResult
from ..lang import Language
from ..exceptions import (
    CurrencyProviderException, DateOverflowException, ZeroDivisionException,
    MissingSimpleevalException, MissingParsedatetimeException, MissingRequestsException
)

def zero_division_error_query_result():
    return QueryResult(
        icon='images/icon.svg',
        name=Language().translate('infinite-result', 'calculator'),
        description=Language().translate('infinite-result-description', 'calculator'),
        error=ZeroDivisionException
    )

def missing_simpleeval_query_result():
    return QueryResult(
        icon='images/icon.svg',
        clipboard='pip install simpleeval',
        name=Language().translate('install-simpleeval', 'calculator'),
        description=Language().translate('install-simpleeval-description', 'calculator'),
        error=MissingSimpleevalException
    )

def missing_parsedatetime_query_result():
    return QueryResult(
        icon='images/time.svg',
        name=Language().translate('install-parsedatetime', 'time'),
        description=Language().translate('install-parsedatetime-description', 'time'),
        clipboard='pip install parsedatetime',
        error=MissingParsedatetimeException,
        order=-1
    )

def missing_requests_query_result():
    return QueryResult(
        icon='images/time.svg',
        name=Language().translate('install-requests', 'currency'),
        description=Language().translate('install-requests-description', 'currency'),
        clipboard='pip install requests',
        error=MissingRequestsException,
        order=-1
    )

def date_overflow_query_result():
    return QueryResult(
        icon='images/time.svg',
        name=Language().translate('years-overflow', 'time'),
        description=Language().translate('years-overflow-description', 'time'),
        clipboard='',
        order=0
    )

def currency_provider_error():
    return QueryResult(
        icon='images/icon.svg',
        name=Language().translate('provider-error', 'currency'),
        description=Language().translate('provider-error-description', 'currency'),
        error=CurrencyProviderException,
    )

class BaseCalculation:
    class Decorators:
        def handle_error_results(func):
            @wraps(func)
            def _wrapper(self, *args, **kwargs):
                if self.is_error(ZeroDivisionException):
                    return zero_division_error_query_result()
                if self.is_error(MissingSimpleevalException):
                    return missing_simpleeval_query_result()
                if self.is_error(MissingParsedatetimeException):
                    return missing_simpleeval_query_result()
                if self.is_error(MissingRequestsException):
                    return missing_requests_query_result()
                if self.is_error(DateOverflowException):
                    return date_overflow_query_result()
                if self.is_error(CurrencyProviderException):
                    return currency_provider_error()
                if self.is_error():
                    raise self._error('Uknown error type: {}'.format(self.error))
                return func(self, *args, **kwargs)
            return _wrapper

    def __init__(self, value=None, error=None, order=-1):
        self.value = value
        self.error = error
        self.order = order

    def is_error(self, _type=None):
        if _type is None:
            return self.error is not None
        return self.error == _type

    def to_query_result(self):
        pass