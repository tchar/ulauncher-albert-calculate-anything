from abc import ABC, abstractmethod
from enum import IntFlag
from functools import wraps
from typing import Any, Callable, TypeVar


__all__ = ['Loader']


RT = TypeVar('RT')


class Loader(ABC):
    class Status(IntFlag):
        SUCCESS = 1
        FAIL = SUCCESS << 1
        PENDING = SUCCESS << 2
        DEFAULT_DATA = SUCCESS << 3
        FILE_IS_DIR = SUCCESS << 4
        CANT_READ_FILE = SUCCESS << 5
        CANNOT_REMOVE_FILE = SUCCESS << 6
        CANNOT_WRITE_FILE = SUCCESS << 7
        INVALID_DATA = SUCCESS << 8

    class Mode(IntFlag):
        LOAD = 1
        MEMORY = LOAD << 1
        REMOVE = LOAD << 2
        NO_REMOVE = LOAD << 3
        CREATE = LOAD << 4
        VALIDATE = LOAD << 5
        FALLBACK = LOAD << 6

    class Decorators:
        @staticmethod
        def with_data(func: Callable[..., RT]) -> RT:
            @wraps(func)
            def _wrapper(self: 'Loader', *args: Any, **kwargs: Any) -> Any:
                if self.data is None:
                    return None
                return func(self, *args, **kwargs)

            return _wrapper

        @staticmethod
        def with_mode(
            mode: 'Loader.Mode',
        ) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
            def _decorator(func: Callable[..., RT]) -> RT:
                @wraps(func)
                def _wrapper(self: 'Loader', *args: Any, **kwargs: Any) -> Any:
                    if self._mode & mode:
                        return func(self, *args, **kwargs)
                    return None

                return _wrapper

            return _decorator

        @staticmethod
        def without_mode(
            mode: 'Loader.Mode',
        ) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
            def _decorator(func: Callable[..., RT]) -> RT:
                @wraps(func)
                def _wrapper(self: 'Loader', *args: Any, **kwargs: Any) -> Any:
                    if self._mode & mode:
                        return None
                    return func(self, *args, **kwargs)

                return _wrapper

            return _decorator

        @staticmethod
        def with_status(
            status: 'Loader.Status',
        ) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
            def _decorator(func: Callable[..., RT]) -> RT:
                @wraps(func)
                def _wrapper(self: 'Loader', *args: Any, **kwargs: Any) -> Any:
                    if self._status & status:
                        return func(self, *args, **kwargs)
                    return None

                return _wrapper

            return _decorator

        @staticmethod
        def without_status(
            status: 'Loader.Status',
        ) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
            def _decorator(func: Callable[..., RT]) -> RT:
                @wraps(func)
                def _wrapper(self: 'Loader', *args: Any, **kwargs: Any) -> Any:
                    if self._status & status:
                        return None
                    return func(self, *args, **kwargs)

                return _wrapper

            return _decorator

    def __init__(self, status: Status = 0, mode: Mode = 0) -> None:
        self._mode = mode
        self._status = status

    @property
    def status(self) -> Status:
        return self._status

    @property
    def mode(self) -> Mode:
        return self._mode

    @property
    @abstractmethod
    def data(self) -> Any:
        pass

    @abstractmethod
    def load(self) -> None:
        pass
