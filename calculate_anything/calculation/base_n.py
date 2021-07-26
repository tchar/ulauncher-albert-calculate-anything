from calculate_anything.calculation import Calculation
from calculate_anything.query.result import QueryResult
from calculate_anything.lang import LanguageService
from calculate_anything.utils.colors import hex_to_rgb, rgb_to_hsv, rgb_to_cmyk, rgb_to_hsl


__all__ = ['BaseNCalculation', 'Base16StringCalculation', 'Base10Calculation',
           'Base2Calculation', 'Base8Calculation', 'Base16Calculation', 'ColorBase16Calculation']


class BaseNCalculation(Calculation):
    def to_base_calculation(self, base_calculation_class, order=None):
        order = order if order is not None else self.order
        return base_calculation_class(value=self.value, query=self.query, order=order)

    def format(self):
        return str(self.value)

    def get_description(self):
        return ''

    @Calculation.Decorators.handle_error_results
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


class Base16StringCalculation(BaseNCalculation):
    def __init__(self, value=None, query='', error=None, order=0):
        value = ':'.join('{:02x}'.format(ord(c)) for c in value)
        super().__init__(value=value, query=query, error=error, order=order)

    def format(self):
        return self.value

    def get_description(self):
        return LanguageService().translate('bytes', 'calculator').upper()


class Base10Calculation(BaseNCalculation):
    def format(self):
        return str(self.value)

    def get_description(self):
        return LanguageService().translate('dec', 'calculator').upper()


class Base2Calculation(BaseNCalculation):
    def format(self):
        return bin(int(self.value))[2:]

    def get_description(self):
        return LanguageService().translate('bin', 'calculator').upper()


class Base8Calculation(BaseNCalculation):
    def format(self):
        return oct(int(self.value))[2:]

    def get_description(self):
        return LanguageService().translate('oct', 'calculator').upper()


class Base16Calculation(BaseNCalculation):
    def format(self):
        return hex(int(self.value))[2:]

    def get_description(self):
        return LanguageService().translate('hex', 'calculator').upper()


class ColorBase16Calculation(Base16Calculation):
    def __init__(self, value=None, query='', error=None, order=0, color_code=None, color_format=None):
        super().__init__(value=value, query=query, error=error, order=order)
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
        items.append(ColorBase16Calculation(
            value=rgb,
            query=query,
            order=order_offset,
            color_code='rgb',
            color_format='{:.0f}, {:.0f}, {:.0f}'
        ))

        for func, color_code, color_format in formats:
            value = func(rgb)
            items.append(
                ColorBase16Calculation(
                    value=value,
                    query=query,
                    order=len(items) + order_offset,
                    color_code=color_code,
                    color_format=color_format
                )
            )
        return items

    def format(self):
        return self.color_format.format(*self.value)

    def get_description(self):
        description = ''
        if self.color_code:
            description = LanguageService().translate(self.color_code, 'color').upper()
        return description

    @Base16Calculation.Decorators.handle_error_results
    def to_query_result(self):
        icon = 'images/color.svg'
        name = self.format()
        description = self.get_description()
        clipboard = name

        return QueryResult(
            icon=icon,
            value=self.value,
            name=name,
            description=description,
            clipboard=clipboard,
            order=self.order
        )
