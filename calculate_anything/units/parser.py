try:
    import pint
except ImportError:
    pint = None
from calculate_anything.lang import LanguageService
from calculate_anything.logging_wrapper import LoggingWrapper as logging
from calculate_anything.constants import UNIT_ALIASES_RE


class PintDefinitionParser:
    def __init__(self, unit_registry: 'pint.registry.UnitRegistry'):
        self._unit_registry = unit_registry
        self._logger = logging.getLogger(__name__)

    def _define_currency(self, currency, definition=None):
        currency_norm = currency.lstrip('currency_')
        currency_upper = 'currency_{}'.format(currency_norm.upper())
        definition = definition or 'nan currency EUR'

        if currency_upper not in self._unit_registry:
            self._unit_registry.define(
                '{} = {}'.format(currency_upper, definition))
        self._unit_registry.define(
            '@alias {} = {}'.format(currency_upper, currency_norm))

    def _process_alias(self, line, translation_adder, is_currency):
        aliases = line.lstrip('@alias').split('=')
        aliases = map(str.strip, aliases)
        root_alias = None
        aliases_to_define = []
        for alias in aliases:
            if not root_alias:
                is_in_registry = alias in self._unit_registry
                if not is_in_registry and is_currency:
                    self._define_currency(alias)
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

    def _process_reverse_alias(self, line, translation_adder):
        pass
        aliases = line.strip('@reverse.alias').split('=')
        aliases = list(map(str.strip, aliases))
        root_alias, aliases_to_define = aliases[0], aliases[1:]
        if not aliases_to_define or not root_alias:
            return
        for alias in aliases_to_define:
            translation_adder(alias.lower(), root_alias)

    def _process_definition(self, line, is_currency):
        line = line.split('=')
        if len(line) == 1:
            return
        line = map(str.strip, line)
        line = list(line)
        root_unit, rest_units = line[0], line[1:]
        rest_units = ' = '.join(rest_units)
        if is_currency:
            self._define_currency(root_unit, definition=rest_units)
        else:
            self._unit_registry.define('{} = {}'.format(root_unit, rest_units))

    def _process_line(self, line, line_n, file_path, translation_adder, is_currency):
        try:
            line = line.strip()
            if line.startswith('#'):
                return
            if line.startswith('@alias '):
                return self._process_alias(line, translation_adder, is_currency)
            if line.startswith('@reverse.alias'):
                return self._process_reverse_alias(line, translation_adder)
            return self._process_definition(line, is_currency)
        except Exception as e:
            self._logger.error(
                'Got exception when parsing line {} in {}: {}'.format(line_n, file_path, e))

    def load_file(self, file_path, translation_mode, is_currency=True):
        translation_adder = LanguageService().get_translation_adder(translation_mode)
        try:
            with open(file_path, 'r') as f:
                for i, line in enumerate(f):
                    self._process_line(line, i + 1, file_path,
                                       translation_adder, is_currency)
            self._logger.info('Loaded unit definitions: {}'.format(file_path))
        except FileNotFoundError:
            self._logger.warning(
                'Unit definitions file not found: {}'.format(file_path))
        except Exception as e:
            self._logger.error(
                'Exception when loading unit definitons file {}: {}'.format(file_path, e))
