from typing import Any, Callable, Type
from functools import wraps


__all__ = ['Singleton']

# https://stackoverflow.com/a/5191224/3215376


class _SingletonPropertyDescriptor(object):

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        return self.fget.__get__(obj, cls())()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError('can\'t set attribute')
        _type = type(obj)
        if _type == Singleton:
            _type = obj
        return self.fset.__get__(obj, _type)(value)

    def setter(self, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self


class _SingletonMethod:
    def __init__(self, func: Callable[[Any], Any]):
        self._func = func

    def __get__(self, obj: Any, cls: Type[Any]):
        '''Returns a wrapper which passes the self to the function provided
        If obj is None (meaning it is a class method) instantiates the class
        and passes it as the self argument'''

        @wraps(self._func)
        def _wrapper(*args, **kwargs):
            if obj is None:
                _self = cls()
            else:
                _self = obj
            return self._func(_self, *args, **kwargs)
        return _wrapper


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

    def method(func):
        '''Returns a SingletonMethod object'''
        return _SingletonMethod(func)

    def property(func):
        if not isinstance(func, (classmethod, staticmethod)):
            # print('In here')
            func = classmethod(func)

        return _SingletonPropertyDescriptor(func)

    def __call__(cls: Type[Any], *args: Any, **kwargs: Any) -> Any:
        '''Gets as input the class and args/kwargs and returns either an already
        instantiated object or a new object from that class'''
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def __setattr__(self, key, value):
        if key in self.__dict__:
            obj = self.__dict__.get(key)
        else:
            obj = self()
            return setattr(obj, key, value)
        if obj and type(obj) is _SingletonPropertyDescriptor:
            return obj.__set__(self, value)
        return super().__setattr__(key, value)
