from calculate_anything.lang import Language
import re
from datetime import datetime
from .calculator import CalculatorQueryHandler
from .interface import QueryHandler
from ..result import QueryResult
from ...utils import Singleton
from ...constants import (
    PERCENTAGES_REGEX_MATCH_NORMAL, PERCENTAGES_REGEX_MATCH_INVERSE,
    PERCENTAGES_REGEX_CALC_MATCH, PLUS_MINUS_REPLACE, PLUS_MINUS_REGEX_REPLACE
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
            return None, None

        percentage_from, percentage_to = matches[0]
        percentage_from = self._use_calculator(percentage_from)

        if percentage_from is None:
            return None, None

        percentage_to = self._use_calculator(percentage_to)
        if percentage_to is None:
            return None, None

        try:
            percentage_from = float(percentage_from)
            percentage_to = float(percentage_to)
            result = percentage_from * percentage_to / 100
            return '{:g}'.format(result), (percentage_from, percentage_to)
        except (TypeError, ValueError) as e:
            return None, None
    
    def _calculate_convert_inverse(self, query):
        matches = PERCENTAGES_REGEX_MATCH_INVERSE.findall(query)
        if not matches:
            return None, None

        percentage_from, percentage_to = matches[0]
        percentage_from = self._use_calculator(percentage_from)

        if percentage_from is None:
            return None, None

        percentage_to = self._use_calculator(percentage_to)
        if percentage_to is None:
            return None, None

        try:
            percentage_from = float(percentage_from)
            percentage_to = float(percentage_to)
            result = 100 * percentage_from / percentage_to
            return '{:g}%'.format(result), (percentage_from, percentage_to)
        except (TypeError, ValueError) as e:
            return None, None

    def _calculate_calc(self, query):
        query = query.lower()
        query = PLUS_MINUS_REGEX_REPLACE.sub(lambda m: PLUS_MINUS_REPLACE[re.escape(m.group(0))], query)

        matches = PERCENTAGES_REGEX_CALC_MATCH.findall(query)
        if not matches:
            return None, None
        
        amount, sign, percentage = matches[0]


        amount = self._use_calculator(amount)
        if amount is None:
            return None, None
        
        percentage = self._use_calculator(percentage)
        if percentage is None:
            return None, None

        try:
            amount = float(amount)
            percentage = float(percentage)
            amount2 = percentage * amount / 100
            result = amount + amount2 if sign == '+' else amount - amount2
            return '{:g}'.format(result), (amount, percentage)
        except (ValueError, TypeError):
            return None, None   

    def handle(self, query):
        result, values = self._calculate_convert_normal(query)
        mode = 'normal'

        if not result:
            result, values = self._calculate_convert_inverse(query)
            mode = 'inverse'
        
        if not result:
            result, values = self._calculate_calc(query)
            mode = 'calc'

        if not result:
            return

        translator = Language().get_translator('percentage')

        a, b = values
        if mode == 'normal':
            description = '{:g}% {{}} {:g}'.format(a, b, result)
            description = description.format(translator('of'))
        elif mode == 'inverse':
            description = '{:g} {{}} {}% of {}'.format(a, result, b)
            description = description.format(translator('is'))
        elif mode == 'calc':
            description = '{:g} + {:g}%'.format(a, b, result)

        return [QueryResult(
            icon='images/percent.svg',
            value=result,
            name=result,
            description=description,
            is_error=False,
            clipboard=True
        )]
