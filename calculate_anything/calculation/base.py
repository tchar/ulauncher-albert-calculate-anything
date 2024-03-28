from abc import ABC, abstractmethod
import cmath
from enum import Enum

try:
    import pint
except ImportError:
    pint = None
from datetime import datetime, timedelta
from typing import Any, Callable, Dict, Tuple, Type, Union
from calculate_anything import logging
from calculate_anything.query.result import QueryResult
from calculate_anything.lang import LanguageService
from calculate_anything.utils import images_dir
from calculate_anything.exceptions import (
    BaseFloatingPointException,
    BooleanComparisonException,
    CurrencyProviderException,
    DateOverflowException,
    ExtendedException,
    MisparsedDateTimeException,
    WrongBaseException,
    ZeroDivisionException,
    MissingSimpleevalException,
    MissingParsedatetimeException,
    BooleanPercetageException,
    MissingPintException,
)
from calculate_anything.constants import CALCULATOR_ERROR

logger = logging.getLogger(__name__)

CalculationValue = Union[
    None,
    complex,
    float,
    int,
    bool,
    str,
    datetime,
    timedelta,
    'pint.Quantity',
    Any,
]


def get_value_type(
    value: CalculationValue,
) -> Tuple[CalculationValue, 'Calculation.ValueType']:
    if isinstance(value, complex):
        value = complex(
            Calculation.fix_number_precision(value.real),
            Calculation.fix_number_precision(value.imag),
        )
        value = value.real if value.imag == 0 else value

    if isinstance(value, float):
        value = Calculation.fix_number_precision(value)

    if value is None:
        return value, Calculation.ValueType.NONE
    if isinstance(value, bool):
        return value, Calculation.ValueType.BOOLEAN
    if isinstance(value, float):
        return value, Calculation.ValueType.FLOAT
    if isinstance(value, int):
        return value, Calculation.ValueType.INT
    if isinstance(value, str):
        return value, Calculation.ValueType.STRING
    if isinstance(value, complex) and value.real == 0:
        return value, Calculation.ValueType.IMAGINARY
    if isinstance(value, complex):
        return value, Calculation.ValueType.COMPLEX
    if isinstance(value, datetime):
        return value, Calculation.ValueType.DATETIME
    if isinstance(value, timedelta):
        return value, Calculation.ValueType.TIMEDELTA
    if pint and isinstance(value, pint.Quantity):
        return value, Calculation.ValueType.UNIT

    return value, Calculation.ValueType.UNKNOWN


class Calculation(ABC):
    class ValueType(Enum):
        UNKNOWN = -1
        NONE = 0
        BOOLEAN = 1
        INT = 2
        FLOAT = 3
        IMAGINARY = 5
        COMPLEX = 6
        STRING = 7
        DATETIME = 8
        TIMEDELTA = 9
        UNIT = 10

    def __init__(
        self,
        value,
        query: str,
        order: int,
    ):
        self.value, self.value_type = get_value_type(value)
        self.query = query
        self.order = order

    @staticmethod
    def fix_number_precision(
        number: Union[float, int, complex]
    ) -> Union[float, int, complex]:
        number_dec = number % 1 if number >= 0 else -(-number % 1)
        if cmath.isclose(number_dec, 0, abs_tol=CALCULATOR_ERROR):
            return int(number)
        if cmath.isclose(number_dec, 1, abs_tol=CALCULATOR_ERROR):
            return int(number) + 1
        return number

    @abstractmethod
    def to_query_result(self):
        pass


class CalculationError(Calculation):
    def __init__(self, error: ExtendedException, query: str = '') -> None:
        super().__init__(None, query, error.order)
        self.error = error

    def to_query_result(self):
        return _HANDLERS[self.error.__class__](self)


def missing_parsedatetime_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('time.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('missing-parsedatetime-error'),
        description=translator('missing-parsedatetime-error-description'),
        clipboard='/usr/bin/python3 -m pip install parsedatetime',
        error=calculation.error,
        order=calculation.order,
    )


def missing_simpleeval_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('icon.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('missing-simpleeval-error'),
        description=translator('missing-simpleeval-error-description'),
        clipboard='/usr/bin/python3 -m pip install simpleeval',
        error=calculation.error,
        order=calculation.order,
    )


def missing_pint_error_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('convert.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('missing-pint-error'),
        description=translator('missing-pint-error-description'),
        clipboard='/usr/bin/python3 -m pip install Pint',
        error=calculation.error,
        order=calculation.order,
    )


def boolean_comparison_error_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('icon.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('boolean-comparison-error'),
        description=translator('boolean-comparison-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.order,
    )


def boolean_percentage_error_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('icon.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('boolean-percentage-error'),
        description=translator('boolean-percentage-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.order,
    )


def base_floating_point_exception_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('icon.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('base-floating-error'),
        description=translator('base-floating-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.order,
    )


def wrong_base_exception_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('icon.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('wrong-base-error'),
        description=translator('wrong-base-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.order,
    )


def date_overflow_error_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('time.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('date-overflow'),
        description=translator('date-overflow-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.order,
    )


def currency_provider_error_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('convert.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('currency-provider-error'),
        description=translator('currency-provider-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.order,
    )


def zero_division_error_query_result(
    calculation: CalculationError,
) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('icon.svg')
    translator = LanguageService().get_translator('errors')
    return QueryResult(
        icon=icon,
        name=translator('zero-division-error'),
        description=translator('zero-division-error-description'),
        clipboard='',
        error=calculation.error,
        order=calculation.order,
    )


def misparsed_time_exception(calculation: CalculationError) -> QueryResult:
    icon = calculation.error.extra.get('icon') or images_dir('time.svg')
    translator = LanguageService().get_translator('errors')
    name = translator('misparsed-datetime')
    name = '{}: "{}"'.format(name, calculation.error.extra['parsed_query'])
    description = translator('misparsed-datetime-description')
    description = '{}: "{}"'.format(
        description, calculation.error.extra['original_query']
    )
    return QueryResult(
        icon=icon,
        name=name,
        description=description,
        clipboard='',
        error=calculation.error,
        order=calculation.order,
    )


_HANDLERS: Dict[
    Type[ExtendedException], Callable[[CalculationError], QueryResult]
] = {
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
    BaseFloatingPointException: base_floating_point_exception_query_result,
}
