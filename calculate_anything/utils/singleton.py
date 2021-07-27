from typing import Any, Type
from functools import wraps


__all__ = ['Singleton']


class Singleton(type):
    _instances = {}
    _functions = {}

    @classmethod
    def function(cls, func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            if func not in cls._functions:
                cls._functions[func] = func(*args, **kwargs)
            return cls._functions[func]
        return _wrapper

    def __call__(cls: Type[Any], *args: Any, **kwargs: Any) -> Any:
        '''Gets as input the class and args/kwargs and returns either an already
        instantiated object or a new object from that class'''
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
