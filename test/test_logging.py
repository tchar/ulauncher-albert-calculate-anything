import pytest
import os
from functools import lru_cache
import logging as _logging
from logging.handlers import RotatingFileHandler
from test.tutils import random_str
from calculate_anything import logging


@lru_cache(maxsize=None)
def get_file_handler(filepath):
    file_hdlr = RotatingFileHandler(
        filepath,
        maxBytes=1000000,
        backupCount=10,
        encoding='utf-8',
        delay=False,
    )
    file_hdlr.setFormatter(logging.ColorFormatter(use_color=False))
    return file_hdlr


@lru_cache(maxsize=None)
def get_stdout_handler():
    hdlr = logging.CustomHandler(print, print, print, print, print)
    return hdlr


@pytest.mark.parametrize(
    'level',
    [
        _logging.DEBUG,
        _logging.INFO,
        _logging.WARNING,
        _logging.ERROR,
        _logging.CRITICAL,
    ],
)
def test_logging(caplog, level):
    with caplog.at_level(level):
        logging.setLevel(level)
        logging.set_file_handler(None)

        logger = logging.getLogger('test_logging_logging')
        assert len(logger.handlers) == 1
        assert isinstance(logger.handlers[0], _logging.StreamHandler)

        msg = random_str()
        logger.debug(msg)
        assert (msg in caplog.text) == (level <= _logging.DEBUG)

        msg = random_str()
        logger.info(msg)
        assert (msg in caplog.text) == (level <= _logging.INFO)

        msg = random_str()
        logger.warning(msg)
        assert (msg in caplog.text) == (level <= _logging.WARNING)

        msg = random_str()
        logger.error(msg)
        assert (msg in caplog.text) == (level <= _logging.ERROR)

        msg = random_str()
        logger.critical(msg)
        assert (msg in caplog.text) == (level <= _logging.CRITICAL)


@pytest.mark.parametrize(
    'level',
    [
        _logging.DEBUG,
        _logging.INFO,
        _logging.WARNING,
        _logging.ERROR,
        _logging.CRITICAL,
    ],
)
def test_logging_custom_stdout_hannler(caplog, level):
    hdlr = get_stdout_handler()
    with caplog.at_level(level):
        logging.setLevel(level)
        logging.set_file_handler(None)
        logging.set_stdout_handler(hdlr)

        logger = logging.getLogger('test_logging_custom_stdout_hannler')
        assert len(logger.handlers) == 1
        assert isinstance(logger.handlers[0], logging.CustomHandler)

        msg = random_str()
        logger.debug(msg)
        assert (msg in caplog.text) == (level <= _logging.DEBUG)

        msg = random_str()
        logger.info(msg)
        assert (msg in caplog.text) == (level <= _logging.INFO)

        msg = random_str()
        logger.warning(msg)
        assert (msg in caplog.text) == (level <= _logging.WARNING)

        msg = random_str()
        logger.error(msg)
        assert (msg in caplog.text) == (level <= _logging.ERROR)

        msg = random_str()
        logger.critical(msg)
        assert (msg in caplog.text) == (level <= _logging.CRITICAL)


@pytest.mark.parametrize(
    'level',
    [
        _logging.DEBUG,
        _logging.INFO,
        _logging.WARNING,
        _logging.ERROR,
        _logging.CRITICAL,
    ],
)
def test_logging_no_stdout_handler(caplog, level):
    with caplog.at_level(level):
        logging.setLevel(level)
        logging.set_file_handler(None)
        logging.set_stdout_handler(None)

        logger = logging.getLogger('test_logging_no_stdout_handler')
        assert not logger.handlers


@pytest.mark.parametrize(
    'level',
    [
        _logging.DEBUG,
        _logging.INFO,
        _logging.WARNING,
        _logging.ERROR,
        _logging.CRITICAL,
    ],
)
def test_logging_file(log_filepath, level):
    hdlr = get_file_handler(log_filepath)
    print('Saving logs to {}'.format(log_filepath))

    logging.setLevel(level)
    logging.set_file_handler(hdlr)
    logging.set_stdout_handler(None)

    logger = logging.getLogger('test_logging_file')

    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], RotatingFileHandler)

    msgs = []
    msg = random_str()
    logger.debug(msg)
    msgs.append((msg, _logging.DEBUG))

    msg = random_str()
    logger.info(msg)
    msgs.append((msg, _logging.INFO))

    msg = random_str()
    logger.warning(msg)
    msgs.append((msg, _logging.WARNING))

    msg = random_str()
    logger.error(msg)
    msgs.append((msg, _logging.ERROR))

    msg = random_str()
    logger.critical(msg)
    msgs.append((msg, _logging.CRITICAL))

    assert os.path.exists(log_filepath)
    with open(log_filepath, 'r', encoding='utf-8') as f:
        log = f.read()

    for msg, mlevel in msgs:
        assert (msg in log) == (level <= mlevel)
