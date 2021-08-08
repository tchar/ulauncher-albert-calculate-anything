import locale
from datetime import datetime
import re
from typing import Tuple, Union

try:
    import pint
except ImportError:
    pass
try:
    import babel.units as babel_units
except ImportError:
    babel_units = None
try:
    import babel.numbers as babel_numbers
except ImportError:
    babel_numbers = None
from calculate_anything import logging
from calculate_anything.calculation.base import Calculation
from calculate_anything.query.result import QueryResult
from calculate_anything.lang import LanguageService
from calculate_anything.utils import multi_re, images_dir
from calculate_anything.constants import FLAGS, TIME_DATETIME_FORMAT_NUMBERS
from calculate_anything.regex import UNIT_CURRENCY_RE


__all__ = [
    'UnitsCalculation',
    'CurrencyUnitsCalculation',
    'TemperatureUnitsCalculation',
]


logger = logging.getLogger(__name__)


class UnitsCalculation(Calculation):
    def __init__(
        self,
        value: 'pint.Quantity',
        unit_from: 'pint.Unit',
        unit_to: 'pint.Unit',
        rate: 'pint.Quantity',
        query: str,
        order: int = 0,
    ) -> None:
        super().__init__(value, query, order)
        self.rate = rate
        self.unit_from = unit_from
        self.unit_to = unit_to

    @staticmethod
    def is_strictly_dimensionless(unit: 'pint.Quantity') -> bool:
        return unit.unitless and unit.dimensionless

    @staticmethod
    def has_temperature(unit: Union['pint.Quantity', 'pint.Unit']) -> bool:
        return '[temperature]' in unit.dimensionality

    @staticmethod
    def has_currency(unit: Union['pint.Quantity', 'pint.Unit']) -> bool:
        return '[currency]' in unit.dimensionality

    @staticmethod
    def is_currency(unit: Union['pint.Quantity', 'pint.Unit']) -> bool:
        dimensionality = unit.dimensionality
        return (
            '[currency]' in dimensionality
            and len(dimensionality) == 1
            and dimensionality['[currency]'] == 1
        )

    def _format_babel(self) -> Tuple[str, str]:
        _locale = locale.getlocale()[0]

        if not UnitsCalculation.is_strictly_dimensionless(self.value):
            name = self.value.format_babel(locale=_locale, spec='g')
        else:
            name = '{:g}'.format(self.value.magnitude)

        if not self.unit_from.dimensionless:
            unit_from_name = self.unit_from.format_babel(
                locale=_locale, spec='g'
            )
        else:
            unit_from_name = '{:g}'.format(self.unit_from)

        rate = self.rate.format_babel(locale=_locale, spec='g')
        if self.unit_from != self.unit_to:
            description = '1 {} = {}'.format(unit_from_name, rate)
        else:
            description = ''

        return name, description

    def format(self) -> Tuple[str, str]:
        use_translator = True
        if babel_units:
            try:
                name, description = self._format_babel()
                use_translator = False
            except Exception as e:
                msg = 'Babel: Could not translate units: {}'
                msg = msg.format(e)
                logger.exception(msg)

        translator = LanguageService().get_translator('units')
        if use_translator:
            unit_name = str(self.value.units)

            unit_name = translator(unit_name)
            name = '{:g} {}'.format(self.value.magnitude, unit_name)

            if self.unit_from != self.unit_to:
                unit_from_name = str(self.unit_from)
                description = '1 {} = {:g} {}'.format(
                    unit_from_name, self.rate.magnitude, unit_name
                )
            else:
                description = ''

        if not self.value.dimensionless:
            dimensionality = str(self.value.dimensionality)
            dimensionality = re.sub(
                r'\[(.*?)\]',
                lambda s: translator(s.group(0)[1:-1]),
                dimensionality,
            )
        else:
            dimensionality = ''

        if description and dimensionality:
            description = '{} • [{}]'.format(description, dimensionality)
        elif dimensionality:
            description = '[{}]'.format(dimensionality)
        else:
            description = ''

        replace_re = multi_re.compile({'**': '^', '_': ' '}, sort=False)
        name = replace_re.sub_dict(name)
        description = replace_re.sub_dict(description)

        return name, description

    def to_query_result(self) -> QueryResult:
        name, description = self.format()

        descriptions = [description]
        if UnitsCalculation.is_strictly_dimensionless(self.value):
            desc_part = (
                LanguageService()
                .translate('result-dimensionless', 'calculator')
                .capitalize()
            )
            descriptions.append(desc_part)

        description = ' '.join(descriptions)
        icon = images_dir('convert.svg')

        return QueryResult(
            icon=icon,
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )


class TemperatureUnitsCalculation(UnitsCalculation):
    def format(self) -> Tuple[str, str]:
        parse_default = True
        if babel_units:
            try:
                _locale = locale.getlocale()[0]
                unit_name = (
                    str(self.value.units)
                    .replace('degree_', 'temperature-', 1)
                    .lower()
                )
                name = babel_units.format_unit(
                    self.value.magnitude,
                    unit_name,
                    locale=_locale,
                    format='#,##0.##;-#',
                )
                parse_default = False
            except Exception as e:
                msg = 'Babel: Could not translate temperature units "{}": {}'
                msg = msg.format(self.value.units, e)
                logger.exception(msg)

        if parse_default:
            unit_name = str(self.value.units)
            name = '{:g} {}'.format(self.value.magnitude, unit_name)

        name = multi_re.sub_dict({'**': '^', '_': ' '}, name, sort=False)
        return name, '[temperature]'


class CurrencyUnitsCalculation(UnitsCalculation):
    def __init__(
        self,
        value: 'pint.Quantity',
        unit_from: 'pint.Unit',
        unit_to: 'pint.Unit',
        rate: 'pint.Quantity',
        update_timestamp,
        query: str,
        order: int = 0,
    ) -> None:
        super().__init__(value, unit_from, unit_to, rate, query, order)
        self.update_timestamp = update_timestamp

    @staticmethod
    def _currency_alias(currency_name: str) -> str:
        if babel_numbers is None:
            return currency_name
        try:
            if babel_numbers.is_currency(currency_name):
                return babel_numbers.get_currency_name(currency_name)
        except Exception as e:
            msg = 'Babel: Could not translate currency "{}": {}'
            msg = msg.format(currency_name, e)
            logger.exception(msg)
        return currency_name

    def format(self) -> Tuple[str, str]:
        def currency_alias_f(m: 're.Match') -> str:
            currency = m.group(0)[9:]
            currency_alias = CurrencyUnitsCalculation._currency_alias(currency)
            if currency == currency_alias:
                return currency
            return '{} ({})'.format(currency, currency_alias)

        replace_re = multi_re.compile(
            {'currency_': '', '**': '^', '_': ' '}, sort=True
        )

        unit_name = str(self.value.units)
        clipboard = replace_re.sub_dict(unit_name)

        if babel_units is not None:
            unit_name = re.sub(
                r'currency_([a-zA-Z]{3,})', currency_alias_f, unit_name
            )
        else:
            unit_name = clipboard

        try:
            converted_amount = locale.currency(
                self.value.magnitude, symbol='', grouping=True
            )
        except ValueError:
            converted_amount = '{:.2f}'.format(self.value.magnitude)

        name = '{} {}'.format(converted_amount, unit_name)
        clipboard = '{} {}'.format(converted_amount, clipboard)

        unit_from_name = str(self.unit_from)
        unit_from_name = replace_re.sub_dict(unit_from_name)

        unit_to_name = str(self.unit_to)
        unit_to_name = replace_re.sub_dict(unit_to_name)

        rate_amount = '{:.6f}'.format(self.rate.magnitude)

        description = '1 {} = {} {}'.format(
            unit_from_name, rate_amount, unit_to_name
        )
        if self.update_timestamp is not None:
            date = datetime.fromtimestamp(self.update_timestamp).strftime(
                TIME_DATETIME_FORMAT_NUMBERS
            )
            description = '{} as of {}'.format(description, date)

        return name, description, clipboard

    def to_query_result(self) -> QueryResult:
        name, description, clipboard = self.format()

        if self.unit_from == self.unit_to:
            description = ''

        unit_to_name = UNIT_CURRENCY_RE.findall(str(self.unit_to))
        if unit_to_name:
            unit_to_name = unit_to_name[0]
        else:
            unit_to_name = (
                str(self.unit_to).replace('currency_', '', 1).replace()
            )

        if unit_to_name in FLAGS:
            icon = FLAGS[unit_to_name]
            icon = images_dir('flags', icon)
        else:
            # Can't test this since we possible have all flags.
            icon = images_dir('currency.svg')  # pragma: no cover

        return QueryResult(
            icon=icon,
            name=name,
            description=description,
            clipboard=clipboard,
            value=self.value,
            order=self.order,
        )
