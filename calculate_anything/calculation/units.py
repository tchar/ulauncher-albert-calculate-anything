import locale
from datetime import datetime
try: import babel
except ImportError: babel = None

try: import babel.units as babel_units
except ImportError: babel_units = None

from .base import _Calculation
from ..query.result import QueryResult
from ..lang import Language
from ..logging_wrapper import LoggingWrapper as logging
from ..utils import replace_dict_re_func
from ..constants import FLAGS, TIME_DATETIME_FORMAT_NUMBERS, UNIT_CURRENCY_RE

class UnitsCalculation(_Calculation):
    
    def __init__(self, value=None, error=None, order=0,
                rate=None, unit_from=None, unit_to=None):
        super().__init__(value=value, error=error, order=order)
        self.rate = rate
        self.unit_from = unit_from
        self.unit_to = unit_to
        self._logger = logging.getLogger(__name__)
    
    @staticmethod
    def is_strictly_dimensionless(unit):
        return not unit.unitless and unit.dimensionless

    @staticmethod
    def has_temperature(unit):
        return '[temperature]' in unit.dimensionality

    @staticmethod
    def has_currency(unit):
        return '[currency]' in unit.dimensionality

    @staticmethod
    def is_currency(unit):
        return unit.dimensionality == '[currency]'

    def _format_babel(self):
        if not babel:
            raise Exception('Babel Missing')
        _locale = locale.getlocale()[0]
        
        name = self.value.format_babel(locale=_locale, spec='g')
        if self.rate is None:
            return name, ''

        unit_from_name = self.unit_from.format_babel(locale=_locale, spec='g')
        rate = self.rate.format_babel(locale=_locale, spec='g')

        description = '1 {} = {}'.format(unit_from_name, rate)
        return name, description

    def format(self):
        use_translator = True
        if babel:
            try:
                name, description = self._format_babel()
                use_translator = False
            except Exception: pass

        if use_translator:
            translator = Language().get_translator('units')

            unit_name = str(self.value.units)
            unit_to_name = str(self.unit_to)

            unit_name = translator(unit_name)
            name = '{:g} {}'.format(self.value.magnitude, unit_name)

            if self.rate is not None:
                unit_to_name = translator(unit_name)
                description = '{:g} {}'.format(self.rate.magnitude, unit_to_name)
            else:
                description = ''
        
        replace_func = replace_dict_re_func({'**': '^', '_': ' '}, sort=False)
        name = replace_func(name)
        description = replace_func(description)

        return name, description

    @_Calculation.Decorators.handle_error_results
    def to_query_result(self):
        name, description = self.format()
        
        if self.unit_from == self.unit_to:
            description = ''
            
        descriptions = [description]
        if UnitsCalculation.is_strictly_dimensionless(self.value):
            descriptions.append(Language().translate('result-dimensionless', 'calculator'))
        
        description = ' '.join(descriptions)
        icon = 'images/convert.svg'

        return QueryResult(
            icon=icon,
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )

class TemperatureUnitsCalculation(UnitsCalculation):
    def format(self):
        parse_default = True
        if babel_units:
            try:
                _locale = locale.getlocale()[0]
                unit_name = str(self.value.units).replace('degree_', 'temperature-', 1).lower()
                name = babel_units.format_unit(self.value.magnitude, unit_name, locale=_locale, format='#,##0.##;-#')
                parse_default = False
            except Exception:
                pass
        
        if parse_default:
            unit_name = str(self.value.units)
            name = '{:g} {}'.format(self.value.magnitude, unit_name)
        
        name = replace_dict_re_func({'**': '^', '_': ' '}, sort=False)(name)
        return name, ''

class CurrencyUnitsCalculation(UnitsCalculation):
        def __init__(self, value=None, error=None, order=0,
                rate=None, unit_from=None, unit_to=None, update_timestamp=None):
            super().__init__(value=value, error=error, order=order,
                             rate=rate, unit_from=unit_from, unit_to=unit_to)
            self.update_timestamp = update_timestamp

        def format(self):
            replace_func = replace_dict_re_func({'currency_': '', '**': '^', '_': ' '}, sort=False)

            unit_name = replace_func(str(self.value.units))
            converted_amount = locale.currency(self.value.magnitude, symbol='', grouping=True)

            name = '{} {}'.format(converted_amount, unit_name)
            if self.rate is None:
                return name, ''

            unit_from_name = replace_func(str(self.unit_from))
            unit_to_name = replace_func(str(self.unit_to))

            rate_amount = '{:.6f}'.format(self.rate.magnitude)

            description = '1 {} = {} {}'.format(unit_from_name, rate_amount, unit_to_name)
            if self.update_timestamp is not None:
                date = datetime.fromtimestamp(self.update_timestamp).strftime(TIME_DATETIME_FORMAT_NUMBERS)
                description = '{} as of {}'.format(description, date)

            return name, description
    
        @UnitsCalculation.Decorators.handle_error_results
        def to_query_result(self):
            name, description = self.format()

            if self.unit_from == self.unit_to:
                description = ''
            
            unit_to_name = UNIT_CURRENCY_RE.findall(str(self.unit_to))
            if unit_to_name:
                unit_to_name = unit_to_name[0]
            else:
                unit_to_name = str(self.unit_to).replace('currency_', '', 1).replace()
            
            if unit_to_name in FLAGS:
                icon = 'images/flags/{}'.format(FLAGS[unit_to_name])
            else:
                icon = 'images/currency.svg'

            return QueryResult(
                icon=icon,
                name=name,
                description=description,
                clipboard=name,
                value=self.value,
                order=self.order,
            )