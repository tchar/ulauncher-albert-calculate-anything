'''Logging module.

For modules/launchers that support python's logging a RotatingFileHandler
and a StreamHandler with a color formatter is used.

For other launchers (i.e Albert) that doesn't let us use logging we use a
CustomHandler instead of a StreamHandler. It is a fucking dirty hack, but
what can we do about it?
'''

import os
import sys
import logging as _logging
import logging.handlers as _handlers
import copy
from typing import Callable, Dict, Optional
from calculate_anything.constants import APP_DIRS


__all__ = [
    'DEBUG',
    'INFO',
    'WARNING',
    'ERROR',
    'CRITICAL',
    'ColorFormatter',
    'CustomHandler',
    'Logging',
    'getLogger',
    'setLevel',
    'disable_file_handler',
    'set_file_handler',
    'disable_stdout_handler',
    'set_stdout_handler',
    'getLogger',
]


DEBUG = _logging.DEBUG
INFO = _logging.INFO
WARNING = _logging.WARNING
ERROR = _logging.ERROR
CRITICAL = _logging.CRITICAL


class ColorFormatter(_logging.Formatter):
    # Just leave this here to remember color numbers
    # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
    SEQS = {
        'RESET': '\033[0m',
        'COLOR': '\033[0;%dm',
        'BCOLOR': '\033[1;%dm',
        'BOLD': '\033[1m',
        'BLACK': '\033[0;30m',
        'RED': '\033[0;31m',
        'GREEN': '\033[0;32m',
        'YELLOW': '\033[0;33m',
        'BLUE': '\033[0;34m',
        'MAGENTA': '\033[0;35m',
        'CYAN': '\033[0;36m',
        'WHITE': '\033[0;37m',
    }
    COLORS = {
        'DEBUG': 34,
        'INFO': 37,
        'WARNING': 33,
        'ERROR': 31,
        'CRITICAL': 35,
    }

    def __init__(
        self,
        fmt: Optional[str] = None,
        date_fmt: str = '%Y-%m-%d:%H:%M:%S',
        use_color: bool = True,
    ):
        '''Args:
        fmt (str, optional): A '{' style format with the extra codes provided
            in ColorFormatter.SEQS. Any related codes from ColorFormatter.SEQS
            should be put in single '{' formatting. Others should be put
            in '{{' e.g '{{asctime}} {BOLD}{{name}}{RESET}: {{message}}'.
            If None the default format is used '{{asctime}}.{{msecs:03.0f}} |
            {{levelname}} | [{BOLD}{{name}}.{{funcName}}:{{lineno}}{RESET}]:
            {{message}}'
        date_fmt (str): A date format, default '%Y-%m-%d:%H:%M:%S'
        use_color (bool): Wether to use colors or not, default True
        '''
        if use_color:
            seqs = ColorFormatter.SEQS
        else:
            seqs = {k: '' for k in ColorFormatter.SEQS}
        if not fmt:
            fmt = (
                '{{asctime}}.{{msecs:03.0f}} | {{levelname}} | '
                '[{BOLD}{{name}}.{{funcName}}:{{lineno}}{RESET}]: {{message}}'
            )

        fmt = fmt.format(**seqs)
        _logging.Formatter.__init__(self, fmt, date_fmt, style='{')
        self._use_color = use_color

    def format(self, record: _logging.LogRecord) -> str:
        '''Formats the record. If coloring is used record is copied and
        levelname is changed to use colors

        Returns:
            str: A formatted string
        '''
        if self._use_color and record.levelname in ColorFormatter.COLORS:
            # Copy record as we are changhing the levelname
            record = copy.copy(record)
            levelname = record.levelname
            levelname = (
                ColorFormatter.SEQS['COLOR'] % ColorFormatter.COLORS[levelname]
                + levelname
                + ColorFormatter.SEQS['RESET']
            )
            record.levelname = levelname
        return _logging.Formatter.format(self, record)


class CustomHandler(_logging.Handler):
    '''A super special handler for fucking Albert'''

    def __init__(
        self,
        debug: Callable[[str], None],
        info: Callable[[str], None],
        warning: Callable[[str], None],
        error: Callable[[str], None],
        critical: Callable[[str], None],
        level=_logging.NOTSET,
    ) -> None:
        '''Args:
        debug (Callable[str]): Called when debug log is received.
        info (Callable[str]): Called when info log is received.
        warning (Callable[str]): Called when warning log is received.
        error (Callable[str]): Called when error log is received.
        critical (Callable[str]): Called when critical log is received.
        level (int): Same as logging module's values.
        '''
        super().__init__(level=level)
        self._debug = debug
        self._info = info
        self._warning = warning
        self._error = error
        self._critical = critical
        self.setFormatter(_logging.Formatter())

    def emit(self, record: _logging.LogRecord) -> None:
        '''Emits the LogRecord using the provided callables when
        instantiated.
        '''

        if record.levelno <= _logging.DEBUG:
            log = self._debug
        elif record.levelno <= _logging.INFO:
            log = self._info
        elif record.levelno <= _logging.WARNING:
            log = self._warning
        elif record.levelno <= _logging.ERROR:
            log = self._error
        elif record.levelno <= _logging.CRITICAL:
            log = self._critical
        else:
            return
        message = self.formatter.format(record)
        log(message)


class Logging:
    '''Holds the logging information such as handlers to use.
    Prefer to use the functons provided in this module.
    '''

    def __init__(self):
        level = os.environ.get('CALCULATE_ANYTHING_VERBOSE', '').upper()
        level = _logging.getLevelName(level)
        level = level if isinstance(level, int) else _logging.INFO

        stdout_hdlr = _logging.StreamHandler(sys.stderr)
        stdout_hdlr.setFormatter(ColorFormatter(use_color=True))

        file_hdlr = _handlers.RotatingFileHandler(
            os.path.join(APP_DIRS.user_log_dir, 'runtime.log'),
            maxBytes=1000000,
            backupCount=10,
            encoding='utf-8',
            delay=True,
        )
        file_hdlr.setFormatter(ColorFormatter(use_color=False))

        self.level = level
        self.file_hdlr = file_hdlr
        self.stdout_hdlr = stdout_hdlr
        self._loggers: Dict[str, _logging.Logger] = {}

    def set_level(self, level: int) -> None:
        '''Sets the level for all loggers'''
        for logger in self._loggers.values():
            logger.setLevel(level)
        self.level = level

    def disable_file_handler(self) -> None:
        '''Disables file handler provided from this class'''
        self.set_file_handler(None)

    def set_file_handler(self, hdlr: _logging.FileHandler) -> None:
        '''Sets file handler to be used

        Args:
            hdlr (logging.FileHandler): The file handler to set
        '''
        if self.file_hdlr is not None:
            self.file_hdlr.close()

        for logger in self._loggers.values():
            if self.file_hdlr is not None:
                logger.removeHandler(self.file_hdlr)
            if hdlr is not None:
                logger.addHandler(hdlr)
        self.file_hdlr = hdlr

    def disable_stdout_handler(self) -> None:
        '''Disables stdout handler provided from this class'''
        self.set_stdout_handler(None)

    def set_stdout_handler(self, hdlr: _logging.Handler) -> None:
        '''Sets stdout handler to be used

        Args:
            hdlr (logging.FileHandler): The stdout handler to set
        '''
        if self.stdout_hdlr is not None:
            self.stdout_hdlr.close()

        for logger in self._loggers.values():
            if self.stdout_hdlr is not None:
                logger.removeHandler(self.stdout_hdlr)
            if hdlr is not None:
                logger.addHandler(hdlr)
        self.stdout_hdlr = hdlr

    def get_logger(self, name: str) -> _logging.Logger:
        '''Returns a logger with file handler and stdout handler
        provided from this class.

        Args:
            name (str): The name of the logger as in logging.getLogger(name)
        '''
        if name in self._loggers:
            return self._loggers[name]

        logger = _logging.getLogger(name)
        if self.stdout_hdlr is not None:
            logger.addHandler(self.stdout_hdlr)
        if self.file_hdlr is not None:
            logger.addHandler(self.file_hdlr)
        logger.setLevel(self.level)

        self._loggers[name] = logger
        return logger


Logging = Logging()


def setLevel(level: int) -> None:
    '''Sets the level for all loggers'''
    Logging.set_level(level)


def disable_file_handler() -> None:
    '''Disables file handler provided from this class'''
    Logging.disable_file_handler()


def set_file_handler(hdlr: _logging.Handler) -> None:
    '''Sets file handler to be used

    Args:
        hdlr (logging.FileHandler): The file handler to set
    '''
    Logging.set_file_handler(hdlr)


def disable_stdout_handler() -> None:
    '''Disables stdout handler provided from this class'''
    Logging.disable_stdout_handler()


def set_stdout_handler(hdlr: _logging.Handler) -> None:
    '''Sets stdout handler to be used

    Args:
        hdlr (logging.FileHandler): The stdout handler to set
    '''
    Logging.set_stdout_handler(hdlr)


def getLogger(name: str) -> _logging.Logger:
    '''Returns a logger with file handler and stdout handler
    provided from this class.

    Args:
        name (str): The name of the logger as in logging.getLogger(name)
    '''
    return Logging.get_logger(name)
