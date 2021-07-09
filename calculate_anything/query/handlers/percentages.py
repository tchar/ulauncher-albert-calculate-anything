from calculate_anything.exceptions import ZeroDivisionException
from calculate_anything.lang import Language
import re
from datetime import datetime
from .calculator import CalculatorQueryHandler
from .interface import QueryHandler
from ..result import QueryResult
from ...utils import Singleton
from ...constants import (
    PERCENTAGES_REGEX_MATCH_NORMAL, PERCENTAGES_REGEX_MATCH_INVERSE,
    PERCENTAGES_REGEX_CALC_MATCH, PLUS_MINUS_REPLACE, PLUS_MINUS_REGEX_REPLACE,
    CALCULATOR_BOOLEAN_RESULT_REGEX
)

class PercentagesQueryHandler(QueryHandler, metaclass=Singleton):
    
    def _use_calculator(self, query):
        results = CalculatorQueryHandler().handle(query, skip_format=True)
        if not results:
            return None
        
        result = results[0]
        if result.error == ZeroDivisionException:
            return float('inf')
        if result.error:
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

        if percentage_from == float('inf') or percentage_to == float('inf'):
            return float('inf'), (percentage_from, percentage_to)

        try:
            result = percentage_from * percentage_to / 100
            return result, (percentage_from, percentage_to)
        except (TypeError, ValueError) as e:
            return None, None
        except ZeroDivisionError as e:
            return float('inf'), (percentage_from, percentage_to)
    
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

        if percentage_from == float('inf') or percentage_to == float('inf'):
            return float('inf'), (percentage_from, percentage_to)

        try:
            result = 100 * percentage_from / percentage_to
            return result, (percentage_from, percentage_to)
        except (TypeError, ValueError) as e:
            return None, None
        except ZeroDivisionError:
            return float('inf'), (percentage_from, percentage_to)

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

        if amount == float('inf') or percentage == float('inf'):
            return float('inf'), (amount, percentage)

        try:
            amount2 = percentage * amount / 100
            result = amount + amount2 if sign == '+' else amount - amount2
            return result, (amount, percentage)
        except (ValueError, TypeError):
            return None, None
        except ZeroDivisionError:
            return float('inf'), (amount, percentage)

    @staticmethod
    def _format_result(value, has_boolean):
        if value == float('inf'):
            return str(value), None
        
        real = CalculatorQueryHandler._fix_number_precision(value.real)
        imag = CalculatorQueryHandler._fix_number_precision(value.imag)
        if imag == 0:
            result_formatted = '{:g}'.format(real)
            result_type = 'real'
        else:
            result_formatted, _ = CalculatorQueryHandler._format_result(value, has_boolean=has_boolean)
            result_formatted = '({})'.format(result_formatted)
            result_type = 'imaginary' if real == 0 else 'complex'

        return result_formatted, result_type
        
    def handle(self, query):
        has_boolean = CALCULATOR_BOOLEAN_RESULT_REGEX.search(query)
        
        result, values = self._calculate_convert_normal(query)
        mode = 'normal'

        if result is None:
            result, values = self._calculate_convert_inverse(query)
            mode = 'inverse'
        
        if result is None:
            result, values = self._calculate_calc(query)
            mode = 'calc'

        if result is None:
            return

        translator = Language().get_translator('calculator')

        result_formatted, result_type = PercentagesQueryHandler._format_result(result, has_boolean)
        value_1, value_2 = values
        value_1, value_1_type = PercentagesQueryHandler._format_result(value_1, has_boolean)
        value_2, value_2_type = PercentagesQueryHandler._format_result(value_2, has_boolean)

        if result == float('inf'):
            name = translator('infinite-result')
            description = translator('infinite-result-description')
            clipboard = ''
            result = None
        elif mode == 'normal':
            name = result_formatted
            description = '{}% {{}} {}'.format(value_1, value_2, result_formatted)
            description = description.format(translator('of'))
            clipboard = name
        elif mode == 'inverse':
            name = '{}%'.format(result_formatted)
            description = '{} {{}} {}% {{}} {}'.format(value_1, result_formatted, value_2)
            description = description.format(translator('is'), translator('of'))
            clipboard = name
        elif mode == 'calc':
            name = result_formatted
            description = '{} + {:}%'.format(value_1, value_2)
            clipboard = name

        extra_descriptions = []
        if result_type == 'complex':
            extra_descriptions.append(translator('result-complex'))
        elif result_type == 'imaginary':
            extra_descriptions.append(translator('result-imaginary'))
        
        if value_1_type == 'complex' or value_2_type == 'complex':
            extra_descriptions.append(translator('value-complex'))
        elif value_1_type == 'imaginary' or value_2_type == 'imaginary':
            extra_descriptions.append(translator('value-imaginary'))

        if has_boolean:
            extra_descriptions.append(translator('query-boolean'))

        if extra_descriptions:
            extra_descriptions = ' '.join(extra_descriptions)
            description = '{} ({})'.format(description, extra_descriptions)

        return [QueryResult(
            icon='images/percent.svg',
            name=name,
            description=description,
            clipboard=clipboard,
            value=result
        )]
