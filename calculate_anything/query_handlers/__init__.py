from .units import UnitsQueryHandler
from .calculator import CalculatorQueryHandler
from .currency import CurrencyQueryHandler
from ..utils  import Singleton

class QueryHandler:
    def __init__(self):
        self._handlers = [
            UnitsQueryHandler.get_instance(),
            CalculatorQueryHandler.get_instance(),
            CurrencyQueryHandler.get_instance()
        ]

    def handle(self, query):
        results = []
        for handler in self._handlers:
            result = handler.handle(query)
            if result:
                results.extend(result)

        return sorted(results, key=lambda result: result.get('order', 0))

    @classmethod
    @Singleton
    def get_instance(cls):
        return cls()