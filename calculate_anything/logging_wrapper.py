from typing import Any, Protocol
import logging


class Logger(Protocol):
    def debug(message: str, *args: Any, **kwargs: Any) -> None:
        pass

    def info(message: str, *args: Any, **kwargs: Any) -> None:
        pass

    def warning(message: str, *args: Any, **kwargs: Any) -> None:
        pass

    def error(message: str, *args: Any, **kwargs: Any) -> None:
        pass

    def exception(message: str, *args: Any, **kwargs: Any) -> None:
        pass


class LoggingModule(Protocol):
    def getLogger(name: str) -> Logger:
        pass


class LoggingWrapper:
    logging: LoggingModule = logging

    @staticmethod
    def set_logging(logging: LoggingModule) -> None:
        LoggingWrapper.logging = logging

    @staticmethod
    def getLogger(name: str) -> Logger:
        return LoggingWrapper.logging.getLogger(name)
