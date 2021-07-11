import re
import cmath
import operator as op
try:
    from simpleeval import SimpleEval
except ImportError:
    SimpleEval = None
from .interface import QueryHandlerInterface
from ...logging_wrapper import LoggingWrapper as logging
from ...calculation import Calculation, BooleanCalculation
from ...utils import is_types, Singleton
from ...exceptions import MissingSimpleevalException, ZeroDivisionException, BooleanComparisonException
from ...constants import (
    CALCULATOR_REGEX_REJECT, CALCULATOR_QUERY_REPLACE,
    CALCULATOR_QUERY_REPLACE, CALCULATOR_QUERY_REGEX_REPLACE,
    CALCULATOR_REPLACE_LEADING_ZEROS, CALCULATOR_QUERY_SPLIT_EQUALITIES
)
class CalculatorQueryHandler(QueryHandlerInterface, metaclass=Singleton):
    def __init__(self):
        functions = {
            name: getattr(cmath, name)
            for name in dir(cmath)
            if not name.startswith('_') and not name.endswith('_')
        }
        self._simple_eval = SimpleEval(functions=functions) if SimpleEval else None
        self._logger = logging.getLogger(__name__)
        self._function_names = list(functions.keys())

        keywords = [name.lower() for name in self._function_names]
        keywords.extend(['%', '//', '*', '/', '+', '-', '(', ')', '**'])
        keywords = sorted(keywords, key=len, reverse=True)
        keywords_regex = map(re.escape, keywords)
        keywords_regex = '(' + '|'.join(keywords_regex) + '|\\s+' + ')'
        self._keywords_regex = re.compile(keywords_regex)
        self._keywords_set = set(keywords)

    def parse_expression(self, expression):
        expression = expression.strip().lower()
        expression = self._keywords_regex.split(expression)
        expr = ''
        prev = ''
        has_imaginary = False
        prev_space = False
        for c in expression:
            is_space = c.strip() == ''
            if is_space: expr += c
            elif c in self._keywords_set: expr += c
            elif c.isnumeric(): 
                if prev.isnumeric() and prev_space: return ''
                expr += c
            elif c in ['i', 'j']:
                has_imaginary = True
                if prev in ['', '(', '+', '-', '*', '/']: expr += '1j'
                else: expr += 'j'
            elif c[0] in ['i', 'j']:
                if not c[1:].isnumeric(): return '', True
                c = c[1:] + c[0]
                expr += c
                has_imaginary = True
            else:
                c = c.replace('i', 'j')
                has_imaginary = has_imaginary or 'j' in c
                expr += c
            prev_space = is_space
            prev = prev if is_space else c
        expr = CALCULATOR_REPLACE_LEADING_ZEROS.sub(lambda r: r.group(0).replace('0', ''), expr)
        return expr, has_imaginary

    def _calculate_boolean_result(values, operators, subqueries):
        fixed_precisions = []
        for value in values:
            if is_types(value, int, float): value = complex(value, 0)
            fixed_precision = complex(
                Calculation.fix_number_precision(value.real),
                Calculation.fix_number_precision(value.imag)
            )
            fixed_precisions.append(fixed_precision)
        values = tuple(fixed_precisions)
        operators = operators

        op_dict = {
            '<': op.lt,
            '>': op.gt,
            '==': op.eq,
            '>=': op.ge,
            '<=': op.le
        }
        inequalities = set(['>', '<', '>=', '<='])

        result = True
        for i, [value1, value2, operator] in enumerate(zip(values, values[1:], operators)):
            if operator in inequalities:
                if value1.imag != 0 or value2.imag != 0:
                    return BooleanCalculation(value=None, error=BooleanComparisonException, order=0)
            result = result and op_dict[operator](value1.real, value2.real)
        return BooleanCalculation(value=result, query=subqueries, order=0)

    def handle(self, query, return_raw=False):
        if self._simple_eval is None:
            result = Calculation(error=MissingSimpleevalException)
            return [result] if return_raw else [result.to_query_result()]

        query = query.lower()
        if CALCULATOR_REGEX_REJECT.match(query):
            return None

        query = CALCULATOR_QUERY_REGEX_REPLACE.sub(lambda m: CALCULATOR_QUERY_REPLACE[re.escape(m.group(0))], query)
        query, _ = self.parse_expression(query)
        if not query:
            return None

        subqueries = CALCULATOR_QUERY_SPLIT_EQUALITIES.split(query)
        subqueries, operators = subqueries[::2], subqueries[1::2]
        if any(map(lambda s: s.strip() == '', subqueries)):
            return

        try:
            values = [self._simple_eval.eval(subquery) for subquery in subqueries]
        except ZeroDivisionError:
            result = Calculation(error=ZeroDivisionException)
            return [result] if return_raw else [result.to_query_result()]
        except Exception as e:
            return None
        
        if not any(map(lambda value: is_types(value, int, float, complex), values)):
            return None

        if len(values) != 1:
            result = CalculatorQueryHandler._calculate_boolean_result(values, operators, subqueries)
        else:
            result = Calculation(value=values[0], query=subqueries[0])

        if return_raw:
            return [result]

        return [result] if return_raw else [result.to_query_result()]