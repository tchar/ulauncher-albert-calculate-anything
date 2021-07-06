import re
from datetime import datetime
from .calculator import CalculatorQueryHandler
from .interface import QueryHandler
from ..result import QueryResult
from ...utils import Singleton
from ...constants import (
    PERCENTAGES_REGEX_MATCH_NORMAL, PERCENTAGES_REGEX_MATCH_INVERSE,
    PERCENTAGES_REGEX_CALC_MATCH, PERCENTAGES_QUERY_REPLACE, PERCENTAGES_QUERY_REGEX_REPLACE
)

class PercentagesQueryHandler(QueryHandler, metaclass=Singleton):
    
    def _use_calculator(self, query):
        results = CalculatorQueryHandler().handle(query)
        if not results:
            return None
        
        result = results[0]
        if result.is_error:
            return None
        
        return result.value

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

        try:
            result = float(percentage_from) * float(percentage_to) / 100
            return '{:g}'.format(result)
        except (TypeError, ValueError) as e:
            return
    
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

        try:
            result = 100 * float(percentage_from) / float(percentage_to)
            return '{:g}%'.format(result)
        except (TypeError, ValueError) as e:
            return

    def _calculate_calc(self, query):
        query = query.lower()
        query = PERCENTAGES_QUERY_REGEX_REPLACE.sub(lambda m: PERCENTAGES_QUERY_REPLACE[re.escape(m.group(0))], query)

        matches = PERCENTAGES_REGEX_CALC_MATCH.findall(query)
        if not matches:
            return
        
        amount, sign, percentage = matches[0]


        amount = self._use_calculator(amount)
        if amount is None:
            return None
        
        percentage = self._use_calculator(percentage)
        if percentage is None:
            return None

        try:
            amount = float(amount)
            amount2 = float(percentage) * amount / 100
            result = amount + amount2 if sign == '+' else amount - amount2
            return '{:g}'.format(result)
        except (ValueError, TypeError):
            return None        

    def handle(self, query):
        result = (
            self._calculate_convert_normal(query) or 
            self._calculate_convert_inverse(query) or
            self._calculate_calc(query)
        )
        if not result:
            return

        return [QueryResult(
            icon='images/icon.svg',
            value=result,
            name=result,
            is_error=False,
            clipboard=True
        )]
