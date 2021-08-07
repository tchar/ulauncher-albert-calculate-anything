'''Functions for multi_re module'''

from typing import Union, List, Optional, Match, Callable, Dict, Type
from calculate_anything.utils.multi_re.multi_re import _MultiRe, MultiRePattern


__all__ = [
    'findall',
    'search',
    'match',
    'fullmatch',
    'split',
    'sub',
    'subn',
    'sub_dict',
    'subn_dict',
    'compile',
]


def _findall(pattern: MultiRePattern, s: str, flags: int, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).findall(s)


def _search(pattern: MultiRePattern, s: str, flags: int, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).search(s)


def _match(pattern: MultiRePattern, s: str, flags: int, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).match(s)


def _fullmatch(
    pattern: MultiRePattern, s: str, flags: int, cls: Type[_MultiRe]
):
    return cls(pattern, sort=True, flags=flags).fullmatch(s)


def _split(
    pattern: MultiRePattern,
    s: str,
    maxsplit: int,
    flags: int,
    cls: Type[_MultiRe],
):
    return cls(pattern, sort=True, flags=flags).split(s, maxsplit)


def _sub(
    pattern: MultiRePattern,
    repl: str,
    s: str,
    count: int,
    flags: int,
    cls: Type[_MultiRe],
):
    return cls(pattern, sort=True, flags=flags).sub(repl, s, count)


def _subn(
    pattern: MultiRePattern,
    repl,
    s: str,
    count: int,
    flags: int,
    cls: Type[_MultiRe],
):
    return cls(pattern, sort=True, flags=flags).subn(repl, s, count)


def _sub_dict(
    pattern: MultiRePattern,
    s: str,
    sort: bool,
    count: int,
    flags: int,
    cls: Type[_MultiRe],
):
    return cls(pattern, sort=sort, flags=flags).sub_dict(s, count)


def _subn_dict(
    pattern: MultiRePattern,
    s: str,
    sort: bool,
    count: int,
    flags: int,
    cls: Type[_MultiRe],
):
    return cls(pattern, sort=sort, flags=flags).subn_dict(s, count)


def _compile(
    pattern: MultiRePattern,
    sort: bool,
    include: bool,
    flags: int,
    cls: Type[_MultiRe],
):
    return cls(pattern, sort, include, flags)


def findall(pattern: MultiRePattern, s: str, flags: int = 0) -> List:
    return _findall(pattern, s, flags, _MultiRe)


def search(
    pattern: MultiRePattern, s: str, flags: int = 0
) -> Optional[Match[str]]:
    return _search(pattern, s, flags, _MultiRe)


def match(
    pattern: MultiRePattern, s: str, flags: int = 0
) -> Optional[Match[str]]:
    return _match(pattern, s, flags, _MultiRe)


def fullmatch(
    pattern: MultiRePattern, s: str, flags: int = 0
) -> Optional[Match[str]]:
    return _fullmatch(pattern, s, flags, _MultiRe)


def split(
    pattern: MultiRePattern,
    s: str,
    maxsplit: int = 0,
    flags: int = 0,
) -> List[str]:
    return _split(pattern, s, maxsplit, flags, _MultiRe)


def sub(
    pattern: MultiRePattern,
    repl: Union[None, str, Callable[[Match], str]],
    s: str,
    count: int = 0,
    flags: int = 0,
) -> str:
    return _sub(pattern, repl, s, count, flags, _MultiRe)


def subn(
    pattern: MultiRePattern,
    repl: Union[None, str, Callable[[Match], str]],
    s: str,
    count: int = 0,
    flags: int = 0,
) -> str:
    return _subn(pattern, repl, s, count, flags, _MultiRe)


def sub_dict(
    pattern: Dict[str, str],
    s: str,
    sort: bool = True,
    count: int = 0,
    flags: int = 0,
) -> str:
    return _sub_dict(pattern, s, sort, count, flags, _MultiRe)


def subn_dict(
    pattern: Dict[str, str],
    s: str,
    sort: bool = True,
    count: int = 0,
    flags: int = 0,
) -> str:
    return _subn_dict(pattern, s, sort, count, flags, _MultiRe)


def compile(
    pattern: MultiRePattern,
    sort: bool = True,
    include: bool = True,
    flags: int = 0,
):
    return _compile(pattern, sort, include, flags, _MultiRe)
