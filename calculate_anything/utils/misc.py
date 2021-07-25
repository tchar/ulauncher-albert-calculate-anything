from contextlib import contextmanager
from functools import wraps
from typing import Any, Container, Iterable, List, Optional, Type, Union
from types import ModuleType
import importlib
from calculate_anything.logging_wrapper import LoggingWrapper as logging
from calculate_anything.exceptions import MissingSimpleevalException


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


@contextmanager
def safe_operation(message: str = ''):
    logger = logging.getLogger(__name__)
    if message:
        logger.info(message)
    try:
        yield
    except Exception as e:
        msg = e
        if message:
            msg = '{}: {}'.format(message, e)
        logger.exception('Got error in safe operation: {}'.format(msg))
    finally:
        pass


def lock(func):
    @wraps(func)
    def _wrapper(self, *args, **kwargs):
        with self._lock:
            return func(self, *args, **kwargs)
    return _wrapper
