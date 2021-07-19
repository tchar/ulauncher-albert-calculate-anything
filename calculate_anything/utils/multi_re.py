from typing import Union, Iterable, List, Optional, Match, Callable, Dict
import sys
import re
from . import deduplicate

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