import cmath
from .base import BaseCalculation
from ..query.result import QueryResult
from ..lang import Language
from ..constants import CALCULATOR_ERROR

class Calculation(BaseCalculation):
    VALUE_REAL = 0
    VALUE_COMPLEX = 1
    VALUE_IMAGINARY = 2
    VALUE_NONE = 3

    def __init__(self, value=None, has_boolean=False, error=None, order=0):
        if value is not None:
            value = complex(
                Calculation.fix_number_precision(value.real),
                Calculation.fix_number_precision(value.imag)
            )
        super().__init__(value=value, error=error, order=order)

        self.has_boolean = has_boolean

        if value is None: self.value_type = Calculation.VALUE_NONE
        elif self.value.imag == 0: self.value_type = Calculation.VALUE_REAL
        elif self.value.real == 0: self.value_type = Calculation.VALUE_IMAGINARY
        else: self.value_type = Calculation.VALUE_COMPLEX

    @staticmethod
    def fix_number_precision(number):
        if cmath.isclose(number, 0, abs_tol=CALCULATOR_ERROR):
            return 0
        return number

    def get_description(self):
        translator = Language().get_translator('calculator')

        if self.has_boolean:
            return translator('query-boolean') if self.has_boolean else ''
        value_type = self.value_type
        if value_type == Calculation.VALUE_IMAGINARY:
            return translator('result-imaginary')
        if value_type == Calculation.VALUE_COMPLEX:
            return translator('result-complex')
        return ''

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

    @BaseCalculation.Decorators.handle_error_results
    def to_query_result(self):
        name = self.format()
        description = self.get_description()

        return QueryResult(
            icon='images/icon.svg',
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order
        )
