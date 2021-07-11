from .calculation import Calculation
from ..query.result import QueryResult
from ..lang import Language
from ..utils import hex_to_rgb, rgb_to_hsv, rgb_to_cmyk, rgb_to_hsl

class BaseNCalculation(Calculation):
    @staticmethod
    def _get_query_result(icon='images/icon.svg' ,name='', description='', clipboard=''):
        return QueryResult(
            icon=icon,
            name=name,
            description=description,
            clipboard=clipboard
        )

    def to_base_calculation(self, base_calculation_class, order=None):
        order = order if order is not None else self.order
        return base_calculation_class(value=self.value, query=self.query, order=order)

    @Calculation.Decorators.handle_error_results
    def to_query_result(self):
        return BaseNCalculation._get_query_result(name=str(self.value))

class Base16StringCalculation(BaseNCalculation):
    @BaseNCalculation.Decorators.handle_error_results
    def to_query_result(self):
        name = ":".join("{:02x}".format(ord(c)) for c in self.value)
        description = Language().translate('bytes', 'calculator').upper()
        clipboard = name
        return BaseNCalculation._get_query_result(name=name, description=description, clipboard=clipboard)

class Base10Calculation(BaseNCalculation):
    @BaseNCalculation.Decorators.handle_error_results
    def to_query_result(self):
        name = str(int(self.value))
        description = Language().translate('dec', 'calculator').upper()
        clipboard = name
        return BaseNCalculation._get_query_result(name=name, description=description, clipboard=clipboard)

class Base2Calculation(BaseNCalculation):
    @BaseNCalculation.Decorators.handle_error_results
    def to_query_result(self):
        name = bin(int(self.value))[2:]
        description = Language().translate('bin', 'calculator').upper()
        clipboard = name
        return BaseNCalculation._get_query_result(name=name, description=description, clipboard=clipboard)

class Base8Calculation(BaseNCalculation):
    @BaseNCalculation.Decorators.handle_error_results
    def to_query_result(self):
        name = oct(int(self.value))[2:]
        description = Language().translate('oct', 'calculator').upper()
        clipboard = name
        return BaseNCalculation._get_query_result(name=name, description=description, clipboard=clipboard)

class Base16Calculation(BaseNCalculation):
    @BaseNCalculation.Decorators.handle_error_results
    def to_query_result(self):
        name = hex(int(self.value))[2:]
        description = Language().translate('hex', 'calculator').upper()
        clipboard = name
        return BaseNCalculation._get_query_result(name=name, description=description, clipboard=clipboard)

class ColorBase16Calculation(Base16Calculation):
    def __init__(self, value=None, query='', error=None, order=0, color_code=None, color_format=None):
        super().__init__(value=value, query=query, error=error, order=order)
        self.color_code = color_code
        self.color_format = color_format or '{:.2f}, {:.2f}, {:.2f}'

    @staticmethod
    def get_color_calculations(value, order_offset):
        formats = [
            (rgb_to_hsv, 'hsv', '{:.0f}, {:.0f}%, {:.0f}%'),
            (rgb_to_hsl, 'hsl', '{:.0f}, {:.0f}%, {:.0f}%'),
            (rgb_to_cmyk, 'cmyk', '{:.0f}%, {:.0f}%, {:.0f}%, {:.0f}%'),
        ]

        items = []

        rgb = hex_to_rgb(value)
        items.append(ColorBase16Calculation(
                value=rgb,
                order=order_offset + 1,
                color_code='rgb',
                color_format='{:.0f}, {:.0f}, {:.0f}'
            )
        )

        for func, color_code, color_format in formats:
            value = func(rgb)
            items.append(
                ColorBase16Calculation(
                    value=value,
                    order=len(items) + order_offset,
                    color_code=color_code,
                    color_format=color_format
                )
            )
        return items
        

    @Base16Calculation.Decorators.handle_error_results
    def to_query_result(self):
        icon = 'images/color.svg'
        name = self.color_format.format(*self.value)
        description = ''
        if self.color_code:
            description = Language().translate(self.color_code, 'color').upper()
        clipboard = name
        return BaseNCalculation._get_query_result(icon=icon, name=name, description=description, clipboard=clipboard)