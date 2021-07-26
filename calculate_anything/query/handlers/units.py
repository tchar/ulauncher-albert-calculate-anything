import math
import itertools
try:
    import pint
except ImportError:  # pragma: no cover (covered artificially in tests)
    pint = None  # pragma: no cover
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything.units.service import UnitsService
from calculate_anything.currency.service import CurrencyService
from calculate_anything.calculation.units import (
    UnitsCalculation, CurrencyUnitsCalculation,
    TemperatureUnitsCalculation
)
from calculate_anything.lang import LanguageService
import calculate_anything.log as logging
from calculate_anything.utils.singleton import Singleton
from calculate_anything.utils.misc import is_types
from calculate_anything.constants import UNIT_QUERY_REGEX, UNIT_SPLIT_RE
from calculate_anything.exceptions import CurrencyProviderException, MissingPintException, MissingRequestsException


class UnitsQueryHandler(QueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__('=')
        self._logger = logging.getLogger(__name__)

    def _items_for_currency_errors(self, unit_dimensionalities):
        currency_service = CurrencyService()
        missing_requests = currency_service.enabled and currency_service.missing_requests
        currency_provider_had_error = currency_service.enabled and currency_service.provider_had_error

        missing_requests = currency_service.enabled and currency_service.missing_requests
        currency_provider_had_error = (
            currency_service.enabled and currency_service.provider_had_error and
            any(map(lambda d: '[currency]' in d, unit_dimensionalities))
        )
        if missing_requests:
            item = UnitsCalculation(
                error=MissingRequestsException,
                order=-1030
            )
            return [item]
        elif currency_provider_had_error:
            item = UnitsCalculation(error=CurrencyProviderException, order=-60)
            return [item]
        return []

    @staticmethod
    def _extract_query(query):
        matches = UNIT_QUERY_REGEX.findall(query)
        if not matches:
            return None

        unit_from, units_to = matches[0]
        units_to = units_to.split(',')

        unit_from = unit_from.strip()
        units_to = map(str.strip, units_to)
        units_to = filter(None, units_to)
        units_to = list(units_to)

        return unit_from, units_to

    def _get_all_possible_units(self, unit_from):
        ureg = UnitsService().unit_registry
        replacer = LanguageService().get_replacer('units', ignorecase=True)

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
        yield unit_from

    def _get_only_one_unit(self, unit_from):
        translator = LanguageService().get_translator('units')
        replacer = LanguageService().get_replacer('units', ignorecase=True)

        unit_from_alt = replacer(unit_from)
        if unit_from_alt != unit_from:
            yield unit_from_alt

        matches = UNIT_SPLIT_RE.split(unit_from)
        if len(matches) in [0, 1]:
            return

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
        yield unit_from

    def _get_possible_units(self, unit_from):
        if UnitsService().conversion_mode == UnitsService.CONVERSION_MODE_NORMAL:
            return self._get_only_one_unit(unit_from)
        if UnitsService().conversion_mode == UnitsService.CONVERSION_MODE_CRAZY:
            return self._get_all_possible_units(unit_from)
        return self._get_only_one_unit(unit_from)

    def _parse_safe(self, expression):
        try:
            unit = UnitsService().unit_registry.parse_expression(expression)
            if not isinstance(unit, pint.Quantity):
                return None
            if (UnitsService().conversion_mode == UnitsService.CONVERSION_MODE_NORMAL and
                CurrencyUnitsCalculation.has_currency(unit) and
                    not CurrencyUnitsCalculation.is_currency(unit)):
                return None
            return unit
        except pint.errors.DimensionalityError:
            pass
        except pint.errors.UndefinedUnitError:
            pass
        except pint.errors.DefinitionSyntaxError:
            pass
        except Exception as e:
            self._logger.error(e)

    def handle_raw(self, query):
        if '%' in query:
            return None
        if pint is None:
            item = UnitsCalculation(
                error=MissingPintException,
                order=-1020
            )
            return [item]
        if not UnitsService().running:
            return None

        query = UnitsQueryHandler._extract_query(query)
        if not query:
            return None

        ureg = UnitsService().unit_registry
        base_currency = UnitsService().base_currency
        unit_from, units_to = query

        unit_from_ureg_currency = None
        unit_dimensionalities = set()
        units_from_ureg = []
        with ureg.context('currency'):
            for expression in self._get_possible_units(unit_from):
                unit_from_ureg = self._parse_safe(expression)
                if unit_from_ureg is None:
                    continue
                unit_from_ureg_dim = unit_from_ureg.dimensionality
                if unit_from_ureg_dim in unit_dimensionalities:
                    continue
                if UnitsCalculation.is_currency(unit_from_ureg):
                    unit_from_ureg_currency = unit_from_ureg
                units_from_ureg.append(unit_from_ureg)
                unit_dimensionalities.add(unit_from_ureg_dim)

        items = []
        items.extend(self._items_for_currency_errors(unit_dimensionalities))

        if not units_to:
            # Add currency units if compattible with units from and map them to units
            if unit_from_ureg_currency:
                unit_from_ureg_currency_str = str(
                    unit_from_ureg_currency.units)
            else:
                unit_from_ureg_currency_str = None

            units_to_curr = CurrencyService().default_currencies
            units_to_curr = map(
                lambda s: 'currency_{}'.format(s), units_to_curr)
            units_to_curr = filter(
                lambda s: s != unit_from_ureg_currency_str, units_to_curr)
            units_to_curr = map(ureg.parse_unit_name, units_to_curr)
            units_to_curr = map(lambda u: ' '.join(
                u[0]) if u else '', units_to_curr)
            units_to_curr = map(ureg.parse_units, units_to_curr)
            units_to_curr = filter(
                base_currency.is_compatible_with, units_to_curr)

            # Add all units from
            units_to_rest = filter(
                lambda u: not base_currency.is_compatible_with(u), units_from_ureg)
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

        added_currency = False
        for unit_from_ureg, unit_to_ureg in itertools.product(units_from_ureg, units_to_ureg):
            try:
                if not unit_from_ureg.is_compatible_with(unit_to_ureg):
                    continue
                unit_converted = unit_from_ureg.to(unit_to_ureg, 'currency')
                if math.isnan(unit_converted.magnitude):
                    self._logger.warning(
                        'Converted magnitude is NaN'': from={} {}, to={}'.format(
                            unit_from_ureg.magnitude,
                            unit_from_ureg.units,
                            unit_to_ureg
                        )
                    )
                    continue
                try:
                    rate = unit_converted.magnitude / unit_from_ureg.magnitude
                    rate = ureg.Quantity(rate, unit_to_ureg)
                except ZeroDivisionError:
                    rate = None
            except Exception as e:
                self._logger.error(e)
                continue

            kwargs = {}
            if UnitsCalculation.is_currency(unit_converted):
                added_currency = True
                # Continue in if same units, it will be added later
                if unit_converted.units == unit_from_ureg.units:
                    continue
                UnitClass = CurrencyUnitsCalculation
                kwargs = {
                    'update_timestamp': UnitsService().get_rate_timestamp(unit_to_ureg)
                }
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
                    query='{} {} to {}'.format(
                        unit_from_ureg.magnitude,
                        unit_from_ureg.units,
                        unit_to_ureg
                    ),
                    order=len(items),
                    **kwargs
                )
            )

        if unit_from_ureg_currency and added_currency:
            items.append(
                CurrencyUnitsCalculation(
                    value=unit_from_ureg_currency,
                    rate=None,
                    unit_from=unit_from_ureg_currency.units,
                    unit_to=unit_from_ureg_currency.units,
                    query='{0} {1} to {1}'.format(
                        unit_from_ureg_currency.magnitude,
                        unit_from_ureg_currency.units
                    ),
                    order=len(items),
                    update_timestamp=None
                )
            )
        return items

    @QueryHandler.Decorators.can_handle
    def handle(self, query):
        return self.handle_raw(query)
