from typing import List, Tuple, Union
import re
import math
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


def get_simple_eval(functions) -> Union['SimpleEval', StupidEval]:
    simple_eval = SimpleEval()
    if not isinstance(simple_eval, StupidEval):
        simple_eval.functions = functions
    return simple_eval


class CalculatorQueryHandler(QueryHandler, metaclass=Singleton):
    """Class that handles Calculation expressions for numbers, complex numbers,
    equalities and inequalities.
    """

    trig_mode = 'rad'
    memory = [0] * 10
    ans = None  # Last answer

    @staticmethod
    def mem_load(index, fn, num_args=1):
        def load(*args):
            memory = CalculatorQueryHandler.memory
            if len(args) == num_args:
                memory[index] = fn(*((memory[index],) + args))
                return memory[index]
            return None

        return load

    @staticmethod
    def mem_clear():
        CalculatorQueryHandler.memory = [0] * 10
        return 0

    @staticmethod
    def _convert_args(name, args, conversion):
        if any(arg.imag != 0 for arg in args):
            return None
        converted = []
        for index, arg in enumerate(args):
            if index in CalculatorQueryHandler.convert_exceptions.get(name, []):
                converted.append(arg.real)
            else:
                converted.append(conversion(arg.real))
        return converted

    # Indices of args that should not be converted
    convert_exceptions = {'rect': [0]}  # r is a distance in rect(r, phi)
    convert_outputs = (
        'asin',
        'acos',
        'atan',
        'acsc',
        'asec',
        'acot',
        'phase',
    )
    convert_inputs = ('sin', 'cos', 'tan', 'csc', 'sec', 'cot', 'rect')

    def __init__(self) -> None:
        super().__init__('=')
        self._old_trig_mode, self._old_memory = None, None

    def _initialize_fns(self) -> None:
        """Initializes the calculator's functions, taking into account the
        trig mode (deg, rad, grad) and memory values.
        """
        functions = {
            "mc": self.mem_clear,
            "ans": lambda: getattr(self, 'ans', 0),
        }
        if self.trig_mode == 'grad':
            functions.update(
                {
                    'deg': lambda x: x * 180 / 200,
                    'rad': lambda x: x * cmath.pi / 200,
                }
            )
        else:
            functions.update({'deg': math.degrees, 'rad': math.radians})
        for i in range(10):
            functions.update(
                {
                    "m{}".format(i): self.memory[i],
                    "m{}l".format(i): self.mem_load(i, lambda x, y: y),
                    "m{}c".format(i): self.mem_load(i, lambda x: 0, 0),
                    "m{}a".format(i): self.mem_load(i, op.add),
                    "m{}s".format(i): self.mem_load(i, op.sub),
                    "m{}m".format(i): self.mem_load(i, op.mul),
                    "m{}d".format(i): self.mem_load(i, op.truediv),
                    "m{}e".format(i): self.mem_load(i, op.pow),
                    "m{}r".format(i): self.mem_load(
                        i, lambda x, y: op.pow(x, 1 / y)
                    ),
                }
            )

        math_fns = {
            name: getattr(cmath, name)
            for name in dir(cmath)
            if not (name.startswith('_') or name.endswith('_'))
        }
        math_fns.update(
            {
                "atan2": lambda x, y: math.atan2(y, x),
                "csc": lambda x: 1 / cmath.sin(x),
                "sec": lambda x: 1 / cmath.cos(x),
                "cot": lambda x: 1 / cmath.tan(x),
                "acsc": lambda x: cmath.asin(1 / x),
                "asec": lambda x: cmath.acos(1 / x),
                "acot": lambda x: cmath.atan(1 / x),
            }
        )

        for name, fn in math_fns.items():
            if any(trig in name for trig in self.convert_outputs):
                if self.trig_mode == 'deg':
                    functions[name] = (
                        lambda orig_fn: lambda *args: (
                            math.degrees(orig_fn(*args).real)
                            if orig_fn(*args).imag == 0
                            else None
                        )
                    )(fn)
                elif self.trig_mode == 'rad':
                    functions[name] = math_fns[name]
                elif self.trig_mode == 'grad':
                    functions[name] = (
                        lambda orig_fn: lambda *args: (
                            orig_fn(*args).real * 200 / cmath.pi
                            if orig_fn(*args).imag == 0
                            else None
                        )
                    )(fn)
            elif any(trig in name for trig in self.convert_inputs):
                if self.trig_mode == 'deg':
                    functions[name] = (
                        lambda orig_fn, name: lambda *args: orig_fn(
                            *self._convert_args(name, args, math.radians)
                        )
                    )(fn, name)
                elif self.trig_mode == 'rad':
                    functions[name] = math_fns[name]
                elif self.trig_mode == 'grad':
                    functions[name] = (
                        lambda orig_fn, name: lambda *args: orig_fn(
                            *self._convert_args(
                                name, args, lambda x: x * cmath.pi / 200
                            )
                        )
                    )(fn, name)
            else:
                functions[name] = math_fns[name]

        self._simple_eval = get_simple_eval(functions)
        self._function_names = list(functions.keys())
        self._old_trig_mode = self.trig_mode
        self._old_memory = self.memory.copy()

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
        if (
            self.trig_mode != self._old_trig_mode
            or self.memory != self._old_memory
        ):
            self._initialize_fns()
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

        self.ans = result.value
        return [result]
