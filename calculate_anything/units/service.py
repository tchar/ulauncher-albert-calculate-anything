import os

try:
    import pint
except ImportError:
    pint = None
from ..currency import CurrencyService
from ..lang import Language
from ..logging_wrapper import LoggingWrapper as logging
from ..utils import Singleton
from ..constants import MAIN_DIR, UNIT_ALIASES_RE

class UnitsService(metaclass=Singleton):
    MODE_NORMAL = 0
    MODE_CRAZY = 1

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._unit_registry = None
        self._ctx = None
        self._base_currency = None
        self._enabled = False
        self._running = False
        self._unit_conversion_mode = UnitsService.MODE_CRAZY
    
    def _load_extra_units(self, file_path, translation_mode, is_currency=True):
        def define_currency(currency, definition=None):
            currency_norm = currency.lstrip('currency_')
            currency_upper = 'currency_{}'.format(currency_norm.upper())
            definition = definition or 'nan currency EUR'

            if currency_upper not in self._unit_registry:
                self._unit_registry.define('{} = {}'.format(currency_upper, definition))
            self._unit_registry.define('@alias {} = {}'.format(currency_upper, currency_norm))
        
        def process_aliases(line):
            aliases = line.lstrip('@alias_').split('=')
            aliases = map(str.strip, aliases)
            root_alias = None
            aliases_to_define = []
            for alias in aliases:
                if not root_alias:
                    is_in_registry = alias in self._unit_registry
                    if not is_in_registry and is_currency:
                        define_currency(alias)
                    elif not is_in_registry:
                        return
                    root_alias = str(self._unit_registry(alias).units)
                    continue
                match = UNIT_ALIASES_RE.match(alias)
                if match:
                    aliases_to_define.append(alias)
                else:
                    translation_adder(alias.lower(), root_alias)
            if aliases_to_define:
                defstr = ' = '.join(aliases_to_define)
                defstr = '@alias {} = {}'.format(root_alias, defstr)
                self._unit_registry.define(defstr)

        def process_definition(line):
            line = line.split('=')
            if len(line) == 1:
                return
            line = map(str.strip, line)
            line = list(line)
            root_unit, rest_units = line[0], line[1:]
            rest_units = ' = '.join(rest_units)
            if is_currency:
                define_currency(root_unit, definition=rest_units)
            else:
                self._unit_registry.define('{} = {}'.format(root_unit, rest_units))

        def process_line(line):
            line = line.strip()
            if line.startswith('@alias '):
                process_aliases(line)
            else:
                process_definition(line)
                
        translation_adder = Language().get_translation_adder(translation_mode)
        import traceback
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    process_line(line)
            self._logger.info('Loaded unit definitions: {}'.format(file_path))
        except FileNotFoundError:
            self._logger.warning('Unit definitions file not found: {}'.format(file_path))
        except Exception as e:
            traceback.print_exc()
            self._logger.error('Exception when loading unit definitons file {}: {}'.format(file_path, e))

    def _update_callback(self, data):
        self._logger.info('Updating currency registry')
        ureg = self._unit_registry
        ctx = self._ctx

        for currency, currency_info in data.items():
            if 'currency_' + currency not in ureg:
                ureg.define('currency_{} = nan currency_EUR'.format(currency))
                ureg.define('@alias currency_{0} = {0}'.format(currency))

            currency_units = ureg('currency_' + currency)
            if currency_units.units == self._base_currency.units:
                continue 
            rate = currency_info['rate']
            ctx.redefine('currency_{} = {} currency_EUR'.format(currency, 1 / rate))
        self._logger.info('Updated currency registry')

    def get_rate_timestamp(self, unit):
        if isinstance(unit, pint.Quantity):
            unit = unit.units
        unit_name = str(unit).replace('currency_', '')
        return CurrencyService().get_rate_timestamp(unit_name)

    def set_unit_conversion_mode(self, mode):
        self._unit_conversion_mode = mode

    @property
    def unit_conversion_mode(self):
        return self._unit_conversion_mode

    @property
    def base_currency(self):
        return self._base_currency

    @property
    def unit_registry(self):
        return self._unit_registry

    @property
    def enabled(self):
        return self._enabled

    @property
    def running(self):
        return self._running

    def enable(self):
        self._enabled = True
        return self

    def disable(self):
        self._enabled = False
        return self

    def stop(self):
        self._running = False
        self._unit_registry = None
        self._base_currency = None
        CurrencyService().remove_update_callback(self._update_callback)
        return self

    def run(self, force=False):
        if pint is None:
            return
        if force: pass
        elif self._running:
            return

        self._unit_registry = pint.UnitRegistry(
            autoconvert_offset_to_baseunit=True,
            case_sensitive=False
        )
        self._unit_registry.define('UNIT_SERVICE_NONE = [unit_service_none]')
        self._ctx = pint.Context('currency')
        self._unit_registry.add_context(self._ctx)

        self._load_extra_units(os.path.join(MAIN_DIR, 'data/currency/definitions.txt'), translation_mode='units', is_currency=True)
        self._load_extra_units(os.path.join(MAIN_DIR, 'data/lang/currency.txt'), translation_mode='units', is_currency=True)
        self._load_extra_units(os.path.join(MAIN_DIR, 'data/lang/units.txt'), translation_mode='units')
        self._base_currency = self._unit_registry.Quantity(1, 'currency_EUR')
        CurrencyService().remove_update_callback(self._update_callback)
        CurrencyService().add_update_callback(self._update_callback)
        self._running = True
        return self
