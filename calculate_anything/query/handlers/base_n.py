import re
import operator
import ast
try:
    from simpleeval import SimpleEval
except ImportError:
    from calculate_anything.utils import StupidEval
    SimpleEval = StupidEval
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything.calculation.base_n import (
    BaseNCalculation, Base16StringCalculation, Base10Calculation,
    Base2Calculation, Base8Calculation, Base16Calculation, ColorBase16Calculation
)
from calculate_anything.query.handlers.calculator import CalculatorQueryHandler
from calculate_anything.logging_wrapper import LoggingWrapper as logging
from calculate_anything.calculation.calculation import BooleanCalculation
from calculate_anything.utils import multi_re, Singleton, is_integer
from calculate_anything.exceptions import (
    BaseFloatingPointException, MissingSimpleevalException,
    WrongBaseException, ZeroDivisionException
)

space_in_middle_re = re.compile(r'\S\s+\S')

expression_eq_split = multi_re.compile(
    ['==', '>', '>=', '<', '<='], include=True)

keyword_set = set(['^', '|', '&', '%', '//', '+', '-', '*', '/', '(', ')'])
expression_split_re = multi_re.compile(keyword_set, include=True)

digits_base2_re = re.compile(r'^\s*([01]+)\s*$')
digits_base8_re = re.compile(r'^\s*([0-7]+)\s*$')
digits_base16_re = re.compile(r'^\s*([A-Fa-f0-9]+)\s*$')
digits_base10_re = re.compile(r'^\s*([0-9]+)\s*$')


class BaseNQueryHandler(QueryHandler):
    def __init__(self, keyword, base, digits_re, base_class, convert_classes=[]):
        super().__init__(keyword)
        self._base = base
        self._digits_re = digits_re
        self._base_class = base_class
        self._convert_classes = convert_classes
        self._simple_eval = SimpleEval() if SimpleEval else None
        if self._simple_eval:
            self._simple_eval.operators[ast.BitOr] = operator.or_
            self._simple_eval.operators[ast.BitAnd] = operator.and_
            self._simple_eval.operators[ast.BitXor] = operator.xor
        self._logger = logging.getLogger(__name__)

    def parse_expression(self, expression, split_eq=True, sub_kw=True):
        def convert_to_base_n(m): return str(int(m.group(0), self._base))

        if sub_kw:
            expression = multi_re.sub_dict({
                'mod': '%', 'div': '//',
                'and': '&', 'or': '|',
                'xor': '^', '=': '=='
            }, expression)

        if split_eq:
            expression = expression_eq_split.split(expression)
            expression, operators = expression[::2], expression[1::2]

            exprs = []
            exprs_parsed = []

            for subexp in expression:
                expr_dec, _, expr_parsed = self.parse_expression(
                    subexp, split_eq=False, sub_kw=False)
                exprs.append(expr_dec[0])
                exprs_parsed.append(expr_parsed[0])

            return exprs, operators, exprs_parsed

        expression = expression_split_re.split(expression)
        expr = ''
        expr_parsed = ''
        for c in expression:
            if c.strip() == '':
                expr += c
                expr_parsed += c
            elif c in keyword_set:
                expr += c
                expr_parsed += c
            else:
                if space_in_middle_re.search(c):
                    raise ValueError
                c_dec, n = re.subn(self._digits_re, convert_to_base_n, c)
                if n == 0 and '.' not in c_dec:
                    raise WrongBaseException
                elif n == 0:
                    raise BaseFloatingPointException
                expr += c_dec
                expr_parsed += c
        return [expr], [], [expr_parsed]

    def handle_raw(self, query):
        query = query.strip()
        original_query = query
        query = query.lower()
        results = []

        try:
            expr_dec, operators, expr_parsed = self.parse_expression(query)
        except WrongBaseException:
            item = BaseNCalculation(
                error=WrongBaseException,
                query=original_query,
                order=-40
            )
            return [item]
        except BaseFloatingPointException:
            item = BaseNCalculation(
                error=BaseFloatingPointException,
                query=original_query,
                order=-30
            )
            return [item]
        except Exception as e:
            self._logger.error(e)
            return None

        results = []
        try:
            results = [self._simple_eval.eval(exp) for exp in expr_dec]
        except MissingSimpleevalException:
            item = BaseNCalculation(
                error=MissingSimpleevalException,
                query=original_query,
                order=-1
            )
            return [item]
        except ZeroDivisionError:
            item = BaseNCalculation(
                error=ZeroDivisionException,
                query=original_query,
                order=-70
            )
            return [item]
        except Exception:
            return None

        if len(results) == 1:
            result = results[0]
            if not is_integer(result):
                item = BaseNCalculation(
                    error=BaseFloatingPointException,
                    order=0
                )
            else:
                item = BaseNCalculation(
                    value=results[0],
                    query=original_query,
                    order=0
                )
        # Boolean result
        elif len(results) > 1:
            item = CalculatorQueryHandler._calculate_boolean_result(
                results, operators, expr_parsed)

        items = []
        if item.is_error():
            items.append(item)
        elif isinstance(item, BooleanCalculation):
            items.append(item)
        else:
            # Add item to original base if original query is not just a number
            if not self._digits_re.match(original_query):
                item_base = item.to_base_calculation(self._base_class, order=0)
                items.append(item_base)
            for convert_class in self._convert_classes:
                item_base = item.to_base_calculation(
                    convert_class, order=len(items))
                items.append(item_base)

        return items

    @QueryHandler.Decorators.can_handle
    def handle(self, query):
        return self.handle_raw(query)


class Base2QueryHandler(BaseNQueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__('bin', 2, digits_base2_re, Base2Calculation,
                         (Base10Calculation, Base16Calculation, Base8Calculation))


class Base8QueryHandler(BaseNQueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__('oct', 8, digits_base8_re, Base8Calculation,
                         (Base10Calculation, Base2Calculation, Base16Calculation))


class Base16QueryHandler(BaseNQueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__('hex', 16, digits_base16_re, Base16Calculation,
                         (Base10Calculation, Base2Calculation, Base8Calculation))

    def handle_raw(self, query):
        original_query = query.strip()
        items = []

        color_query = query.strip()
        is_color = color_query.startswith('#')
        if is_color:
            color_query = color_query[1:].strip()
            if self._digits_re.match(color_query) and len(color_query) == 6:
                items.extend(ColorBase16Calculation.get_color_calculations(
                    color_query, query=original_query, order_offset=len(items)
                ))
        else:
            items_super = super().handle_raw(query)
            if items_super:
                items.extend(items_super)

        non_errors = sum(map(lambda item: not item.error, items))
        item = Base16StringCalculation(
            value=query,
            query=original_query,
            order=non_errors
        )
        items.append(item)
        return items

    @QueryHandler.Decorators.can_handle
    def handle(self, query):
        return self.handle_raw(query)


class Base10QueryHandler(BaseNQueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__('dec', 10, digits_base10_re, Base10Calculation,
                         (Base16Calculation, Base2Calculation, Base8Calculation))
