try:
    import pint
except ImportError:
    pint = None
from typing import Callable, Optional
from calculate_anything.lang import LanguageService
from calculate_anything import logging
from calculate_anything.regex import UNIT_ALIASES_RE


logger = logging.getLogger(__name__)


class PintDefinitionParser:
    def __init__(self, unit_registry: 'pint.registry.UnitRegistry') -> None:
        self._unit_registry = unit_registry

    def _define_currency(
        self, currency: str, definition: Optional[str] = None
    ) -> None:
        currency_norm = currency.lstrip('currency_')
        currency_upper = 'currency_{}'.format(currency_norm.upper())
        definition = definition or 'nan currency_EUR'

        if currency_upper not in self._unit_registry:
            self._unit_registry.define(
                '{} = {}'.format(currency_upper, definition)
            )
        self._unit_registry.define(
            '@alias {} = {}'.format(currency_upper, currency_norm)
        )

    def _process_alias(
        self,
        line: str,
        translation_adder: Callable[[str, str], None],
        is_currency: bool,
    ) -> None:
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

    def _process_reverse_alias(
        self, line: str, translation_adder: Callable[[str, str], None]
    ) -> None:
        aliases = line.strip('@reverse.alias').split('=')
        aliases = list(map(str.strip, aliases))
        root_alias, aliases_to_define = aliases[0], aliases[1:]
        if not aliases_to_define or not root_alias:
            return
        for alias in aliases_to_define:
            translation_adder(alias.lower(), root_alias)

    def _process_definition(self, line: str, is_currency: bool) -> None:
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

    def _process_line(
        self,
        line: str,
        line_n: int,
        file_path: str,
        translation_adder: Callable[[str, str], None],
        is_currency: bool,
    ) -> None:
        try:
            line = line.strip()
            if line.startswith('#'):
                return None
            if line.startswith('@alias '):
                self._process_alias(line, translation_adder, is_currency)
                return
            if line.startswith('@reverse.alias'):
                self._process_reverse_alias(line, translation_adder)
                return
            self._process_definition(line, is_currency)
        except Exception as e:
            logger.exception(
                'Got exception when parsing line {} in {}: {}'.format(
                    line_n, file_path, e
                )
            )

    def load_file(
        self, file_path: str, mode: str, is_currency: bool = True
    ) -> None:
        translation_adder = LanguageService().translation_adder(mode)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    self._process_line(
                        line, i + 1, file_path, translation_adder, is_currency
                    )
            logger.info('Loaded unit definitions: {}'.format(file_path))
        except FileNotFoundError:
            logger.warning(
                'Unit definitions file not found: {}'.format(file_path)
            )
        except Exception as e:
            logger.exception(
                'Exception when loading unit definitons file {}: {}'.format(
                    file_path, e
                )
            )
