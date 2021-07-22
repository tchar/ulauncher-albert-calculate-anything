from calculate_anything.calculation.calculation import Calculation
from .calculator import CalculatorQueryHandler
from .base import QueryHandler
from ... import logging
from ...calculation import InversePercentageCalculation, NormalPercentageCalculation, PercentageCalculation
from ...exceptions import BooleanPercetageException, ZeroDivisionException
from ...utils import Singleton
from ...constants import (
    PERCENTAGES_REGEX_MATCH_NORMAL, PERCENTAGES_REGEX_MATCH_INVERSE,
    PERCENTAGES_REGEX_CALC_MATCH, PLUS_MINS_REGEX,
)


class PercentagesQueryHandler(QueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__('=')
        self._logger = logging.getLogger(__name__)

    def _use_calculator(self, query):
        results = CalculatorQueryHandler().handle_raw(query)
        if not results:
            return None

        return results[0]

    def _calculate_convert_normal(self, query):
        matches = PERCENTAGES_REGEX_MATCH_NORMAL.findall(query)
        if not matches:
            return None

        percentage_from, percentage_to = matches[0]
        percentage_from = self._use_calculator(percentage_from)
        if percentage_from is None:
            return None

        percentage_to = self._use_calculator(percentage_to)
        if percentage_to is None:
            return None

        if percentage_from.error or percentage_to.error:
            return NormalPercentageCalculation(
                error=percentage_from.error or percentage_to.error,
                amounts=(percentage_from, percentage_to)
            )

        if percentage_from.value_type == Calculation.VALUE_BOOLEAN or percentage_to.value_type == Calculation.VALUE_BOOLEAN:
            return PercentageCalculation(error=BooleanPercetageException, order=0)

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

        percentage_from = self._use_calculator(percentage_from)
        if percentage_from is None:
            return None

        percentage_to = self._use_calculator(percentage_to)
        if percentage_to is None:
            return None

        if percentage_from.error or percentage_to.error:
            return InversePercentageCalculation(
                error=percentage_from.error or percentage_to.error,
                amounts=(percentage_from, percentage_to)
            )

        if percentage_from.value_type == Calculation.VALUE_BOOLEAN or percentage_to.value_type == Calculation.VALUE_BOOLEAN:
            return PercentageCalculation(error=BooleanPercetageException, order=0)

        try:
            result = 100 * percentage_from.value / percentage_to.value
            query_from = percentage_from.query
            query_to = percentage_to.query
            query = '({}) as % of ({})'.format(query_from, query_to)
            return InversePercentageCalculation(
                value=result,
                query=query,
                amounts=(percentage_from, percentage_to)
            )
        except ZeroDivisionError:
            return InversePercentageCalculation(
                amounts=(percentage_from, percentage_to),
                error=ZeroDivisionException,
            )
        except Exception as e:  # pragma: no cover
            self._logger.exception(  # pragma: no cover
                'Got exception when calculating inverse percentage with values {}, {}: {}'.format(
                    percentage_from.value, percentage_to.value, e))
            return None  # pragma: no cover

    def _calculate_calc(self, query):
        query = query.lower()
        query = PLUS_MINS_REGEX.sub_dict(query)

        matches = PERCENTAGES_REGEX_CALC_MATCH.findall(query)
        if not matches:
            return None

        amount, sign, percentage = matches[0]

        amount = self._use_calculator(amount)
        if amount is None:
            return None

        percentage = self._use_calculator(percentage)
        if percentage is None:
            return None

        if amount.error or percentage.error:
            return PercentageCalculation(
                error=amount.error or percentage.error,
                amounts=(amount, percentage)
            )

        if percentage.value_type == Calculation.VALUE_BOOLEAN or amount.value_type == Calculation.VALUE_BOOLEAN:
            return PercentageCalculation(error=BooleanPercetageException, order=0)

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
