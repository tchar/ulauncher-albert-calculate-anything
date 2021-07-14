from .handlers import UnitsQueryHandler
from .handlers import CalculatorQueryHandler
from .handlers import CurrencyQueryHandler
from .handlers import PercentagesQueryHandler
from .handlers import TimeQueryHandler
from .handlers import (
    Base16QueryHandler, Base10QueryHandler,
    Base2QueryHandler, Base8QueryHandler
)
from ..utils  import Singleton

class QueryHandler(metaclass=Singleton):
    def __init__(self):
        self._handlers = [
            UnitsQueryHandler(),
            CalculatorQueryHandler(),
            # CurrencyQueryHandler(),
            PercentagesQueryHandler(),
            TimeQueryHandler(),
            Base10QueryHandler(),
            Base16QueryHandler(),
            Base8QueryHandler(),
            Base2QueryHandler()
        ]

    def handle(self, query, *handlers, return_raw=False):
        handlers = set(handlers)
        results = []
        for handler in self._handlers:
            if handlers and not handler.__class__ in handlers:
                continue
            result = handler.handle(query)
            if not result:
                continue
            if not return_raw:
                result = map(lambda r: r.to_query_result(), result)
            results.extend(result)

        return sorted(results, key=lambda result: result.order)
