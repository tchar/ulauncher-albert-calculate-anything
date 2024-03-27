from typing import List, Tuple, Union
import re
import cmath
import operator as op

from calculate_anything.utils import is_types, Singleton, StupidEval

try:
    from simpleeval import (
        SimpleEval,
        NameNotDefined,
        FeatureNotAvailable,
        FunctionNotDefined,
    )
except ImportError:  # pragma: no cover
    SimpleEval = StupidEval
    NameNotDefined = TypeError
    FeatureNotAvailable = TypeError
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything import logging
from calculate_anything.calculation.base import CalculationError
from calculate_anything.calculation.calculator import (
    CalculatorCalculation,
    BooleanCalculation,
)
from calculate_anything.exceptions import (
    MissingSimpleevalException,
    ZeroDivisionException,
    BooleanComparisonException,
)
from calculate_anything.regex import (
    CALCULATOR_REGEX_REJECT,
    CALCULATOR_QUERY_REGEX_REPLACE,
    CALCULATOR_REPLACE_LEADING_ZEROS,
    CALCULATOR_QUERY_SPLIT_EQUALITIES,
)


__all__ = ['CalculatorQueryHandler']


logger = logging.getLogger(__name__)


@Singleton.function
def get_simple_eval(functions) -> Union['SimpleEval', StupidEval]:
    simple_eval = SimpleEval()
    if not isinstance(simple_eval, StupidEval):
        simple_eval.functions = functions
    return simple_eval


class CalculatorQueryHandler(QueryHandler, metaclass=Singleton):
    """Class that handles Calculation expressions for numbers, complex numbers,
    equalities and inequalities.
    """

    def __init__(self) -> None:
        super().__init__('=')
        # Cmath to set for simpleeval
        functions = {
            name: getattr(cmath, name)
            for name in dir(cmath)
            if not name.startswith('_') and not name.endswith('_')
        }
        self._simple_eval = get_simple_eval(functions)
        self._function_names = list(functions.keys())

        keywords = [name.lower() for name in self._function_names]
        keywords.extend(['%', '//', '*', '/', '+', '-', '(', ')', '**'])
        keywords = sorted(keywords, key=len, reverse=True)
        keywords_regex = map(re.escape, keywords)
        keywords_regex = '(' + '|'.join(keywords_regex) + '|\\s+' + ')'
        self._keywords_regex = re.compile(keywords_regex)
        self._keywords_set = set(keywords)

    def _parse_expression(
        self, expression: str
    ) -> Tuple[Union[None, str], int]:
        """Parses the expression and changes i(imaginary unit) to j.
        Returns str or None (parsed expression), int if it has imaginary
        number.

        """
        expression = expression.strip().lower()
        expression = self._keywords_regex.split(expression)
        expr = ''
        prev = ''
        has_imaginary = False
        prev_space = False
        for c in expression:
            is_space = c.strip() == ''
            if is_space or c in self._keywords_set:
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
                    return None, False
            elif c[0] == 'i':
                if not c[1:].isnumeric():
                    return None, True
                c = c[1:] + 'j'
                expr += c
                has_imaginary = True
            else:
                c = c.replace('i', 'j')
                has_imaginary = has_imaginary or 'j' in c
                expr += c
            prev_space = is_space
            prev = prev if is_space else c
        expr = CALCULATOR_REPLACE_LEADING_ZEROS.sub(
            lambda r: r.group(0).replace('0', ''), expr
        )
        return expr, has_imaginary

    @staticmethod
    def _calculate_boolean_result(
        values: Union[int, float, complex],
        operators: List[str],
        subqueries: List[str],
    ) -> BooleanCalculation:
        """Calculates result form expression with equality/inequality
        and returns a BooleanCalculation

        """
        fixed_precisions = []
        for value in values:
            if isinstance(value, (int, float)):
                value = complex(value, 0)
            # Do this so if it is the case we have something
            # like 1 + 0.00000000001j
            # We consider it as 1 so it can be comparable with real numbers
            fixed_precision = complex(
                CalculatorCalculation.fix_number_precision(value.real),
                CalculatorCalculation.fix_number_precision(value.imag),
            )
            fixed_precisions.append(fixed_precision)
        values = tuple(fixed_precisions)

        op_dict = {
            '<': op.lt,
            '>': op.gt,
            '==': op.eq,
            '>=': op.ge,
            '<=': op.le,
        }
        inequalities = set(['>', '<', '>=', '<='])
        inequality_error = False
        query = ''
        result = True
        zipped_values = zip(values, values[1:], operators)
        for i, [value1, value2, operator] in enumerate(zipped_values):
            # If it is an inequality and either of the results have imaginary
            # part. Then mark it as error, let query be constructed and return
            # a BooleanComparisonException
            if operator in inequalities:
                if value1.imag != 0 or value2.imag != 0:
                    inequality_error = True
            result = result and op_dict[operator](value1.real, value2.real)
            if i == 0:
                query += subqueries[i].strip()
            query += ' ' + operator + ' ' + subqueries[i + 1].strip()

        if inequality_error:
            return CalculationError(BooleanComparisonException(), query)

        return BooleanCalculation(result, query)

    def can_handle(self, query: str) -> bool:
        if not super().can_handle(query):
            return False

        if CALCULATOR_REGEX_REJECT.match(query):
            return False
        return True

    def handle_raw(
        self, query: str
    ) -> Union[None, List[Union[CalculationError, CalculatorCalculation]]]:
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
        query = CALCULATOR_QUERY_REGEX_REPLACE.sub_dict(query)
        query, _ = self._parse_expression(query)
        if not query:
            return None

        subqueries = CALCULATOR_QUERY_SPLIT_EQUALITIES.split(query)
        subqueries, operators = subqueries[::2], subqueries[1::2]

        if any(map(lambda s: s.strip() == '', subqueries)):
            return None

        try:
            results = [
                self._simple_eval.eval(subquery) for subquery in subqueries
            ]
        except MissingSimpleevalException:
            item = CalculationError(MissingSimpleevalException(), query)
            return [item]
        except ZeroDivisionError:
            item = CalculationError(ZeroDivisionException(), query)
            return [item]
        except (SyntaxError, TypeError):
            return None
        except (NameNotDefined, FeatureNotAvailable, FunctionNotDefined) as e:
            logger.debug(
                'Got simpleval Exception: when calculating {!r}: {}'.format(
                    query, e
                )
            )
            return None
        except Exception as e:  # pragma: no cover
            logger.exception(
                'Got exception when trying to calculate {!r}: {}'.format(
                    query, e
                )
            )  # pragma: no cover
            return None  # pragma: no cover

        if not any(map(is_types(int, float, complex), results)):
            # (result must be one of int float complex, just in case)
            return None  # pragma: no cover

        if len(results) != 1:
            result = CalculatorQueryHandler._calculate_boolean_result(
                results, operators, subqueries
            )
        else:
            result = CalculatorCalculation(results[0], subqueries[0])

        return [result]
