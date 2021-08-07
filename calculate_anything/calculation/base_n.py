from typing import Tuple, Type, Union
from calculate_anything.calculation import CalculatorCalculation
from calculate_anything.query.result import QueryResult
from calculate_anything.lang import LanguageService
from calculate_anything.utils import images_dir
from calculate_anything.utils.colors import (
    hex_to_rgb,
    rgb_to_hsv,
    rgb_to_cmyk,
    rgb_to_hsl,
)


__all__ = [
    'BaseNCalculation',
    'Base16StringCalculation',
    'Base10Calculation',
    'Base2Calculation',
    'Base8Calculation',
    'Base16Calculation',
    'ColorBase16Calculation',
]


class BaseNCalculation(CalculatorCalculation):
    def to_base_calculation(
        self,
        base_calculation_class: Type['BaseNCalculation'],
        order: bool = None,
    ) -> 'BaseNCalculation':
        order = order if order is not None else self.order
        return base_calculation_class(self.value, self.query, order)

    def format(self) -> str:
        return str(self.value)

    def get_description(self) -> str:
        return ''

    def to_query_result(self) -> QueryResult:
        name = self.format()
        description = self.get_description()
        return QueryResult(
            icon=images_dir('icon.svg'),
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )


class Base16StringCalculation(BaseNCalculation):
    def __init__(self, value: str, query: str, order: int = 0) -> None:
        value = ':'.join('{:02x}'.format(ord(c)) for c in value)
        super().__init__(value, query, order)

    def format(self) -> str:
        return self.value

    def get_description(self) -> str:
        return LanguageService().translate('bytes', 'calculator').upper()


class Base10Calculation(BaseNCalculation):
    def get_description(self) -> str:
        return LanguageService().translate('dec', 'calculator').upper()


class Base2Calculation(BaseNCalculation):
    def format(self) -> str:
        return bin(int(self.value))[2:]

    def get_description(self) -> str:
        return LanguageService().translate('bin', 'calculator').upper()


class Base8Calculation(BaseNCalculation):
    def format(self) -> str:
        return oct(int(self.value))[2:]

    def get_description(self) -> str:
        return LanguageService().translate('oct', 'calculator').upper()


class Base16Calculation(BaseNCalculation):
    def format(self) -> str:
        return hex(int(self.value))[2:]

    def get_description(self) -> str:
        return LanguageService().translate('hex', 'calculator').upper()


class ColorBase16Calculation(Base16Calculation):
    def __init__(
        self,
        value: Tuple[Union[float, int], ...],
        color_code: str,
        color_format: str,
        query: str,
        order: int = 0,
    ):
        super().__init__(value, query, order)
        self.color_code = color_code
        self.color_format = color_format or '{:.2f}, {:.2f}, {:.2f}'

    @staticmethod
    def get_color_calculations(value, query, order_offset):
        formats = [
            (rgb_to_hsv, 'hsv', '{:.0f}, {:.0%}, {:.0%}'),
            (rgb_to_hsl, 'hsl', '{:.0f}, {:.0%}, {:.0%}'),
            (rgb_to_cmyk, 'cmyk', '{:.0%}, {:.0%}, {:.0%}, {:.0%}'),
        ]

        items = []

        rgb = hex_to_rgb(value)
        items.append(
            ColorBase16Calculation(
                rgb,
                'rgb',
                '{:.0f}, {:.0f}, {:.0f}',
                query,
                order_offset,
            )
        )

        for func, color_code, color_format in formats:
            value = func(rgb)
            items.append(
                ColorBase16Calculation(
                    value,
                    color_code,
                    color_format,
                    query,
                    len(items) + order_offset,
                )
            )
        return items

    def format(self) -> str:
        return self.color_format.format(*self.value)

    def get_description(self) -> str:
        description = ''
        if self.color_code:
            description = (
                LanguageService().translate(self.color_code, 'color').upper()
            )
        return description

    def to_query_result(self) -> QueryResult:
        icon = images_dir('color.svg')
        name = self.format()
        description = self.get_description()
        clipboard = name

        return QueryResult(
            icon=icon,
            value=self.value,
            name=name,
            description=description,
            clipboard=clipboard,
            order=self.order,
        )
