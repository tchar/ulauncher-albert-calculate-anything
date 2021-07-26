from calculate_anything.query.handlers.calculator import CalculatorQueryHandler
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything import logging
from calculate_anything.calculation import (
    Calculation, InversePercentageCalculation,
    NormalPercentageCalculation, PercentageCalculation
)
from calculate_anything.exceptions import BooleanPercetageException, ZeroDivisionException
from calculate_anything.utils import Singleton
from calculate_anything.constants import (
    PERCENTAGES_REGEX_MATCH_NORMAL, PERCENTAGES_REGEX_MATCH_INVERSE,
    PERCENTAGES_REGEX_CALC_MATCH, PLUS_MINUS_REGEX,
)


__all__ = ['PercentagesQueryHandler']


class PercentagesQueryHandler(QueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__('=')
        self._logger = logging.getLogger(__name__)

    def _use_calculator(self, query):
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

        if amount1.error:
            return NormalPercentageCalculation(
                error=amount1.error,
                amounts=(amount1, amount2),
                query=query,
                order=amount1.order
            )
        if amount2.error:
            return NormalPercentageCalculation(
                error=amount2.error,
                amounts=(amount1, amount2),
                query=query,
                order=amount2.order
            )

        if amount1.value_type == Calculation.VALUE_BOOLEAN or \
                amount2.value_type == Calculation.VALUE_BOOLEAN:
            return PercentageCalculation(
                error=BooleanPercetageException,
                query=query,
                order=-20
            )

        return amount1, amount2

    def _calculate_convert_normal(self, query):
        matches = PERCENTAGES_REGEX_MATCH_NORMAL.findall(query)
        if not matches:
            return None

        percentage_from, percentage_to = matches[0]
        result = self._find_amounts(percentage_from, percentage_to, query)

        if result is None:
            return None
        if isinstance(result, Calculation):
            return result

        percentage_from, percentage_to = result
        try:
            result = percentage_from.value * percentage_to.value / 100
            query_percentage_from = percentage_from.query
            query_percentage_to = percentage_to.query
            query = '({})% of ({})'.format(
                query_percentage_from, query_percentage_to)
            return NormalPercentageCalculation(
                value=result,
                query=query,
                amounts=(percentage_from, percentage_to)
            )
        except Exception as e:  # pragma: no cover
            self._logger.exception(  # pragma: no cover
                'Got exception when calculating inverse percentage with values {}, {}: {}'.format(
                    percentage_from.value, percentage_to.value, e))
            return None  # pragma: no cover

    def _calculate_convert_inverse(self, query):
        matches = PERCENTAGES_REGEX_MATCH_INVERSE.findall(query)
        if not matches:
            return None

        percentage_from, percentage_to = matches[0]

        percentage_from, percentage_to = matches[0]
        result = self._find_amounts(percentage_from, percentage_to, query)

        if result is None:
            return None
        if isinstance(result, Calculation):
            return result

        percentage_from, percentage_to = result
        try:
            result = 100 * percentage_from.value / percentage_to.value
            query_from = percentage_from.query
            query_to = percentage_to.query
            query = '({}) as % of ({})'.format(query_from, query_to)
            return InversePercentageCalculation(
                value=result,
                query=query,
                amounts=(percentage_from, percentage_to),
                order=0
            )
        except ZeroDivisionError:
            return InversePercentageCalculation(
                amounts=(percentage_from, percentage_to),
                query=query,
                error=ZeroDivisionException,
                order=-70
            )
        except Exception as e:  # pragma: no cover
            self._logger.exception(  # pragma: no cover
                'Got exception when calculating inverse percentage with values {}, {}: {}'.format(
                    percentage_from.value, percentage_to.value, e))
            return None  # pragma: no cover

    def _calculate_calc(self, query):
        query = query.lower()
        query = PLUS_MINUS_REGEX.sub_dict(query)

        if not PERCENTAGES_REGEX_CALC_MATCH.findall(query):
            return None

        # Parse expression because it is ambiguous and difficult to match with regex
        signs = set(['+', '-'])
        parens = 0
        for i, c in enumerate(reversed(query)):
            if c == '%':
                pass
            elif c == ')':
                parens += 1
            elif c == '(':
                parens -= 1
            if c in signs and parens == 0:
                break
        else:
            return None

        i = len(query) - i - 1

        amount = query[:i]
        sign = query[i]
        percentage = query[i+1:-1]
        if not amount.strip() or not percentage.strip():
            return None

        result = self._find_amounts(amount, percentage, query)

        if result is None:
            return None
        if isinstance(result, Calculation):
            return result

        amount, percentage = result
        try:
            amount2 = percentage.value * amount.value / 100
            result = amount.value + amount2 if sign == '+' else amount.value - amount2
            query_amount = amount.query
            query_percentage = percentage.query
            query = '({}) + ({})%'.format(query_amount, query_percentage)
            return PercentageCalculation(
                value=result,
                query=query,
                amounts=(amount, percentage)
            )
        except Exception as e:  # pragma: no cover
            self._logger.exception(  # pragma: no cover
                'Got exception when calculating inverse percentage with values {}, {}: {}'.format(
                    amount.value, percentage.value, e))
            return None  # pragma: no cover

    def handle_raw(self, query):
        if '%' not in query:
            return None

        query = query.strip()

        calculation = self._calculate_convert_normal(query)

        if calculation is None:
            calculation = self._calculate_convert_inverse(query)

        if calculation is None:
            calculation = self._calculate_calc(query)

        if calculation is None:
            return

        return [calculation]

    @QueryHandler.Decorators.can_handle
    def handle(self, query):
        return self.handle_raw(query)
