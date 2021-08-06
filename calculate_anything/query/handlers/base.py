from typing import Optional
from functools import wraps
from calculate_anything.calculation import Calculation


class QueryHandler:
    class Decorators:
        @staticmethod
        def can_handle(func):
            @wraps(func)
            def _wrapper(self: 'QueryHandler', query: str, *args, **kwargs):
                if not self.can_handle(query):
                    return None
                query = self.query_without_keyword(query)
                return func(self, query, *args, **kwargs)

            return _wrapper

    def __init__(self, keyword: str = ''):
        self._keyword = keyword

    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, kw):
        self._keyword = kw

    def query_without_keyword(self, query, check=False):
        if check and not self.can_handle(query):
            return ''
        return query[len(self.keyword) :]

    def can_handle(self, query):
        if not query.startswith(self.keyword):
            return False
        return True

    def handle_raw(self, query, *args, **kwargs) -> Optional[Calculation]:
        pass

    @Decorators.can_handle
    def handle(self, query, *args, **kwargs) -> Optional[Calculation]:
        return self.handle_raw(query, *args, **kwargs)
