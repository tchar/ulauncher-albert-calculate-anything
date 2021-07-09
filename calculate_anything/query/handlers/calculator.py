import re
import cmath
try:
    from simpleeval import SimpleEval
except ImportError:
    SimpleEval = None
from .interface import QueryHandler
from ...calculation import Calculation
from ...utils import is_types, Singleton
from ...exceptions import MissingSimpleevalException, ZeroDivisionException
from ...constants import (
    CALCULATOR_REGEX_REJECT, CALCULATOR_QUERY_REPLACE, CALCULATOR_IMAG_REGEX_UNIT_REGEX,
    CALCULATOR_QUERY_REPLACE, CALCULATOR_QUERY_REGEX_REPLACE, CALCULATOR_IMAG_REPLACE,
    CALCULATOR_BOOLEAN_RESULT_REGEX
)
class CalculatorQueryHandler(QueryHandler, metaclass=Singleton):
    def __init__(self):
        functions = {
            name: getattr(cmath, name)
            for name in dir(cmath)
            if not name.startswith('_') and not name.endswith('_')
        }
        self._simple_eval = SimpleEval(functions=functions) if SimpleEval else None

    def handle(self, query, return_raw=False):
        if self._simple_eval is None:
            result = Calculation(error=MissingSimpleevalException)
            return [result] if return_raw else [result.to_query_result()]

        query = query.lower()
        if CALCULATOR_REGEX_REJECT.match(query):
            return []

        def replace_j_unit(match):
            group = match.group(0)
            first_char = group[0]
            if first_char == ')':
                return group.replace('j', '*1j')
            if first_char.isnumeric():
                return first_char + group[1:].strip()
            return group.replace('j', '1j')

        query = CALCULATOR_QUERY_REGEX_REPLACE.sub(lambda m: CALCULATOR_QUERY_REPLACE[re.escape(m.group(0))], query)
        query = CALCULATOR_IMAG_REPLACE.sub(lambda m: m.group(0).replace('i', 'j'), query)
        query = CALCULATOR_IMAG_REGEX_UNIT_REGEX.sub(replace_j_unit, query)
        has_boolean = CALCULATOR_BOOLEAN_RESULT_REGEX.search(query)

        try:
            value = self._simple_eval.eval(query)
        except ZeroDivisionError:
            result = Calculation(error=ZeroDivisionException)
            return [result] if return_raw else [result.to_query_result()]
        except Exception as e:
            return None
        
        if not is_types(value, int, float, complex):
            return None
     
        result = Calculation(value, has_boolean=has_boolean)
        if return_raw:
            return [result]

        return [result] if return_raw else [result.to_query_result()]