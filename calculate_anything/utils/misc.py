import importlib
from typing import Any, Container, Iterable, List, Optional, Type, Union
from types import ModuleType
from ..exceptions import MissingSimpleevalException


def get_module(name: str) -> Union[None, ModuleType]:
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        return None


def is_types(*types: List[Type[Any]]) -> bool:
    return lambda value: any(map(lambda t: isinstance(value, t), types))


def is_not_types(*types: List[Type[Any]]) -> bool:
    return lambda value: not is_types(*types)(value)


def get_or_default(value: Any, _type: Type[Any], default: Any,
                   allowed_values: Optional[Union[Container, Iterable]] = None) -> Any:
    try:
        value = _type(value)
        if allowed_values and value not in allowed_values:
            return default
        return value
    except Exception:
        return default


def is_integer(value: Any) -> bool:
    if isinstance(value, float):
        if value.is_integer():
            return True
        return False
    if isinstance(value, complex):
        return value.imag == 0
    if isinstance(value, bool):
        return False
    return isinstance(value, int)


class StupidEval:
    def __init__(self, *args: Any, **kwargs: Any):
        self.operators = {}

    def eval(self, query: str) -> int:
        try:
            if not isinstance(query, str):
                raise MissingSimpleevalException
            return int(query)
        except (ValueError, TypeError):
            raise MissingSimpleevalException
