'''Singleton class.'''

from typing import Any, Callable, Type, TypeVar
from functools import wraps


__all__ = ['Singleton']


RT = TypeVar('RT')


class Singleton(type):
    '''Singleton class to be used as a metaclass'''

    _instances = {}
    _functions = {}

    @classmethod
    def function(cls, func: Callable[..., RT]) -> Callable[..., RT]:
        '''Singleton function decorator.

        Args:
            func (Callable): The function to decorate/

        Returns:
            Callable: The function decorated as singleton.
        '''

        @wraps(func)
        def _wrapper(*args: Any, **kwargs: Any) -> Any:
            if func not in cls._functions:
                cls._functions[func] = func(*args, **kwargs)
            return cls._functions[func]

        return _wrapper

    def __call__(cls: Type[Any], *args: Any, **kwargs: Any) -> Any:
        '''Gets as input the class and args/kwargs and returns either an already
        instantiated object or a new object from that class'''
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]
