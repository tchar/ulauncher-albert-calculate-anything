from functools import wraps
from abc import abstractmethod
from calculate_anything import logging
from calculate_anything.query.result import QueryResult
from calculate_anything.lang import LanguageService
from calculate_anything.exceptions import (
    BaseFloatingPointException, BooleanComparisonException,
    CurrencyProviderException, DateOverflowException,
    MisparsedDateTimeException, WrongBaseException, ZeroDivisionException,
    MissingSimpleevalException, MissingParsedatetimeException,
    BooleanPercetageException, MissingPintException
)

# TODO: Fix this mess


def missing_parsedatetime_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/time.svg',
        name=translator('missing-parsedatetime-error'),
        description=translator('missing-parsedatetime-error-description'),
        clipboard='pip install parsedatetime',
        error=MissingParsedatetimeException,
        order=-1000
    )


def missing_simpleeval_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('missing-simpleeval-error'),
        description=translator('missing-simpleeval-error-description'),
        clipboard='pip install simpleeval',
        error=MissingSimpleevalException,
        order=-1010
    )


def missing_pint_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/convert.svg',
        name=translator('missing-pint-error'),
        description=translator('missing-pint-error-description'),
        clipboard='pip install Pint',
        error=MissingPintException,
        order=-1020
    )


def boolean_comparison_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('boolean-comparison-error'),
        description=translator('boolean-comparison-error-description'),
        clipboard='',
        error=BooleanComparisonException,
        order=-10
    )


def boolean_percentage_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('boolean-percentage-error'),
        description=translator('boolean-percentage-error-description'),
        clipboard='',
        error=BooleanPercetageException,
        order=-20
    )


def base_floating_point_exception_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('base-floating-error'),
        description=translator('base-floating-error-description'),
        clipboard='',
        error=BaseFloatingPointException,
        order=-30
    )


def wrong_base_exception_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('wrong-base-error'),
        description=translator('wrong-base-error-description'),
        clipboard='',
        error=WrongBaseException,
        order=-40
    )


def date_overflow_error_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/time.svg',
        name=translator('date-overflow'),
        description=translator('date-overflow-description'),
        clipboard='',
        error=DateOverflowException,
        order=-50
    )


def currency_provider_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('currency-provider-error'),
        description=translator('currency-provider-error-description'),
        clipboard='',
        error=CurrencyProviderException,
        order=-60
    )


def zero_division_error_query_result():
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('zero-division-error'),
        description=translator('zero-division-error-description'),
        clipboard='',
        error=ZeroDivisionException,
        order=-70
    )


def misparsed_time_exception(calculation):
    translator = LanguageService().get_translator('errors')
    name = translator('misparsed-datetime')
    name = '{}: "{}"'.format(name, calculation.error.extra['parsed_query'])
    description = translator('misparsed-datetime-description')
    description = '{}: "{}"'.format(
        description, calculation.error.extra['original_query'])
    return QueryResult(
        icon='images/time.svg',
        name=name,
        description=description,
        clipboard='',
        error=MisparsedDateTimeException,
        order=-80
    )


class _Calculation:
    class Decorators:
        def handle_error_results(func):
            @wraps(func)
            def _wrapper(self, *args, **kwargs):
                if self.is_error(MissingPintException):
                    return missing_pint_error_query_result()
                if self.is_error(MissingSimpleevalException):
                    return missing_simpleeval_query_result()
                if self.is_error(MissingParsedatetimeException):
                    return missing_parsedatetime_query_result()
                if self.is_error(ZeroDivisionException):
                    return zero_division_error_query_result()
                if self.is_error(DateOverflowException):
                    return date_overflow_error_query_result(self)
                if isinstance(self.error, MisparsedDateTimeException):
                    return misparsed_time_exception(self)
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
                if self.is_error():
                    self._logger.exception(  # pragma: no cover (just in case)
                        'Uknown error type: {}'.format(self.error))
                    raise self.error  # pragma: no cover
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

    @abstractmethod
    def to_query_result(self):
        pass  # pragma: no cover
