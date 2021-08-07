from typing import Any, Callable, List, Optional, TypeVar
from functools import wraps
from calculate_anything.calculation.base import Calculation


__all__ = ['QueryHandler']


RT = TypeVar('RT')


class QueryHandler:
    class Decorators:
        @staticmethod
        def can_handle(func: Callable[..., RT]) -> Callable[..., RT]:
            @wraps(func)
            def _wrapper(
                self: 'QueryHandler', query: str, *args, **kwargs
            ) -> Any:
                if not self.can_handle(query):
                    return None
                query = self.query_without_keyword(query)
                return func(self, query, *args, **kwargs)

            return _wrapper

    def __init__(self, keyword: str = '') -> None:
        self._keyword = keyword

    @property
    def keyword(self) -> str:
        return self._keyword

    @keyword.setter
    def keyword(self, kw: str) -> None:
        self._keyword = kw

    def query_without_keyword(self, query: str, check: bool = False) -> str:
        if check and not self.can_handle(query):
            return ''
        return query[len(self.keyword) :]

    def can_handle(self, query: str) -> bool:
        if not query.startswith(self.keyword):
            return False
        return True

    def handle_raw(
        self, query: str, *args: Any, **kwargs: Any
    ) -> Optional[List[Calculation]]:
        pass

    @Decorators.can_handle
    def handle(
        self, query: str, *args: Any, **kwargs: Any
    ) -> Optional[List[Calculation]]:
        return self.handle_raw(query, *args, **kwargs)
