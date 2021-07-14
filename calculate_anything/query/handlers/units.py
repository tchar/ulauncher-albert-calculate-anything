import math
import itertools
try:
    import pint
except ImportError:
    pint = None
from .interface import QueryHandlerInterface
from ...units import UnitsService
from ...currency import CurrencyService
from ...calculation import UnitsCalculation, CurrencyUnitsCalculation, TemperatureUnitsCalculation
from ...lang import Language
from ...logging_wrapper import LoggingWrapper as logging
from ...utils import is_types, Singleton
from ...constants import UNIT_QUERY_REGEX, UNIT_SPLIT_RE
from ...exceptions import MissingPintException

class UnitsQueryHandler(QueryHandlerInterface, metaclass=Singleton):
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    @staticmethod
    def _extract_query(query):
        matches = UNIT_QUERY_REGEX.findall(query)
        if matches:
            unit_from, units_to = matches[0]
            units_to = units_to.split(',')
        else:
            unit_from = query
            units_to = []

        unit_from = unit_from.strip()
        units_to = map(str.strip, units_to)
        units_to = list(dict.fromkeys(units_to))

        return unit_from, units_to

    def _get_all_possible_units(self, unit_from):
        ureg = UnitsService().unit_registry
        replacer = Language().get_replacer('units', ignorecase=True)

        unit_from_alt = replacer(unit_from)
        
        if unit_from_alt != unit_from:
            yield unit_from_alt

        matches = UNIT_SPLIT_RE.split(unit_from)
        if len(matches) in [0, 1]:
            return
        expression_fmt = '{}'.join(matches[0::2])

        keys_dict = {}
        keys_set = {}
        for match in matches[1::2]:
            if match in keys_dict:
                continue
            keys_dict[match] = {}
            keys_set[match] = set()
            units = ureg.parse_unit_name(match)
            for unit in units:
                main_unit = unit[1]
                unit = ''.join(unit)
                keys_dict[match][main_unit] = unit
                keys_set[match].add(main_unit)

        units_seen = set()
        disjoint_groups = []
        for key in keys_dict:
            group = []
            for unit in keys_dict[key]:
                if unit in units_seen:
                    continue
                units_seen.add(unit)
                group.append(unit)
            if group:
                disjoint_groups.append(sorted(group))

        for g in itertools.product(*disjoint_groups):
            g_set = set(g)
            expression = []
            for m in matches[1::2]:
                units_set = g_set.intersection(keys_set[m])
                if len(units_set) != 1:
                    break
                unit = next(iter(units_set))
                value = keys_dict[m][unit]
                expression.append(value)
            else:
                expression = expression_fmt.format(*expression)
                yield expression

    def _get_only_one_unit(self, unit_from):
        translator = Language().get_translator('units')
        replacer = Language().get_replacer('units', ignorecase=True)

        unit_from_alt = replacer(unit_from)
        
        if unit_from_alt != unit_from:
            yield unit_from_alt

        matches = UNIT_SPLIT_RE.split(unit_from)
        if len(matches) in [0, 1]:
            return

        yield unit_from
        
        units = matches[1::2]
        units_alt = []
        for unit in units:
            unit_lower = unit.lower()
            unit_alt = translator(unit_lower)
            if unit_alt != unit_lower:
                units_alt.append(unit_alt)
            else:
                units_alt.append(unit)

        unit_from_alt = zip(matches[::2], matches[1::2])
        unit_from_alt = map(lambda u: u[0] + u[1], unit_from_alt)
        unit_from_alt = ''.join(unit_from_alt)
        if unit_from_alt != unit_from:
            yield unit_from_alt

    def _get_possible_units(self, unit_from):
        if UnitsService().unit_conversion_mode == UnitsService.MODE_NORMAL:
            return self._get_only_one_unit(unit_from)
        if UnitsService().unit_conversion_mode == UnitsService.MODE_CRAZY:
            return self._get_all_possible_units(unit_from)
        return self._get_only_one_unit(unit_from)

    def _parse_safe(self, expression):
        try:
            unit = UnitsService().unit_registry.parse_expression(expression)
            if not isinstance(unit, pint.Quantity):
                return None
            if (UnitsService().unit_conversion_mode == UnitsService.MODE_NORMAL and
                CurrencyUnitsCalculation.has_currency(unit) and
                not CurrencyUnitsCalculation.is_currency(unit)):
                return None
            return unit
        except pint.errors.DimensionalityError: pass
        except pint.errors.UndefinedUnitError: pass
        except pint.errors.DefinitionSyntaxError: pass
        except Exception as e:
            self._logger.error(e)
    
    def handle(self, query):
        if not UnitsService().running:
            return None
        elif '%' in query or query.strip() == '':
            return None

        if pint is None:
            return [UnitsCalculation(error=MissingPintException)]
        
        query = UnitsQueryHandler._extract_query(query)
        if not query:
            return None

        ureg = UnitsService().unit_registry
        base_currency = UnitsService().base_currency
        unit_from, units_to = query
        
        units_from_ureg_set = set()
        units_from_ureg = []
        with ureg.context('currency'):
            for expression in self._get_possible_units(unit_from):
                unit_from_ureg = self._parse_safe(expression)
                if unit_from_ureg is None:
                    continue
                units_from_ureg_str = str(units_from_ureg)
                if units_from_ureg_str in units_from_ureg_set:
                    continue
                units_from_ureg.append(unit_from_ureg)
                units_from_ureg_set.add(units_from_ureg_str)

        if not units_to:
            # Add currency units if compattible with units from and map them to units
            units_to_curr = CurrencyService().default_currencies
            units_to_curr = map(lambda s: 'currency_{}'.format(s), units_to_curr)
            units_to_curr = map(ureg.parse_unit_name, units_to_curr)
            units_to_curr = map(lambda u: ' '.join(u[0]) if u else '', units_to_curr)
            units_to_curr = map(ureg.parse_units, units_to_curr)
            units_to_curr = filter(base_currency.is_compatible_with, units_to_curr)

            # Add all units from
            units_to_rest = filter(lambda u: not base_currency.is_compatible_with(u), units_from_ureg)
            units_to_rest = map(lambda u: u.units, units_to_rest)
            units_to_ureg = itertools.chain(units_to_curr, units_to_rest)
        else:
            # Map to units and filter out if not compatible
            units_to_ureg = map(self._get_possible_units, units_to)
            units_to_ureg = itertools.chain.from_iterable(units_to_ureg)
            units_to_ureg = map(self._parse_safe, units_to_ureg)
            units_to_ureg = filter(is_types(pint.Quantity), units_to_ureg)
            # units_to_ureg = filter(lambda u: not u.units.unitless, units_to_ureg)
            units_to_ureg = filter(lambda u: u.magnitude == 1, units_to_ureg)
            units_to_ureg = map(lambda u: u.units, units_to_ureg)

        items = []
        for unit_from_ureg, unit_to_ureg in itertools.product(units_from_ureg, units_to_ureg):
            try:
                if not unit_from_ureg.is_compatible_with(unit_to_ureg):
                    continue
                unit_converted = unit_from_ureg.to(unit_to_ureg, 'currency')
                if math.isnan(unit_converted.magnitude): continue
                try: 
                    rate = unit_converted.magnitude / unit_from_ureg.magnitude
                    rate = ureg.Quantity(rate, unit_to_ureg)
                except ZeroDivisionError:
                    rate = None
            except Exception as e:
                self._logger.error(e)
                continue

            kwargs = {}
            if UnitsCalculation.has_currency(unit_converted):
                UnitClass = CurrencyUnitsCalculation
                kwargs = {'update_timestamp': UnitsService().get_rate_timestamp(unit_to_ureg)}
            elif UnitsCalculation.has_temperature(unit_converted):
                UnitClass = TemperatureUnitsCalculation
            else:
                UnitClass = UnitsCalculation
            
            items.append(
                UnitClass(
                    value=unit_converted,
                    rate=rate,
                    unit_from=unit_from_ureg.units,
                    unit_to=unit_to_ureg,
                    order=len(items),
                    **kwargs
                )
            )
        return items
