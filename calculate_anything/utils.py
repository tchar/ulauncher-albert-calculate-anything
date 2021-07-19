import importlib
from typing import (
    Any, Callable, Collection, Container, Dict,
    Generator, Hashable, Iterable, List, Match, Optional, Tuple, Type, Union,
)
from types import ModuleType
import sys
import re
from itertools import combinations
from .exceptions import MissingSimpleevalException


def get_module(name: str) -> Union[None, ModuleType]:
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        return None


def is_types(*types: List[Type[Any]]) -> bool:
    return lambda value: any(map(lambda t: isinstance(value, t), types))


def is_not_types(*types: List[Type[Any]]) -> bool:
    return lambda value: not is_types(*types)(value)


def get_or_default(value: Any, _type: Type[Any], default: Any,
                   allowed_values: Optional[Union[Container, Iterable]] = None) -> Any:
    try:
        value = _type(value)
        if allowed_values and value not in allowed_values:
            return default
        return value
    except Exception:
        return default


class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class StupidEval:
    def __init__(self, *args: Any, **kwargs: Any):
        self.operators = {}

    def eval(self, query: str) -> int:
        try:
            if not isinstance(query, str):
                raise MissingSimpleevalException
            return int(query)
        except (ValueError, TypeError):
            raise MissingSimpleevalException


def partition(l: List[Any]) -> Generator[List[Any], None, None]:
    for i in range(len(l)):
        for comb in combinations(range(1, len(l)), i):
            result = []
            prev = 0
            for e in comb:
                result.append(l[prev:e])
                prev = e
            result.append(l[prev:])
            yield result


def deduplicate(value: Iterable[Hashable]) -> Generator[Hashable, None, None]:
    value_set = set()
    for v in value:
        if v in value_set:
            continue
        value_set.add(v)
        yield v


class MultiRe:
    def __init__(self, value: Union[Iterable[str], str],
                 sort: bool = True, include: bool = True, flags: int = 0):
        value = deduplicate(value)
        sort = (sort or isinstance(value, set) or (
                isinstance(value, dict) and sys.version_info[:2] < (3, 7)))
        if sort:
            value = sorted(value, key=len, reverse=True)

        regex = r'|'.join(map(re.escape, value))

        if include:
            regex = '(' + regex + ')'

        self._re = re.compile(regex, flags=flags)

    def findall(self, s: str) -> List:
        return self._re.findall(s)

    def search(self, s: str) -> Optional[Match[str]]:
        return self._re.search(s)

    def match(self, s: str) -> Optional[Match[str]]:
        return self._re.match(s)

    def fullmatch(self, s: str) -> Optional[Match[str]]:
        return self._re.fullmatch(s)

    def split(self, s: str, maxsplit: int = 0) -> List[str]:
        return self._re.split(s, maxsplit)

    def _sub(self, repl, s, count, func):
        return func(repl, s, count)

    def sub(self, repl: Union[None, str, Callable[[Match], str]], s: str, count: int = 0) -> str:
        return self._sub(repl, s, count, self._re.sub)

    def subn(self, repl: Union[None, str, Callable[[Match], str]], s: str, count: int = 0) -> str:
        return self._sub(repl, s, count, self._re.subn)


class MultiReDict(MultiRe):
    def __init__(self, value: Dict[str, str],
                 sort: bool = True, include: bool = False, flags: int = 0):

        if flags & re.IGNORECASE:
            value = {k.lower(): v for k, v in value.items()}

        sort = sort or sys.version_info[:2] < (3, 7)
        super().__init__(value.keys(), sort=sort, include=include, flags=flags)

        self._flags = flags
        self._replace_dict = value

    def _sub(self, s, count, func):
        if self._flags & re.IGNORECASE:
            def repl(m): return self._replace_dict[m.group(0).lower()]
        else:
            def repl(m): return self._replace_dict[m.group(0)]
        return super()._sub(repl, s, count, func)

    def sub(self, s: str, count: int = 0) -> str:
        return self._sub(s, count, self._re.sub)

    def subn(self, s: str, count: int = 0) -> str:
        return self._sub(s, count, self._re.subn)


def hex_to_rgb(hex: str) -> Tuple[int, int, int]:
    r, g, b = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
    return r, g, b


# https://ariya.blogspot.com/2008/07/converting-between-hsl-and-hsv.html
def rgb_to_cmyk(rgb: Collection[int]) -> Tuple[float, float, float]:
    r, g, b = map(lambda v: v / 255., rgb)
    k = 1 - max(r, g, b)
    c = (1 - r - k) / (1 - k) if k != 1 else 0
    m = (1 - g - k) / (1 - k) if k != 1 else 0
    y = (1 - b - k) / (1 - k) if k != 1 else 0
    c, m, y, k = 100 * c, 100 * m, 100 * y, 100 * k
    return c, m, y, k


# https://ariya.blogspot.com/2008/07/converting-between-hsl-and-hsv.html
def rgb_to_hsv(rgb: Collection[int]) -> Tuple[float, float, float]:
    r, g, b = map(lambda v: v / 255., rgb)
    cmax, cmin = max(r, g, b), min(r, g, b)
    delta = cmax - cmin
    if delta == 0:
        h = 0
    elif cmax == r:
        h = ((g - b) / delta) % 6
    elif cmax == g:
        h = ((b - r) / delta) + 2
    elif cmax == b:
        h = ((r - g) / delta) + 4
    h *= 60
    s = 0 if cmax == 0 else 100 * delta / cmax
    v = 100 * cmax
    return h, s, v


# https://ariya.blogspot.com/2008/07/converting-between-hsl-and-hsv.html
def rgb_to_hsl(rgb: Collection[int]) -> Tuple[float, float, float]:
    r, g, b = map(lambda v: v / 255., rgb)
    cmax, cmin = max(r, g, b), min(r, g, b)
    delta = cmax - cmin
    if delta == 0:
        h = 0
    elif cmax == r:
        h = ((g - b) / delta) % 6
    elif cmax == g:
        h = ((b - r) / delta) + 2
    elif cmax == b:
        h = ((r - g) / delta) + 4
    h *= 60
    l = (cmax + cmin) / 2.
    s = 0 if delta == 0 else 100 * delta / (1 - abs(2 * l - 1))
    l = 100 * l
    return h, s, l


def is_integer(value: Any) -> bool:
    if isinstance(value, float):
        if value.is_integer():
            return True
        return False
    if isinstance(value, complex):
        return value.imag == 0
    if isinstance(value, bool):
        return False
    return isinstance(value, int)
