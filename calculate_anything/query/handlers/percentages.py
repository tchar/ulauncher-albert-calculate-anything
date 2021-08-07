from calculate_anything.calculation.base import CalculationError
from typing import Optional, Union
from calculate_anything.query.handlers.calculator import CalculatorQueryHandler
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything import logging
from calculate_anything.calculation.calculator import CalculatorCalculation
from calculate_anything.calculation.percentage import (
    InversePercentageCalculation,
    NormalPercentageCalculation,
    PercentageCalculation,
    PercentageCalculationError,
)
from calculate_anything.exceptions import (
    BooleanPercetageException,
    ZeroDivisionException,
)
from calculate_anything.utils import Singleton, images_dir
from calculate_anything.regex import (
    PERCENTAGES_REGEX_MATCH_NORMAL,
    PERCENTAGES_REGEX_MATCH_INVERSE,
    PERCENTAGES_REGEX_CALC_MATCH,
    PLUS_MINUS_REGEX,
)


__all__ = ['PercentagesQueryHandler']


logger = logging.getLogger(__name__)


class PercentagesQueryHandler(QueryHandler, metaclass=Singleton):
    def __init__(self) -> None:
        super().__init__('=')

    def _use_calculator(self, query: str) -> Optional[CalculatorCalculation]:
        results = CalculatorQueryHandler().handle_raw(query)
        if not results:
            return None

        return results[0]

    def _find_amounts(self, amount1, amount2, query):
        amount1 = self._use_calculator(amount1)
        if amount1 is None:
            return None

        amount2 = self._use_calculator(amount2)
        if amount2 is None:
            return None

        if isinstance(amount1, CalculationError):
            amount1.error.extra['icon'] = images_dir('percent.svg')
            return PercentageCalculationError(
                amount1.error, query, (amount1, amount2)
            )

        if isinstance(amount2, CalculationError):
            amount2.error.extra['icon'] = images_dir('percent.svg')
            return PercentageCalculationError(
                amount2.error, query, (amount1, amount2)
            )

        if (
            amount1.value_type == CalculatorCalculation.ValueType.BOOLEAN
            or amount2.value_type == CalculatorCalculation.ValueType.BOOLEAN
        ):
            icon = images_dir('percent.svg')
            return PercentageCalculationError(
                BooleanPercetageException(extra={'icon': icon}),
                query,
                (amount1, amount2),
            )

        return amount1, amount2

    def _calculate_convert_normal(
        self, query: str
    ) -> Union[None, PercentageCalculationError, NormalPercentageCalculation]:
        matches = PERCENTAGES_REGEX_MATCH_NORMAL.findall(query)
        if not matches:
            return None

        percentage_from, percentage_to = matches[0]
        result = self._find_amounts(percentage_from, percentage_to, query)

        if result is None:
            return None
        if isinstance(result, PercentageCalculationError):
            return result

        percentage_from, percentage_to = result
        try:
            result = percentage_from.value * percentage_to.value / 100
            query_percentage_from = percentage_from.query
            query_percentage_to = percentage_to.query
            query = '({})% of ({})'.format(
                query_percentage_from, query_percentage_to
            )
            return NormalPercentageCalculation(
                result, query, (percentage_from, percentage_to)
            )
        except Exception as e:  # pragma: no cover
            logger.exception(
                'Got exception when calculating inverse percentage '
                'with values {}, {}: {}'.format(
                    percentage_from.value, percentage_to.value, e
                )
            )
            return None

    def _calculate_convert_inverse(
        self, query: str
    ) -> Union[None, PercentageCalculationError, InversePercentageCalculation]:
        matches = PERCENTAGES_REGEX_MATCH_INVERSE.findall(query)
        if not matches:
            return None

        percentage_from, percentage_to = matches[0]
        result = self._find_amounts(percentage_from, percentage_to, query)

        if result is None:
            return None
        if isinstance(result, PercentageCalculationError):
            return result

        percentage_from, percentage_to = result
        try:
            result = 100 * percentage_from.value / percentage_to.value
            query_from = percentage_from.query
            query_to = percentage_to.query
            query = '({}) as % of ({})'.format(query_from, query_to)
            return InversePercentageCalculation(
                result, query, (percentage_from, percentage_to)
            )
        except ZeroDivisionError:
            icon = images_dir('percent.svg')
            return PercentageCalculationError(
                ZeroDivisionException(extra={'icon': icon}),
                query,
                (percentage_from, percentage_to),
            )
        except Exception as e:  # pragma: no cover
            logger.exception(  # pragma: no cover
                'Got exception when calculating inverse percentage '
                'with values {}, {}: {}'.format(
                    percentage_from.value, percentage_to.value, e
                )
            )
            return None  # pragma: no cover

    def _calculate_calc(
        self, query: str
    ) -> Union[None, PercentageCalculationError, PercentageCalculation]:
        query = query.lower()
        query = PLUS_MINUS_REGEX.sub_dict(query)

        if not PERCENTAGES_REGEX_CALC_MATCH.findall(query):
            return None

        # Parse expression because it is ambiguous to match with regex
        parens_dict = {')': 1, '(': -1}
        signs = set(['+', '-'])
        parens = 0
        index = None
        for i, c in enumerate(reversed(query)):
            parens += parens_dict.get(c, 0)
            if c in signs and parens == 0:
                index = i
                break
        if index is None:
            return None

        index = len(query) - index - 1

        amount = query[:index]
        sign = 1 if query[index] == '+' else -1
        percentage = query[index + 1 : -1]
        if not amount.strip() or not percentage.strip():
            return None

        result = self._find_amounts(amount, percentage, query)

        if result is None:
            return None
        if isinstance(result, PercentageCalculationError):
            return result

        amount, percentage = result
        try:
            result = percentage.value * amount.value / 100
            result = amount.value + sign * result
            query_amount = amount.query
            query_percentage = percentage.query
            query = '({}) + ({})%'.format(query_amount, query_percentage)
            return PercentageCalculation(result, query, (amount, percentage))
        except Exception as e:  # pragma: no cover
            logger.exception(
                'Got exception when calculating inverse percentage '
                'with values {}, {}: {}'.format(
                    amount.value, percentage.value, e
                )
            )
            return None

    def handle_raw(
        self, query: str
    ) -> Union[None, PercentageCalculationError, PercentageCalculation]:
        if '%' not in query:
            return None

        query = query.strip()

        calculation = self._calculate_convert_normal(query)

        if calculation is None:
            calculation = self._calculate_convert_inverse(query)

        if calculation is None:
            calculation = self._calculate_calc(query)

        if calculation is None:
            return None

        return [calculation]
