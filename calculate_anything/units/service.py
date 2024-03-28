import os
import math
from threading import RLock
from enum import Enum
from typing import Union

try:
    import pint
except ImportError:  # pragma: no cover
    pint = None
from calculate_anything.units.parser import PintDefinitionParser
from calculate_anything.currency import CurrencyService
from calculate_anything.currency.data import CurrencyData
from calculate_anything import logging
from calculate_anything.utils import Singleton, with_lock
from calculate_anything.constants import MAIN_DIR


__all__ = ['UnitsService']


logger = logging.getLogger(__name__)


class UnitsService(metaclass=Singleton):
    class ConversionMode(Enum):
        NORMAL = 0
        CRAZY = 1

    def __init__(self):
        self._lock = RLock()
        self._unit_registry = None
        self._ctx = None
        self._currencies_in_registry = set()
        self._base_currency = None
        self._enabled = False
        self._running = False
        self._currency_timestamps = {}
        self._conversion_mode = UnitsService.ConversionMode.NORMAL

    @property
    def lock(self):
        return self._lock

    @with_lock
    def _update_callback(self, data: CurrencyData, error: bool) -> None:
        if error:
            logger.warning('Provider had error, will not reset data')
            return
        if not data:
            logger.warning('Got empty data, will not reset data')
            return
        logger.info('Updating currency registry')
        ureg = self._unit_registry
        ctx = self._ctx

        updated_currencies = set()
        for currency, currency_info in data.items():
            if 'currency_' + currency not in ureg:
                ureg.define('currency_{} = nan currency_EUR'.format(currency))
                ureg.define('@alias currency_{0} = {0}'.format(currency))

            updated_currencies.add('currency_' + currency)
            currency_units = ureg('currency_' + currency)

            timestamp = currency_info['timestamp_refresh']
            self._currency_timestamps[str(currency_units.units)] = timestamp

            if currency_units.units == self._base_currency.units:
                continue
            rate = currency_info['rate']
            if rate == 0 or not math.isfinite(rate) or math.isnan(rate):
                continue
            ctx.redefine(
                'currency_{} = {} currency_EUR'.format(currency, 1 / rate)
            )

        for currency in self._currencies_in_registry:
            if currency in updated_currencies:
                continue
            if currency == 'currency_EUR':
                continue
            ctx.redefine('{} = nan currency_EUR'.format(currency))

        self._currencies_in_registry = updated_currencies
        logger.info(
            'Updated currency registry with {} currencies'.format(len(data))
        )

    def get_rate_timestamp(
        self, unit: Union['pint.Quantity', 'pint.Unit']
    ) -> float:
        if isinstance(unit, pint.Quantity):
            unit = unit.units
        unit_name = str(unit)
        return self._currency_timestamps.get(unit_name)

    def set_conversion_mode(self, mode: ConversionMode) -> 'UnitsService':
        self._conversion_mode = mode
        return self

    @property
    def conversion_mode(self) -> ConversionMode:
        return self._conversion_mode

    @property
    def base_currency(self) -> 'pint.Quantity':
        return self._base_currency

    @property
    @with_lock
    def unit_registry(self) -> 'pint.UnitRegistry':
        return self._unit_registry

    @property
    def enabled(self) -> bool:
        return self._enabled

    @property
    def running(self) -> bool:
        return self._running

    def enable(self) -> 'UnitsService':
        self._enabled = True
        return self

    def disable(self) -> 'UnitsService':
        self._enabled = False
        return self

    def stop(self) -> 'UnitsService':
        CurrencyService().remove_update_callback(self._update_callback)
        self._unit_registry = None
        self._base_currency = None
        self._running = False
        return self

    @with_lock
    def start(self, force: bool = False) -> 'UnitsService':
        if pint is None:
            return self
        if force:
            pass
        elif self._running:
            return self

        self._currencies_in_registry = set()
        self._unit_registry = pint.UnitRegistry(
            autoconvert_offset_to_baseunit=True, case_sensitive=False
        )
        self._ctx = pint.Context('currency')
        self._unit_registry.add_context(self._ctx)

        pint_parser = PintDefinitionParser(self._unit_registry)
        pint_parser.load_file(
            os.path.join(MAIN_DIR, 'data/currency/definitions.txt'),
            mode='units',
            is_currency=True,
        )
        pint_parser.load_file(
            os.path.join(MAIN_DIR, 'data/lang/currency.txt'),
            mode='units',
            is_currency=True,
        )
        pint_parser.load_file(
            os.path.join(MAIN_DIR, 'data/lang/units.txt'),
            mode='units',
            is_currency=False,
        )
        self._base_currency = self._unit_registry.Quantity(1, 'currency_EUR')
        CurrencyService().remove_update_callback(self._update_callback)
        CurrencyService().add_update_callback(self._update_callback)
        self._running = True
        return self
