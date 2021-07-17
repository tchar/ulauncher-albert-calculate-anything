import re
import cmath
from .base import _Calculation
from ..query.result import QueryResult
from ..lang import Language
from ..constants import CALCULATOR_ERROR
from ..utils import replace_dict_re_func

class Calculation(_Calculation):
    VALUE_UNKNOWN = -1
    VALUE_NONE = 0
    VALUE_BOOLEAN = 1
    VALUE_INT = 2
    VALUE_FLOAT = 3
    VALUE_REAL = 4
    VALUE_IMAGINARY = 5
    VALUE_COMPLEX = 6
    VALUE_STRING = 7

    def __init__(self, value=None, query='', error=None, order=0):
        if isinstance(value, complex):
            value = complex(
                Calculation.fix_number_precision(value.real),
                Calculation.fix_number_precision(value.imag)
            )
        super().__init__(value=value, query=query, error=error, order=order)

        if value is None: self.value_type = Calculation.VALUE_NONE
        elif isinstance(value, int): self.value_type = Calculation.VALUE_INT
        elif isinstance(value, float): self.value_type = Calculation.VALUE_FLOAT
        elif isinstance(value, bool): self.value_type = Calculation.VALUE_BOOLEAN
        elif isinstance(value, str): self.value_type = Calculation.VALUE_STRING
        elif isinstance(value, complex):
            if self.value.imag == 0: self.value_type = Calculation.VALUE_REAL
            elif self.value.real == 0: self.value_type = Calculation.VALUE_IMAGINARY
            else: self.value_type = Calculation.VALUE_COMPLEX
        else: self.value_type = Calculation.VALUE_UNKNOWN

    @staticmethod
    def fix_number_precision(number):
        number_dec = number % 1
        if cmath.isclose(number_dec, 0, abs_tol=CALCULATOR_ERROR):
            return int(number)
        return number

    def get_description(self):
        translator = Language().get_translator('calculator')

        value_type = self.value_type
        if value_type == Calculation.VALUE_IMAGINARY:
            return translator('result-imaginary').capitalize()
        if value_type == Calculation.VALUE_COMPLEX:
            return translator('result-complex').capitalize()
        return ''

    def format_query(self):
        def sub_i(match):
            group = match.group(0).lstrip()
            if group.startswith('1j'):
                return 'i'
            return group.replace('j', 'i')
        
        replace_special = {
            '%': 'mod',
            '//': 'div',
            '**': '^',
            '*': '×',
            'sqrt': '√',
            'pi': 'π',
            'tau': 'τ',
            '==': '='
        }

        query = self.query
        query = re.sub(r'\d+j', sub_i, query)
        query = re.split(r'(\/\/|\*\*|\=\=|\>\=|\<\=|[\+\-\/\*\%\^\>\<])', query)
        query = map(str.strip, query)
        query = ' '.join(query)
        query = replace_dict_re_func(replace_special, sort=True)(query)
        return query

    def format(self):
        real, imag = self.value.real, self.value.imag
        
        if real == 0 and imag == 0:
            name = '0'
        elif real == 0:
            if imag == -1:
                name = '-i'
            elif imag == 1:
                name = 'i'
            else:
                name = '{:g}i'.format(imag)
        elif imag == 0:
            name = '{:g}'.format(real)
        elif imag < 0:
            if imag == -1:
                name = '{:g} - i'.format(real)
            else:
                name = '{:g} - {:g}i'.format(real, -imag)
        else:
            if imag == 1:
                name = '{:g} + i'.format(real)
            else:
                name = '{:g} + {:g}i'.format(real, imag)
        return name

    def get_value(self):
        value = self.value
        value_type = self.value_type

        if value_type == Calculation.VALUE_REAL:
            return Calculation.fix_number_precision(value.real)
        return value
            
    @_Calculation.Decorators.handle_error_results
    def to_query_result(self):
        name = self.format()
        description = self.format_query()
        description_paren = self.get_description()
        if description_paren:
            description = '{} ({})'.format(description, description_paren)

        return QueryResult(
            icon='images/icon.svg',
            name=name,
            description=description,
            clipboard=name,
            value=self.get_value(),
            order=self.order
        )

class BooleanCalculation(Calculation):
    @Calculation.Decorators.handle_error_results
    def to_query_result(self):
        translator = Language().get_translator('calculator')
        result = str(self.value).lower()
    
        description = self.format_query()
        result_is_bool_str = translator('result-boolean').capitalize()
        description = '{} ({})'.format(description, result_is_bool_str)

        return QueryResult(
            icon='images/icon.svg',
            name=result,
            description=description,
            clipboard=result,
            value=self.value
        )
