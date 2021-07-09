import re
from .calculator import CalculatorQueryHandler
from .interface import QueryHandler
from ...calculation import InversePercentageCalculation, NormalPercentageCalculation, PercentageCalculation
from ...exceptions import ZeroDivisionException
from ...utils import Singleton
from ...constants import (
    PERCENTAGES_REGEX_MATCH_NORMAL, PERCENTAGES_REGEX_MATCH_INVERSE,
    PERCENTAGES_REGEX_CALC_MATCH, PLUS_MINUS_REPLACE, PLUS_MINUS_REGEX_REPLACE,
)

class PercentagesQueryHandler(QueryHandler, metaclass=Singleton):

    def _use_calculator(self, query):
        results = CalculatorQueryHandler().handle(query, return_raw=True)
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
                amounts=(percentage_from, percentage_to)
            )

        try:
            result = percentage_from.value * percentage_to.value / 100
            return NormalPercentageCalculation(
                value=result,
                amounts=(percentage_from, percentage_to),
            )
        except (TypeError, ValueError) as e:
            return None
        except ZeroDivisionError as e:
            return NormalPercentageCalculation(
                amounts=(percentage_from, percentage_to),
                error=ZeroDivisionException,
            )
    
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
                amounts=(percentage_from, percentage_to)
            )

        try:
            result = 100 * percentage_from.value / percentage_to.value
            return InversePercentageCalculation(
                value=result,
                amounts=(percentage_from, percentage_to),
            )
        except (TypeError, ValueError) as e:
            return None
        except ZeroDivisionError:
            return InversePercentageCalculation(
                amounts=(percentage_from, percentage_to),
                error=ZeroDivisionException,
            )

    def _calculate_calc(self, query):
        query = query.lower()
        query = PLUS_MINUS_REGEX_REPLACE.sub(lambda m: PLUS_MINUS_REPLACE[re.escape(m.group(0))], query)

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
                amounts=(amount, percentage)
            )

        try:
            amount2 = percentage.value * amount.value / 100
            result = amount.value + amount2 if sign == '+' else amount.value - amount2
            return PercentageCalculation(
                value=result,
                amounts=(amount, percentage),
            )
        except (ValueError, TypeError):
            return None, None, None
        except ZeroDivisionError:
            return PercentageCalculation(
                amounts=(amount, percentage),
                error=ZeroDivisionException,
            )

    def handle(self, query, return_raw=False):
        calculation = self._calculate_convert_normal(query)

        if calculation is None:
            calculation = self._calculate_convert_inverse(query)
        
        if calculation is None:
            calculation = self._calculate_calc(query)

        if calculation is None:
            return

        return [calculation] if return_raw else [calculation.to_query_result()]
