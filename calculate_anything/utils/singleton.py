from typing import Any
from functools import wraps


__all__ = ['Singleton']


class Singleton(type):
    _instances = {}
    _funcinstances = {}

    def function(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            if func not in Singleton._funcinstances:
                Singleton._funcinstances[func] = func(*args, **kwargs)
            return Singleton._funcinstances[func]
        return _wrapper

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
