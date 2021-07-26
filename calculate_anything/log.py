'''Logging for calculate anything.

For modules/launchers that support python's logging a RotatingFileHandler
and a StreamHandler with a color formatter is used.

For other launchers (i.e Albert) that doesn't let us use logging we use a 
CustomHandler instead of a StreamHandler. It is a fucking dirty hack, but
what can we do about it?
'''
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
import copy
from typing import Callable
from calculate_anything.constants import LOGS_DIR

__all__ = []


class ColorFormatter(logging.Formatter):
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

    def __init__(self, fmt=None, date_fmt=None, use_color: bool = True):
        if use_color:
            seqs = ColorFormatter.SEQS
        else:
            seqs = {k: '' for k in ColorFormatter.SEQS}
        if not fmt:
            fmt = '{{asctime}}.{{msecs:03.0f}} | {{levelname}} | [{BOLD}{{name}}.{{funcName}}:{{lineno}}{RESET}]: {{message}}'
        if not date_fmt:
            date_fmt = '%Y-%m-%d:%H:%M:%S'

        fmt = fmt.format(**seqs)
        logging.Formatter.__init__(self, fmt, date_fmt, style='{')
        self._use_color = use_color

    def format(self, record):
        if self._use_color and record.levelname in ColorFormatter.COLORS:
            # Copy record as we are changhing the levelname
            record = copy.copy(record)
            levelname = record.levelname
            levelname = ColorFormatter.SEQS['COLOR'] % \
                ColorFormatter.COLORS[levelname] + \
                levelname + ColorFormatter.SEQS['RESET']
            record.levelname = levelname
        return logging.Formatter.format(self, record)


class CustomHandler(logging.Handler):
    '''A super special handler for fucking Albert'''

    def __init__(self, debug: Callable[[str], None],
                 info: Callable[[str], None],
                 warning: Callable[[str], None],
                 error: Callable[[str], None],
                 critical: Callable[[str], None],
                 level=logging.NOTSET) -> None:
        super().__init__(level=level)
        self._debug = debug
        self._info = info
        self._warning = warning
        self._error = error
        self._critical = critical
        self.setFormatter(logging.Formatter())

    def emit(self, record) -> None:
        if record.levelno == logging.DEBUG:
            log = self._debug
        elif record.levelno == logging.INFO:
            log = self._info
        elif record.levelno == logging.WARNING:
            log = self._warning
        elif record.levelno == logging.ERROR:
            log = self._error
        elif record.levelno == logging.CRITICAL:
            log = self._critical
        else:
            return
        message = self.formatter.format(record)
        log(message)


class _Logging:
    _level = os.environ.get('CALCULATE_ANYTHING_VERBOSE', '').upper()
    _level = logging.getLevelName(_level)
    _level = _level if isinstance(_level, int) else logging.INFO

    _stdout_hdlr = logging.StreamHandler(sys.stderr)
    _stdout_hdlr.setFormatter(ColorFormatter(use_color=True))

    _file_hdlr = RotatingFileHandler(
        os.path.join(LOGS_DIR, 'runtime.log'),
        maxBytes=1000000, backupCount=10, encoding='utf-8',
        delay=True
    )
    _file_hdlr.setFormatter(ColorFormatter(use_color=False))

    @classmethod
    def set_level(cls, level: int):
        cls._level = level

    @classmethod
    def disable_stdout_handler(cls):
        cls._stdout_hdlr = None

    @classmethod
    def set_stdout_handler(cls, hdlr: logging.Handler):
        cls._stdout_hdlr = hdlr

    @classmethod
    def disable_file_handler(cls):
        cls._file_hdlr = None

    @classmethod
    def set_file_handler(cls, hdlr: logging.FileHandler):
        cls._file_hdlr = hdlr

    @classmethod
    def get_logger(cls, name):
        logger = logging.getLogger(name)
        logger.setLevel(cls._level)

        if cls._file_hdlr:
            logger.removeHandler(cls._file_hdlr)
            logger.addHandler(cls._file_hdlr)
        if cls._stdout_hdlr:
            # Remove the handler because logging caches loggers
            logger.removeHandler(cls._stdout_hdlr)
            logger.addHandler(cls._stdout_hdlr)

        return logger


def disable_stdout_handler():
    _Logging.disable_stdout_handler()


def set_stdout_handler(hdlr: logging.Handler):
    _Logging.set_stdout_handler(hdlr)


def disable_file_handler():
    _Logging.disable_file_handler()


def set_file_handler(hdlr: logging.Handler):
    _Logging.set_file_handler(hdlr)

def setLevel(level: int):
    _Logging.set_level(level)

def getLogger(name: str) -> logging.Logger:
    return _Logging.get_logger(name)
