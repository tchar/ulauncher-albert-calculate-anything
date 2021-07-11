from calculate_anything.calculation.calculation import BooleanCalculation
from calculate_anything.query.handlers.calculator import CalculatorQueryHandler
import re
import operator
import ast
try:
    from simpleeval import SimpleEval
except ImportError:
    SimpleEval = None
from .interface import QueryHandlerInterface
from ...calculation import (
    BaseNCalculation, Base16StringCalculation, Base10Calculation, 
    Base2Calculation, Base8Calculation, Base16Calculation, ColorBase16Calculation
)
from ...logging_wrapper import LoggingWrapper as logging
from ...utils import Singleton, is_integer, or_regex
from ...exceptions import BaseFloatingPointException, WrongBaseException, ZeroDivisionException

space_in_middle_re = re.compile('\S\s+\S')
expression_sub = {'mod': '%', 'div': '//', 'and': '&', 'or': '|', 'xor': '^', '=': '=='}
expression_sub_re = re.compile(or_regex(expression_sub))

expression_eq_split = re.compile(or_regex(['==', '>', '>=', '<', '<=']))

keyword_set = set(['^', '|', '&', '%', '//' , '+', '-', '*', '/', '(', ')'])
expression_split_re = re.compile(or_regex(keyword_set))

digits_base2_re = re.compile(re.compile(r'^\s*([01]+)\s*$'))
digits_base8_re = re.compile(r'^\s*([0-7]+)\s*$')
digits_base16_re = re.compile(r'^\s*([A-Fa-f0-9]+)\s*$')
digits_base10_re = re.compile(r'^\s*([0-9]+)\s*$')

class BaseNQueryHandler(QueryHandlerInterface):
    def __init__(self, base, digits_re, base_class, convert_classes=[]):
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
        convert_to_base_n = lambda m: str(int(m.group(0), self._base))
        sub_keywords = lambda s: expression_sub[s.group(0)]

        if sub_kw:
            expression = expression_sub_re.sub(sub_keywords, expression)

        if split_eq:
            expression = expression_eq_split.split(expression)
            expression, operators = expression[::2], expression[1::2]
            return [
                self.parse_expression(subexp, split_eq=False, sub_kw=False)[0][0]
                for subexp in expression
            ], operators

        expression = expression_split_re.split(expression)
        expr = ''
        for c in expression:
            if c.strip() == '': expr += c
            elif c in keyword_set: expr += c
            else:
                if space_in_middle_re.search(c): raise ValueError
                c, n = re.subn(self._digits_re, convert_to_base_n, c)
                if n == 0 and '.' not in c: raise WrongBaseException
                elif n == 0: raise BaseFloatingPointException
                expr += c
        return [expr], []

    def _items_to_result(items, return_raw):
        return items if return_raw else [item.to_query_result() for item in items]

    def handle(self, query, return_raw=False):
        if query.strip() == '':
            return None
        
        original_query = query
        query = query.lower()
        results = []

        try:
            expressions, operators = self.parse_expression(query)
        except WrongBaseException:
            item = BaseNCalculation(error=WrongBaseException, order=-1)
            return BaseNQueryHandler._items_to_result([item], return_raw)
        except BaseFloatingPointException:
            item = BaseNCalculation(error=BaseFloatingPointException, order=0)
            return BaseNQueryHandler._items_to_result([item], return_raw)
        except ValueError: pass
        except Exception as e:
            self.__logger.error(e)
            return None

        results = []
        try:
            results = [self._simple_eval.eval(exp) for exp in expressions]
        except ZeroDivisionError:
            item = BaseNCalculation(error=ZeroDivisionException, order=-1)
        except Exception:
            return None
        
        if len(results) == 1:
            result = results[0]
            if not is_integer(result):
                item = BaseNCalculation(error=BaseFloatingPointException, order=0)
            else:
                item = BaseNCalculation(value=results[0], order=0)
        # Boolean result
        elif len(results) > 1:
            item = CalculatorQueryHandler._calculate_boolean_result(results, operators, [])

        items = []
        if item.is_error(): items.append(item)
        elif isinstance(item, BooleanCalculation): items.append(item)
        else:
            # Add item to original base if original query is not just a number
            if not self._digits_re.match(original_query):
                item_base = item.to_base_calculation(self._base_class, order=0)
                items.append(item_base)
            for convert_class in self._convert_classes:
                item_base = item.to_base_calculation(convert_class, order=len(items))
                items.append(item_base)
        
        return BaseNQueryHandler._items_to_result(items, return_raw)

class Base2QueryHandler(BaseNQueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__(2, digits_base2_re, Base2Calculation, (Base10Calculation, Base16Calculation, Base8Calculation))

class Base8QueryHandler(BaseNQueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__(8, digits_base8_re, Base8Calculation, (Base10Calculation, Base2Calculation, Base16Calculation))

class Base16QueryHandler(BaseNQueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__(16, digits_base16_re, Base16Calculation, (Base10Calculation, Base2Calculation, Base8Calculation))

    def handle(self, query, return_raw=False):
        if query.strip() == '':
            return None
        items = []

        color_query = query.strip()
        is_color = color_query.startswith('#')
        if is_color:
            color_query = color_query[1:].strip()
            if self._digits_re.match(color_query) and len(color_query) == 6:
                items.extend(ColorBase16Calculation.get_color_calculations(color_query, order_offset=len(items)))
        else:
            items_super = super().handle(query, return_raw=True)
            if items_super: items.extend(items_super)
            
        item = Base16StringCalculation(value=query, order=len(items))
        items.append(item)

        return Base16QueryHandler._items_to_result(items, return_raw)

class Base10QueryHandler(BaseNQueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__(10, digits_base10_re, Base10Calculation, (Base16Calculation, Base2Calculation, Base8Calculation))