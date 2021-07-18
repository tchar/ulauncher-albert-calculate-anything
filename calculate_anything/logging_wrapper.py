from typing import Any, Protocol
from abc import abstractmethod
import logging


class Logger(Protocol):
    @abstractmethod
    def debug(self, message: str, *args: Any, **kwargs: Any) -> None: #pragma: no cover
        pass

    @abstractmethod
    def info(self, message: str, *args: Any, **kwargs: Any) -> None: #pragma: no cover
        pass

    @abstractmethod
    def warning(self, message: str, *args: Any, **kwargs: Any) -> None: #pragma: no cover
        pass

    @abstractmethod
    def error(self, message: str, *args: Any, **kwargs: Any) -> None: #pragma: no cover
        pass

    @abstractmethod
    def exception(self, message: str, *args: Any, **kwargs: Any) -> None: #pragma: no cover
        pass


class LoggingModule(Protocol):
    def getLogger(name: str) -> Logger: #pragma: no cover
        pass


class LoggingWrapper:
    logging: LoggingModule = logging

    @staticmethod
    def set_logging(logging: LoggingModule) -> None:
        LoggingWrapper.logging = logging

    @staticmethod
    def getLogger(name: str) -> Logger:
        return LoggingWrapper.logging.getLogger(name)
