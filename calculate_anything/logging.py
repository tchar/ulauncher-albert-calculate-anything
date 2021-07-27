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
from calculate_anything.utils import Singleton
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


class Logging(metaclass=Singleton):
    def __init__(self):
        level = os.environ.get('CALCULATE_ANYTHING_VERBOSE', '').upper()
        level = logging.getLevelName(level)
        level = level if isinstance(level, int) else logging.INFO

        stdout_hdlr = logging.StreamHandler(sys.stderr)
        stdout_hdlr.setFormatter(ColorFormatter(use_color=True))

        file_hdlr = RotatingFileHandler(
            os.path.join(LOGS_DIR, 'runtime.log'),
            maxBytes=1000000, backupCount=10, encoding='utf-8',
            delay=True
        )
        file_hdlr.setFormatter(ColorFormatter(use_color=False))

        self.level = level
        self.file_hdlr = file_hdlr
        self.stdout_hdlr = stdout_hdlr
        self._prev_hdlrs = set()
        self._got_logger = False

    def set_level(self, level: int):
        self.level = level

    def disable_stdout_handler(self):
        self.stdout_hdlr = None

    def set_stdout_handler(self, hdlr: logging.Handler):
        if self.stdout_hdlr and self._got_logger:
            print(self._got_logger)
            self._prev_hdlrs.add(self.stdout_hdlr)
        self.stdout_hdlr = hdlr

    def disable_file_handler(self):
        self.file_hdlr = None

    def set_file_handler(self, hdlr: logging.FileHandler):
        if self.file_hdlr and self._got_logger:
            print(self._got_logger)
            self._prev_hdlrs.add(self.file_hdlr)
        self.file_hdlr = hdlr

    def get_logger(self, name):
        self._got_logger = True
        logger = logging.getLogger(name)
        logger.setLevel(self.level)

        for hdlr in self._prev_hdlrs:
            logger.removeHandler(hdlr)
        if self.file_hdlr:
            logger.addHandler(self.file_hdlr)
        if self.stdout_hdlr:
            logger.addHandler(self.stdout_hdlr)

        return logger


def disable_stdout_handler():
    Logging().disable_stdout_handler()


def set_stdout_handler(hdlr: logging.Handler):
    Logging().set_stdout_handler(hdlr)


def disable_file_handler():
    Logging().disable_file_handler()


def set_file_handler(hdlr: logging.Handler):
    Logging().set_file_handler(hdlr)


def setLevel(level: int):
    Logging().set_level(level)


def getLogger(name: str) -> logging.Logger:
    return Logging().get_logger(name)
