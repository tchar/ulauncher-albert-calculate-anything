from calculate_anything.lang import Language
import re
import cmath
try:
    from simpleeval import SimpleEval
except ImportError:
    SimpleEval = None
from ..result import QueryResult
from .interface import QueryHandler
from ...utils import is_types, Singleton
from ...exceptions import MissingSimpleevalException, ZeroDivisionException
from ...constants import (
    CALCULATOR_ERROR, CALCULATOR_REGEX_REJECT, CALCULATOR_QUERY_REPLACE, CALCULATOR_IMAG_REGEX_UNIT_REGEX,
    CALCULATOR_QUERY_REPLACE, CALCULATOR_QUERY_REGEX_REPLACE, CALCULATOR_IMAG_REPLACE, CALCULATOR_BOOLEAN_RESULT_REGEX
)

class CalculatorQueryHandler(QueryHandler, metaclass=Singleton):
    def __init__(self):
        functions = {
            name: getattr(cmath, name)
            for name in dir(cmath)
            if not name.startswith('_') and not name.endswith('_')
        }
        self._simple_eval = SimpleEval(functions=functions)

    @staticmethod
    def _fix_number_precision(number):
        # if isinstance(number, float) and number.is_integer():
            # return int(number)
        
        if cmath.isclose(number, 0, abs_tol=CALCULATOR_ERROR):
            return 0
        return number

    @staticmethod
    def _zero_division_error():
        return [QueryResult(
            icon='images/icon.svg',
            name=Language().translate('infinite-result', 'calculator'),
            description=Language().translate('infinite-result-description', 'calculator'),
            error=ZeroDivisionException
        )]

    @staticmethod
    def _format_result(value, has_boolean):
        translator = Language().get_translator('calculator')

        real, imag = value.real, value.imag
        real = CalculatorQueryHandler._fix_number_precision(real)
        imag = CalculatorQueryHandler._fix_number_precision(imag)
        
        if real == 0 and imag == 0:
            name = '0'
            description = translator('query-boolean') if has_boolean else ''
        elif real == 0:
            if imag == -1:
                name = '-i'
            elif imag == 1:
                name = 'i'
            else:
                name = '{:g}i'.format(imag)
            description = translator('result-imaginary')
        elif imag == 0:
            name = '{:g}'.format(real)
            description = translator('query-boolean') if has_boolean else ''
        elif imag < 0:
            if imag == -1:
                name = '{:g} - i'.format(real)
            else:
                name = '{:g} - {:g}i'.format(real, -imag)
            description = translator('result-complex')
        else:
            if imag == 1:
                name = '{:g} + i'.format(real)
            else:
                name = '{:g} + {:g}i'.format(real, imag)
            description = translator('result-complex')

        return name, description

    def handle(self, query, skip_format=False):
        translator = Language().get_translator('calculator')

        if self._simple_eval is None:
            return [QueryResult(
                icon='images/icon.svg',
                clipboard='pip install simpleeval',
                name=translator('install-simpleeval'),
                description=translator('install-simpleeval-description'),
                error=MissingSimpleevalException
            )]

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
            return CalculatorQueryHandler._zero_division_error()
        except Exception as e:
            return None
        
        if not is_types(value, int, float, complex):
            return None
     
        if not skip_format:
            name, description = CalculatorQueryHandler._format_result(value, has_boolean)
        else:
            name, description = '', ''

        return [QueryResult(
            icon='images/icon.svg',
            name=name,
            description=description,
            clipboard=name,
            value=value,
            order=0
        )]
