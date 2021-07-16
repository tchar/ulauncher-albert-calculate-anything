import logging as _logging
from calculate_anything.logging_wrapper import LoggingWrapper as logging


class MockLogger:
    def __init__(self, name):
        self._name = name

    def _log(self, func, message, *args):
        message = str(message)
        if args:
            message = message % args
        message = '{}: {}'.format(self._name, message)
        func(message)

    def debug(self, message, *args):
        self._log(print, message, *args)

    def info(self, message, *args):
        self._log(print, message, *args)

    def warning(self, message, *args):
        self._log(print, message, *args)

    def error(self, message, *args):
        self._log(print, message, *args)


class MockLogging:
    @staticmethod
    def getLogger(name):
        return MockLogger(name)


def test_logging_wrapper_logging(caplog):
    logging.set_logging(_logging)
    logger = logging.getLogger(__name__)

    with caplog.at_level(_logging.DEBUG):
        logger.debug('A debug message')
        assert 'A debug message' in caplog.text

        logger.info('An info message')
        assert'An info message' in caplog.text

        logger.warning('A warning message')
        assert 'A warning message' in caplog.text

        logger.error('An error message')
        assert 'An error message\n' in caplog.text


def test_logging_wrapper_custom(capfd):
    logging.set_logging(MockLogging)
    logger = logging.getLogger(__name__)
    prefix = '{}: '.format(__name__)

    logger.debug('A debug message')
    out, err = capfd.readouterr()
    assert prefix + 'A debug message\n' == out
    assert err == ''

    logger.info('An info message')
    out, err = capfd.readouterr()
    assert prefix + 'An info message\n' == out
    assert err == ''

    logger.warning('A warning message')
    out, err = capfd.readouterr()
    assert prefix + 'A warning message\n' == out
    assert err == ''

    logger.error('An error message')
    out, err = capfd.readouterr()
    assert prefix + 'An error message\n' == out
    assert err == ''
