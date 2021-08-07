import re
from typing import Union
from calculate_anything.calculation.base import Calculation
from calculate_anything.query.result import QueryResult
from calculate_anything.lang import LanguageService
from calculate_anything.utils import multi_re, images_dir


__all__ = ['CalculatorCalculation', 'BooleanCalculation']


class CalculatorCalculation(Calculation):
    def __init__(
        self,
        value: Union[int, float, complex, bool],
        query: str,
        order: int = 0,
    ) -> None:
        super().__init__(value, query, order)

    def get_description(self) -> str:
        translator = LanguageService().get_translator('calculator')

        value_type = self.value_type
        if value_type == Calculation.ValueType.IMAGINARY:
            return translator('result-imaginary').capitalize()
        if value_type == Calculation.ValueType.COMPLEX:
            return translator('result-complex').capitalize()
        return ''

    def format_query(self) -> str:
        def sub_i(match: 're.Match') -> str:
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
            '==': '=',
        }

        query = self.query
        query = re.sub(r'\d+j', sub_i, query)
        query = re.split(
            r'(\/\/|\*\*|\=\=|\>\=|\<\=|[\+\-\/\*\%\^\>\<])', query
        )
        query = map(str.strip, query)
        query = ' '.join(query)
        query = multi_re.sub_dict(replace_special, query, sort=True)
        return query

    def format(self) -> str:
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

    def to_query_result(self) -> QueryResult:
        name = self.format()
        description = self.format_query()
        description_paren = self.get_description()
        if description_paren:
            description = '{} ({})'.format(description, description_paren)

        return QueryResult(
            icon=images_dir('icon.svg'),
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )


class BooleanCalculation(CalculatorCalculation):
    def to_query_result(self) -> QueryResult:
        translator = LanguageService().get_translator('calculator')
        result = str(self.value).lower()

        description = self.format_query()
        result_is_bool_str = translator('result-boolean').capitalize()
        description = '{} ({})'.format(description, result_is_bool_str)

        return QueryResult(
            icon=images_dir('icon.svg'),
            name=result,
            description=description,
            clipboard=result,
            value=self.value,
        )
