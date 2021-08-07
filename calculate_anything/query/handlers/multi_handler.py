from calculate_anything.query.handlers.base import QueryHandler
import inspect
from typing import List, Type, Union
from calculate_anything.calculation.base import Calculation
from calculate_anything.query.result import QueryResult
from calculate_anything.query.handlers.calculator import CalculatorQueryHandler
from calculate_anything.query.handlers.percentages import (
    PercentagesQueryHandler,
)
from calculate_anything.query.handlers.units import UnitsQueryHandler
from calculate_anything.query.handlers.time import TimeQueryHandler
from calculate_anything.query.handlers.base_n import (
    Base16QueryHandler,
    Base10QueryHandler,
    Base2QueryHandler,
    Base8QueryHandler,
)
from calculate_anything import logging


__all__ = ['MultiHandler']


logger = logging.getLogger(__name__)


class MultiHandler:
    def __init__(self) -> None:
        self._handlers = [
            UnitsQueryHandler,
            CalculatorQueryHandler,
            PercentagesQueryHandler,
            TimeQueryHandler,
            Base10QueryHandler,
            Base16QueryHandler,
            Base2QueryHandler,
            Base8QueryHandler,
        ]

    def _handle(
        self,
        query: str,
        *handlers: Union[Type[QueryHandler], QueryHandler],
        return_raw: bool
    ) -> List[Union[Calculation, QueryResult]]:
        results = []

        if not handlers:
            handlers = self._handlers

        for handler in handlers:
            if inspect.isclass(handler):
                handler = handler()
            try:
                result = handler.handle(query)
            except Exception as e:  # pragma: no cover
                hdlr_name = handler.__class__.__name__
                msg = 'Exception in handler: {}: {}'  # pragma: no cover
                msg = msg.format(hdlr_name, e)  # pragma: no cover
                logger.exception(msg)
                result = None

            if not result:
                continue
            if not return_raw:
                result = map(lambda r: r.to_query_result(), result)
            results.extend(result)

        return sorted(results, key=lambda result: result.order)

    def handle_raw(
        self, query: str, *handlers: Union[Type[QueryHandler], QueryHandler]
    ) -> List[Calculation]:
        return self._handle(query, *handlers, return_raw=True)

    def handle(
        self, query: str, *handlers: Union[Type[QueryHandler], QueryHandler]
    ) -> List[QueryResult]:
        return self._handle(query, *handlers, return_raw=False)
