from functools import wraps
from .. import logging
from ..query.result import QueryResult
from ..lang import LanguageService
from ..exceptions import (
    BaseFloatingPointException, BooleanComparisonException, CurrencyProviderException,
    DateOverflowException, DateAddDateException, MisparsedTimeException, WrongBaseException, ZeroDivisionException,
    MissingSimpleevalException, MissingParsedatetimeException, MissingRequestsException,
    BooleanPercetageException, MissingPintException
)

def zero_division_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('infinite-result-error'),
        description=translator('infinite-result-error-description'),
        error=ZeroDivisionException
    )

def missing_simpleeval_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        clipboard='pip install simpleeval',
        name=translator('install-simpleeval'),
        description=translator('install-simpleeval-description'),
        error=MissingSimpleevalException,
        order=-1
    )

def missing_parsedatetime_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/time.svg',
        name=translator('install-parsedatetime'),
        description=translator('install-parsedatetime-description'),
        clipboard='pip install parsedatetime',
        error=MissingParsedatetimeException,
        order=-1
    )

def missing_requests_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/time.svg',
        name=translator('install-requests'),
        description=translator('install-requests-description'),
        clipboard='pip install requests',
        error=MissingRequestsException,
        order=-1
    )

def date_overflow_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/time.svg',
        name=translator('date-overflow'),
        description=translator('date-overflow-description'),
        clipboard='',
        order=0
    )

def date_add_date_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/time.svg',
        name=translator('date-add-date'),
        description=translator('date-add-date-description'),
        clipboard='',
        order=0
    )

def misparsed_time_exception(exception):
    translator = LanguageService().get_translator('errors')
    name = translator('unfully-parsed-date')
    name = '{}: "{}"'.format(name, exception.extra['parsed_query'])
    description = translator('unfully-parsed-date-description')
    description = '{}: "{}"'.format(description, exception.extra['original_query'])
    return QueryResult(
        icon='images/time.svg',
        name=name,
        description=description,
        clipboard='',
        order=0
    )

def currency_provider_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('provider-error'),
        description=translator('provider-error-description'),
        error=CurrencyProviderException,
    )

def boolean_comparison_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('boolean-comparison-error'),
        description=translator('boolean-comparison-error-description'),
        error=BooleanComparisonException
    )

def boolean_percentage_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('boolean-percentage-error'),
        description=translator('boolean-percentage-error-description'),
        error=BooleanPercetageException
    )

def wrong_base_exception_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('wrong-base-error'),
        description=translator('wrong-base-error-description'),
        error=BooleanPercetageException
    )

def base_floating_point_exception_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('base-floating-error'),
        description=translator('base-floating-error-description'),
        error=BaseFloatingPointException
    )

def missing_pint_error_query_result():
    translator = LanguageService().get_translator('errors')
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
                    return date_overflow_error_query_result()
                if self.is_error(DateAddDateException):
                    return date_add_date_query_result()
                if isinstance(self.error, MisparsedTimeException):
                    return misparsed_time_exception(self.error)
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