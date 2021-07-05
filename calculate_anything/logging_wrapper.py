import logging

class LoggingWrapper:
    logging = logging

    @staticmethod
    def set_logging(logging):
        LoggingWrapper.logging = logging

    @staticmethod
    def getLogger(name=''):
        return LoggingWrapper.logging.getLogger(name)