from typing import List, Tuple, Union
import re
import cmath
import operator as op
try:
    from simpleeval import SimpleEval
except ImportError:
    from ...utils import StupidEval
    SimpleEval = StupidEval
from .interface import QueryHandlerInterface
from ...logging_wrapper import LoggingWrapper as logging
from ...calculation import Calculation, BooleanCalculation
from ...utils import is_types, Singleton
from ...exceptions import MissingSimpleevalException, ZeroDivisionException, BooleanComparisonException
from ...constants import (
    CALCULATOR_REGEX_REJECT, CALCULATOR_QUERY_REGEX_REPLACE_FUNC,
    CALCULATOR_REPLACE_LEADING_ZEROS, CALCULATOR_QUERY_SPLIT_EQUALITIES
)


class CalculatorQueryHandler(QueryHandlerInterface, metaclass=Singleton):
    """Class that handles Calculation expressions for numbers, complex numbers,
    equalities and inequalities.
    """

    def __init__(self):
        # Cmath to set for simpleeval
        functions = {
            name: getattr(cmath, name)
            for name in dir(cmath)
            if not name.startswith('_') and not name.endswith('_')
        }
        self._simple_eval = SimpleEval(functions=functions)
        self._logger = logging.getLogger(__name__)
        self._function_names = list(functions.keys())

        keywords = [name.lower() for name in self._function_names]
        keywords.extend(['%', '//', '*', '/', '+', '-', '(', ')', '**'])
        keywords = sorted(keywords, key=len, reverse=True)
        keywords_regex = map(re.escape, keywords)
        keywords_regex = '(' + '|'.join(keywords_regex) + '|\\s+' + ')'
        self._keywords_regex = re.compile(keywords_regex)
        self._keywords_set = set(keywords)

    def _parse_expression(self, expression: str) -> Tuple[Union[None, str], int]:
        """Parses the expression and changes i(imaginary unit) to j.
        Returns str or None (parsed expression), int if it has imaginary number 

        """
        expression = expression.strip().lower()
        expression = self._keywords_regex.split(expression)
        expr = ''
        prev = ''
        has_imaginary = False
        prev_space = False
        for c in expression:
            is_space = c.strip() == ''
            if is_space:
                expr += c
            elif c in self._keywords_set:
                expr += c
            elif 'j' in c:
                return None, False
            elif c.isnumeric():
                if prev.isnumeric() and prev_space:
                    return None, False
                expr += c
            elif c == 'i':
                has_imaginary = True
                if prev in ['', '(', '+', '-', '*', '/']:
                    expr += '1j'
                else:
                    expr += 'j'
            elif c[0] == 'i':
                if not c[1:].isnumeric():
                    return None, True
                c = c[1:] + c[0]
                expr += c
                has_imaginary = True
            else:
                c = c.replace('i', 'j')
                has_imaginary = has_imaginary or 'j' in c
                expr += c
            prev_space = is_space
            prev = prev if is_space else c
        expr = CALCULATOR_REPLACE_LEADING_ZEROS.sub(
            lambda r: r.group(0).replace('0', ''), expr)
        return expr, has_imaginary

    def _calculate_boolean_result(values: Union[int, float, complex],
                                  operators: List[str], subqueries: List[str]) -> BooleanCalculation:
        """Calculates result form expression with equality/inequality
        and returns a BooleanCalculation

        """
        fixed_precisions = []
        for value in values:
            if is_types(int, float)(value):
                value = complex(value, 0)
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

        query = ''
        result = True
        for i, [value1, value2, operator] in enumerate(zip(values, values[1:], operators)):
            # If it is an inequality and either of the results have imaginary part
            # Then add a BooleanComparisonException
            if operator in inequalities:
                if value1.imag != 0 or value2.imag != 0:
                    return BooleanCalculation(value=None, error=BooleanComparisonException, order=0)
            result = result and op_dict[operator](value1.real, value2.real)
            if i == 0:
                query += subqueries[i].strip()
            query += ' ' + operator + ' ' + subqueries[i + 1].strip()

        return BooleanCalculation(value=result, query=query, order=0)

    def handle(self, query: str) -> Union[List[Calculation], None]:
        """Handles a calculation query

        Parameters
        ----------
        query : str
                The expression to calculate.

        Returns
        -------
        list of Calculation or None if query cannot be parsed/calculated
            A list of calculation results.
        """
        query = query.lower()
        if CALCULATOR_REGEX_REJECT.match(query):
            return None

        query = CALCULATOR_QUERY_REGEX_REPLACE_FUNC(query)
        query, _ = self._parse_expression(query)
        if not query:
            return None

        subqueries = CALCULATOR_QUERY_SPLIT_EQUALITIES.split(query)
        subqueries, operators = subqueries[::2], subqueries[1::2]

        if any(map(lambda s: s.strip() == '', subqueries)):
            return None

        try:
            results = [
                self._simple_eval.eval(subquery)
                for subquery in subqueries
            ]
        except MissingSimpleevalException:
            item = Calculation(query=query, error=MissingSimpleevalException)
            return [item]
        except ZeroDivisionError:
            item = Calculation(query=query, error=ZeroDivisionException)
            return [item]
        except Exception as e:
            self._logger.error(
                'Got exception when trying to calculate {}: {}'.format(query, e))
            return None

        if not any(map(is_types(int, float, complex), results)):
            return None

        if len(results) != 1:
            result = CalculatorQueryHandler._calculate_boolean_result(
                results, operators, subqueries)
        else:
            result = Calculation(value=results[0], query=subqueries[0])

        return [result]
