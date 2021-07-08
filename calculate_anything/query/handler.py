from .handlers import UnitsQueryHandler
from .handlers import CalculatorQueryHandler
from .handlers import CurrencyQueryHandler
from .handlers import PercentagesQueryHandler
from .handlers import TimeQueryHandler
from ..utils  import Singleton

class QueryHandler(metaclass=Singleton):
    def __init__(self):
        self._handlers = [
            UnitsQueryHandler(),
            CalculatorQueryHandler(),
            CurrencyQueryHandler(),
            PercentagesQueryHandler(),
            TimeQueryHandler()
        ]

    def handle(self, query, *handlers):
        results = []
        for handler in self._handlers:
            if handlers and not handler.__class__ in handlers:
                continue
            result = handler.handle(query)
            if result:
                results.extend(result)

        return sorted(results, key=lambda result: result.order)
