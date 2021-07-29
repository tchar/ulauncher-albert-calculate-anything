from functools import wraps
from abc import abstractmethod
from calculate_anything import logging
from calculate_anything.query.result import QueryResult
from calculate_anything.lang import LanguageService
from calculate_anything.exceptions import (
    BaseFloatingPointException, BooleanComparisonException,
    CurrencyProviderException, DateOverflowException, ExtendedException,
    MisparsedDateTimeException, WrongBaseException, ZeroDivisionException,
    MissingSimpleevalException, MissingParsedatetimeException,
    BooleanPercetageException, MissingPintException
)


def missing_parsedatetime_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/time.svg',
        name=translator('missing-parsedatetime-error'),
        description=translator('missing-parsedatetime-error-description'),
        clipboard='pip install parsedatetime',
        error=calculation.error,
        order=calculation.error.order
    )


def missing_simpleeval_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('missing-simpleeval-error'),
        description=translator('missing-simpleeval-error-description'),
        clipboard='pip install simpleeval',
        error=calculation.error,
        order=calculation.error.order
    )


def missing_pint_error_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/convert.svg',
        name=translator('missing-pint-error'),
        description=translator('missing-pint-error-description'),
        clipboard='pip install Pint',
        error=calculation.error,
        order=calculation.error.order
    )


def boolean_comparison_error_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('boolean-comparison-error'),
        description=translator('boolean-comparison-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.error.order
    )


def boolean_percentage_error_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('boolean-percentage-error'),
        description=translator('boolean-percentage-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.error.order
    )


def base_floating_point_exception_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('base-floating-error'),
        description=translator('base-floating-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.error.order
    )


def wrong_base_exception_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('wrong-base-error'),
        description=translator('wrong-base-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.error.order
    )


def date_overflow_error_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/time.svg',
        name=translator('date-overflow'),
        description=translator('date-overflow-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.error.order
    )


def currency_provider_error_query_result(calculation):
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon='images/icon.svg',
        name=translator('currency-provider-error'),
        description=translator('currency-provider-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.error.order
    )


def zero_division_error_query_result(calculation):
    icon = 'images/icon.svg'
    if calculation.error.extra is not None:
        icon = calculation.error.extra.get('icon', icon)
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('zero-division-error'),
        description=translator('zero-division-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.error.order
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
        error=calculation.error,
        order=calculation.error.order
    )


_HANDLERS = {
    MissingPintException: missing_pint_error_query_result,
    MissingSimpleevalException: missing_simpleeval_query_result,
    MissingParsedatetimeException: missing_parsedatetime_query_result,
    ZeroDivisionException: zero_division_error_query_result,
    DateOverflowException: date_overflow_error_query_result,
    MisparsedDateTimeException: misparsed_time_exception,
    CurrencyProviderException: currency_provider_error_query_result,
    BooleanComparisonException: boolean_comparison_error_query_result,
    BooleanPercetageException: boolean_percentage_error_query_result,
    WrongBaseException: wrong_base_exception_query_result,
    BaseFloatingPointException: base_floating_point_exception_query_result
}


class _Calculation:
    class Decorators:
        def handle_error_results(func):
            @wraps(func)
            def _wrapper(self, *args, **kwargs):
                if isinstance(self.error, ExtendedException):
                    return _HANDLERS[self.error.__class__](self)
                if self.is_error():
                    self._logger.exception(  # pragma: no cover (just in case)
                        'Uknown error type: {}'.format(self.error))
                    raise self.error  # pragma: no cover
                return func(self, *args, **kwargs)
            return _wrapper

    def __init__(self, value=None, query='', error=None, order=0):
        self.value = value
        self.query = query
        self.error = error
        self.order = order if not error else error.order
        self._logger = logging.getLogger(__name__)

    def is_error(self, _type=None):
        if _type is None:
            return self.error is not None
        return self.error == _type

    @abstractmethod
    def to_query_result(self):
        pass  # pragma: no cover
