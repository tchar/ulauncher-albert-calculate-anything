from calculate_anything.exceptions import ExtendedException
from typing import Any, Optional


__all__ = ['QueryResult']


class QueryResult:
    def __init__(
        self,
        icon: str = '',
        name: str = '',
        description: str = '',
        clipboard: Optional[str] = None,
        value: Any = None,
        error: Optional[ExtendedException] = None,
        order: int = 0,
    ):
        self.icon = icon
        self.name = name
        self.description = description
        self.clipboard = clipboard
        self.value = value
        self.error = error
        self.order = order
