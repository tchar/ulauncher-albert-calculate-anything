import math
from itertools import product, chain
import tokenize
try:
    import pint
except ImportError:  # pragma: no cover (covered artificially in tests)
    pint = None  # pragma: no cover
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything.units import UnitsService
from calculate_anything.currency import CurrencyService
from calculate_anything.calculation import (
    UnitsCalculation, CurrencyUnitsCalculation,
    TemperatureUnitsCalculation
)
from calculate_anything.lang import LanguageService
from calculate_anything import logging
from calculate_anything.utils import is_types, Singleton
from calculate_anything.regex import UNIT_QUERY_SPLIT_RE, UNIT_SPLIT_RE
from calculate_anything.exceptions import (
    CurrencyProviderException, MissingPintException, ZeroDivisionException
)


__all__ = ['UnitsQueryHandler']


class UnitsQueryHandler(QueryHandler, metaclass=Singleton):
    def __init__(self):
        super().__init__('=')
        self._logger = logging.getLogger(__name__)

    def _items_for_currency_errors(self, units):
        dimensionalities = set(unit.dimensionality for unit in units)
        currency_service = CurrencyService()
        currency_provider_had_error = currency_service.enabled and \
            currency_service.provider_had_error

        currency_provider_had_error = (
            currency_service.enabled and
            currency_service.provider_had_error and
            any(map(lambda d: '[currency]' in d, dimensionalities))
        )
        if currency_provider_had_error:
            item = UnitsCalculation(
                error=CurrencyProviderException(),
            )
            return [item]
        return []

    @staticmethod
    def _extract_query(query):
        query = UNIT_QUERY_SPLIT_RE.split(query, maxsplit=1)

        unit_from = query[0].strip()
        units_to = []
        if len(query) == 1:
            return unit_from, units_to

        units_to = query[1].split(',')
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

        for g in product(*disjoint_groups):
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
        # TODO: To be removed
        # yield unit_from

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
        if UnitsService().conversion_mode == UnitsService.ConversionMode.CRAZY:
            return self._get_all_possible_units(unit_from)
        return self._get_only_one_unit(unit_from)

    def _parse_safe(self, expression):
        unit = None
        error_to_show = None
        try:
            unit = UnitsService().unit_registry.parse_expression(expression)
            if UnitsCalculation.is_strictly_dimensionless(unit):
                unit = None
            if (UnitsService().conversion_mode ==
                UnitsService.ConversionMode.NORMAL and
                CurrencyUnitsCalculation.has_currency(unit) and
                    not CurrencyUnitsCalculation.is_currency(unit)):
                unit = None
        except TypeError:
            pass
        except ZeroDivisionError:
            extra = {'icon': 'images/convert.svg'}
            error_to_show = ZeroDivisionException(extra=extra)
        except (pint.errors.DimensionalityError,
                pint.errors.UndefinedUnitError,
                pint.errors.DefinitionSyntaxError,
                tokenize.TokenError) as e:
            self._logger.debug(
                'Got pint exception when trying to parse {!r}: {}'
                .format(expression, e))
        except Exception as e:  # pragma no cover
            self._logger.exception(  # pragma no cover
                'Got exception when trying to parse: {!r}: {}'
                .format(expression, e))

        return unit, error_to_show

    def handle_raw(self, query):
        if '%' in query:
            return None
        if pint is None:
            item = UnitsCalculation(
                error=MissingPintException(),
            )
            return [item]
        if not UnitsService().running:
            return None

        original_query = query
        query = UnitsQueryHandler._extract_query(query)

        ureg = UnitsService().unit_registry
        base_currency = UnitsService().base_currency
        unit_from, units_to = query

        parse_err = None
        unit_from_ureg_currency = None
        unit_set = set()
        units_from_ureg = []
        with ureg.context('currency'):
            for expression in self._get_possible_units(unit_from):
                unit_from_ureg, parse_err = self._parse_safe(expression)
                if parse_err:
                    break
                if unit_from_ureg is None:
                    continue
                unit_from_ureg_unit = unit_from_ureg.units
                if unit_from_ureg_unit in unit_set:
                    continue
                if UnitsCalculation.is_currency(unit_from_ureg):
                    unit_from_ureg_currency = unit_from_ureg
                units_from_ureg.append(unit_from_ureg)
                unit_set.add(unit_from_ureg_unit)

        if parse_err:
            suffix = ', '.join(units_to)
            suffix = ' to {}'.format(suffix) if suffix else ''
            query = '{}{}'.format(expression, suffix)
            item = UnitsCalculation(query=query, error=parse_err)
            return [item]

        items = []
        items.extend(self._items_for_currency_errors(unit_set))

        if not units_to:
            # Add currency units if compattible with units from
            # and map them to units
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
                lambda u: not base_currency.is_compatible_with(u),
                units_from_ureg)
            units_to_rest = map(lambda u: u.units, units_to_rest)
            units_to_ureg = chain(units_to_curr, units_to_rest)
        else:
            # Map to units and filter out if not compatible
            units_to_ureg = map(self._get_possible_units, units_to)
            units_to_ureg = chain.from_iterable(units_to_ureg)
            units_to_ureg = map(self._parse_safe, units_to_ureg)
            units_to_ureg = filter(lambda u: u[1] is None, units_to_ureg)
            units_to_ureg = map(lambda u: u[0], units_to_ureg)
            units_to_ureg = filter(is_types(pint.Quantity), units_to_ureg)
            units_to_ureg = filter(lambda u: u.magnitude == 1, units_to_ureg)
            units_to_ureg = map(lambda u: u.units, units_to_ureg)

        added_currency = False
        for unit_from_ureg, unit_to_ureg in product(units_from_ureg,
                                                    units_to_ureg):
            try:
                if not unit_from_ureg.is_compatible_with(unit_to_ureg):
                    continue
                unit_converted = unit_from_ureg.to(unit_to_ureg, 'currency')
                if math.isnan(unit_converted.magnitude):
                    self._logger.warning(
                        'Converted magnitude is NaN'': from={} {}, to={}'
                        .format(
                            unit_from_ureg.magnitude,
                            unit_from_ureg.units,
                            unit_to_ureg
                        )
                    )
                    continue
                Q = ureg.Quantity
                rate = Q(1, unit_from_ureg.units)
                rate = rate.to(Q(1, unit_converted.units), 'currency')
            except Exception as e:  # pragma no cover
                self._logger.exception(  # pragma no cover
                    'Unexpected exception uni units conversion: {!r}: {}'
                    .format(original_query, e))
                continue  # pragma no cover

            kwargs = {}
            if UnitsCalculation.is_currency(unit_converted):
                added_currency = True
                # Continue in if same units, it will be added later
                if unit_converted.units == unit_from_ureg.units:
                    continue
                UnitClass = CurrencyUnitsCalculation
                timestamp = UnitsService().get_rate_timestamp(unit_to_ureg)
                kwargs = {
                    'update_timestamp': timestamp
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
            Q = ureg.Quantity
            items.append(
                CurrencyUnitsCalculation(
                    value=unit_from_ureg_currency,
                    rate=Q(1.0, unit_from_ureg_currency.units),
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
