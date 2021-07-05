from .query_result import QueryResult
from .units import UnitsQueryHandler
from .calculator import CalculatorQueryHandler
from .currency import CurrencyQueryHandler
from ..utils  import Singleton

class QueryHandler(metaclass=Singleton):
    def __init__(self):
        self._handlers = [
            UnitsQueryHandler(),
            CalculatorQueryHandler(),
            CurrencyQueryHandler()
        ]

    def handle(self, query):
        results = []
        for handler in self._handlers:
            result = handler.handle(query)
            if result:
                results.extend(result)

        return sorted(results, key=lambda result: result.order)
