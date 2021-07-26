from calculate_anything.query.handlers import (
    UnitsQueryHandler, CalculatorQueryHandler,
    PercentagesQueryHandler, TimeQueryHandler,
    Base16QueryHandler, Base10QueryHandler,
    Base2QueryHandler, Base8QueryHandler
)
from calculate_anything import logging
from calculate_anything.utils import Singleton


__all__ = ['MultiHandler']


class MultiHandler(metaclass=Singleton):
    def __init__(self):
        self._handlers = [
            UnitsQueryHandler(),
            CalculatorQueryHandler(),
            PercentagesQueryHandler(),
            TimeQueryHandler(),
            Base10QueryHandler(),
            Base16QueryHandler(),
            Base8QueryHandler(),
            Base2QueryHandler()
        ]
        self._logger = logging.getLogger(__name__)

    def handle(self, query, *handlers, return_raw=False):
        handlers = set(handlers)
        results = []
        for handler in self._handlers:
            if handlers and not handler.__class__ in handlers:
                continue
            try:
                result = handler.handle(query)
            except Exception as e:
                self._logger.exception('Got exception when handling with: {}: {}'.format(
                    handler.__class__.__name__, e))
                result = None

            if not result:
                continue
            if not return_raw:
                result = map(lambda r: r.to_query_result(), result)
            results.extend(result)

        return sorted(results, key=lambda result: result.order)
