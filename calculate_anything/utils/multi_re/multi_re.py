from collections import OrderedDict
from typing import Union, Iterable, List, Optional, Match, Callable, Dict
import sys
import re
from calculate_anything.utils.iter import deduplicate


MultiRePattern = Union[
    Dict[str, str], Iterable[str], str, 'OrderedDict[str, str]'
]


class _MultiRe:
    COMPATIBILITY_ITER = 0
    COMPATIBILITY_DICT = 1

    def __init__(
        self,
        value: MultiRePattern,
        sort: bool = True,
        include: bool = True,
        flags: int = 0,
    ) -> None:
        if isinstance(value, dict):
            self._mode = _MultiRe.COMPATIBILITY_DICT
            if flags & re.IGNORECASE:
                value = {k.lower(): v for k, v in value.items()}
            if sys.version_info[:2] < (3, 7) and not isinstance(
                value, OrderedDict
            ):  # pragma: no cover
                sort = True  # pragma: no cover
            self._replace_dict = value
        elif isinstance(value, set):
            sort = True
            self._mode = _MultiRe.COMPATIBILITY_ITER
            self._replace_dict = None
        else:
            self._mode = _MultiRe.COMPATIBILITY_ITER
            self._replace_dict = None
            value = deduplicate(value)

        if sort:
            value = sorted(value, key=len, reverse=True)

        regex = r'|'.join(map(re.escape, value))
        if include:
            regex = '({})'.format(regex)

        self._re = re.compile(regex, flags=flags)
        self._flags = flags

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

    def _sub_dict(self, s, count, func):
        if self._flags & re.IGNORECASE:

            def repl(m):
                return self._replace_dict[m.group(0).lower()]

        else:

            def repl(m):
                return self._replace_dict[m.group(0)]

        return self._sub(repl, s, count, func)

    def sub(
        self, repl: Union[str, Callable[[Match], str]], s: str, count: int = 0
    ) -> str:
        return self._sub(repl, s, count, self._re.sub)

    def subn(
        self, repl: Union[str, Callable[[Match], str]], s: str, count: int = 0
    ) -> str:
        return self._sub(repl, s, count, self._re.subn)

    def sub_dict(self, s: str, count: int = 0) -> str:
        if not self._mode & _MultiRe.COMPATIBILITY_DICT:
            raise ValueError('Did not provide dictionary as pattern')
        return self._sub_dict(s, count, self._re.sub)

    def subn_dict(self, s: str, count: int = 0) -> str:
        if not self._mode & _MultiRe.COMPATIBILITY_DICT:
            raise ValueError('Did not provide dictionary as pattern')
        return self._sub_dict(s, count, self._re.subn)
