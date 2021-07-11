from functools import wraps
from ..logging_wrapper import LoggingWrapper as logging
from ..query.result import QueryResult
from ..lang import Language
from ..exceptions import (
    BaseFloatingPointException, BooleanComparisonException, CurrencyProviderException,
    DateOverflowException, WrongBaseException, ZeroDivisionException,
    MissingSimpleevalException, MissingParsedatetimeException, MissingRequestsException,
    BooleanPercetageException, MissingPintException
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

def currency_provider_error_query_result():
    return QueryResult(
        icon='images/icon.svg',
        name=Language().translate('provider-error', 'currency'),
        description=Language().translate('provider-error-description', 'currency'),
        error=CurrencyProviderException,
    )

def boolean_comparison_error_query_result():
    return QueryResult(
        icon='images/icon.svg',
        name=Language().translate('boolean-comparison-error', 'calculator'),
        description=Language().translate('boolean-comparison-error-description', 'calculator'),
        error=BooleanComparisonException
    )

def boolean_percentage_error_query_result():
    return QueryResult(
        icon='images/icon.svg',
        name=Language().translate('boolean-percentage-error', 'calculator'),
        description=Language().translate('boolean-percentage-error-description', 'calculator'),
        error=BooleanPercetageException
    )

def wrong_base_exception_query_result():
    return QueryResult(
        icon='images/icon.svg',
        name=Language().translate('wrong-base-error', 'calculator'),
        description=Language().translate('wrong-base-error-description', 'calculator'),
        error=BooleanPercetageException
    )

def base_floating_point_exception_query_result():
    return QueryResult(
        icon='images/icon.svg',
        name=Language().translate('base-floating-error', 'calculator'),
        description=Language().translate('base-floating-error-description', 'calculator'),
        error=BaseFloatingPointException
    )

def missing_pint_error_query_result():
    translator = Language().get_translator('units')
    return QueryResult(
        icon='images/convert.svg',
        name=translator('install-pint'),
        description=translator('install-pint-description'),
        clipboard='pip install pint',
        error=MissingPintException,
        order=-1
    )

class _Calculation:
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
                    return currency_provider_error_query_result()
                if self.is_error(BooleanComparisonException):
                    return boolean_comparison_error_query_result()
                if self.is_error(BooleanPercetageException):
                    return boolean_percentage_error_query_result()
                if self.is_error(WrongBaseException):
                    return wrong_base_exception_query_result()
                if self.is_error(BaseFloatingPointException):
                    return base_floating_point_exception_query_result()
                if self.is_error(MissingPintException):
                    return missing_pint_error_query_result()
                if self.is_error():
                    self._logger.error('Uknown error type: {}'.format(self.error))
                    raise self.error
                return func(self, *args, **kwargs)
            return _wrapper

    def __init__(self, value=None, query='', error=None, order=-1):
        self.value = value
        self.query = query
        self.error = error
        self.order = order
        self._logger = logging.getLogger(__name__)

    def is_error(self, _type=None):
        if _type is None:
            return self.error is not None
        return self.error == _type

    def to_query_result(self):
        pass