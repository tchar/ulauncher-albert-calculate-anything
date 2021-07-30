from enum import IntFlag
from functools import wraps


class Loader:
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

    def __init__(self, status=0, mode=0):
        self._mode = mode
        self._status = status

    class Decorators:
        def with_data(func):
            @wraps(func)
            def _wrapper(self: Loader, *args, **kwargs):
                if self.data is None:
                    return
                return func(self, *args, **kwargs)
            return _wrapper

        def with_mode(mode: IntFlag):
            def _decorator(func):
                @wraps(func)
                def _wrapper(self: Loader, *args, **kwargs):
                    if self._mode & mode:
                        return func(self, *args, **kwargs)
                return _wrapper
            return _decorator

        def without_mode(mode: IntFlag):
            def _decorator(func):
                @wraps(func)
                def _wrapper(self: Loader, *args, **kwargs):
                    if self._mode & mode:
                        return
                    return func(self, *args, **kwargs)
                return _wrapper
            return _decorator

        def with_status(status: IntFlag):
            def _decorator(func):
                @wraps(func)
                def _wrapper(self: Loader, *args, **kwargs):
                    if self._status & status:
                        return func(self, *args, **kwargs)
                return _wrapper
            return _decorator

        def without_status(status: IntFlag):
            def _decorator(func):
                @wraps(func)
                def _wrapper(self: Loader, *args, **kwargs):
                    if self._status & status:
                        return
                    return func(self, *args, **kwargs)
                return _wrapper
            return _decorator

    @property
    def status(self):
        return self._status

    @property
    def mode(self):
        return self._mode

    @property
    def data(self):
        return None  # pragma: no cover
