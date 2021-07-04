import re
import cmath
try:
    from simpleeval import SimpleEval
except ImportError:
    SimpleEval = None
from ..utils import is_types
from .interface import QueryHandler
from ..utils import Singleton
from ..constants import (
    CALCULATOR_ERROR, CALCULATOR_REGEX_REJECT, CALCULATOR_QUERY_REPLACE, CALCULATOR_IMAG_REGEX,
    CALCULATOR_IMAG_REGEX_UNIT_REGEX, CALCULATOR_QUERY_REPLACE, CALCULATOR_REGEX_QUERY_REPLACE
)

class CalculatorQueryHandler(QueryHandler):
    def __init__(self):
        functions = {
            name: getattr(cmath, name)
            for name in dir(cmath)
            if not name.startswith('_') and not name.endswith('_')
        }
        self._simple_eval = SimpleEval(functions=functions)

    @staticmethod
    def _format_number(number):
        if isinstance(number, float) and number.is_integer():
            return int(number)
        
        if cmath.isclose(number, 0, abs_tol=CALCULATOR_ERROR):
            return 0
        return number

    def handle(self, query):
        if self._simple_eval is None:
            return [{
                'value': 'pip install simpleeval',
                'name': 'Looks like simpleeval is not installed.',
                'description': 'Install it with "pip install simpleeval" and restart launcher.',
                'is_error': True,
                'order': -1
            }]

        query = query.lower()
        if CALCULATOR_REGEX_REJECT.match(query):
            return []
        
        query = CALCULATOR_REGEX_QUERY_REPLACE.sub(lambda m: CALCULATOR_QUERY_REPLACE[re.escape(m.group(0))], query)
        query = CALCULATOR_IMAG_REGEX.sub(lambda m: m.group(0).replace(' ', ''), query)
        query = CALCULATOR_IMAG_REGEX_UNIT_REGEX.sub(lambda m: m.group(0).replace('j', '1j'), query)

        try:
            result = self._simple_eval.eval(query)
        except Exception as e:
            return None
        
        if not is_types(result, int, float, complex):
            return None
        real, imag = result.real, result.imag
        real = CalculatorQueryHandler._format_number(real)
        imag = CalculatorQueryHandler._format_number(imag)
        if real == 0 and imag == 0:
            result = '0'
            description = ''
        elif real == 0:
            if imag == -1:
                result = '-j'
            elif imag == 1:
                result = 'j'
            else:
                result = '{:g}j'.format(imag)
            description = 'Result is an Imaginary number'
        elif imag == 0:
            result = '{:g}'.format(real)
            description = ''
        elif imag < 0:
            if imag == -1:
                result = '{:g} - j'.format(real)
            else:
                result = '{:g} - {:g}j'.format(real, -imag)
            description = 'Result is a Complex number'
        else:
            if imag == 1:
                result = '{:g} + j'.format(real)
            else:
                result = '{:g} + {:g}j'.format(real, imag)
            description = 'Result is a Complex number'
        
        return [{'icon': 'images/calculator.svg', 'value': result, 'name': result, 'description': description, 'is_error': False, 'order': 0}]

    @classmethod
    @Singleton
    def get_instance(cls):
        return cls()