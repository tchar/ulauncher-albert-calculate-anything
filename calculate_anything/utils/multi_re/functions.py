from typing import Union, Iterable, List, Optional, Match, Callable, Dict, Type
from calculate_anything.utils.multi_re.multi_re import _MultiRe


__all__ = ['findall', 'search', 'match', 'fullmatch', 'split',
           'sub', 'subn', 'sub_dict', 'subn_dict', 'compile']


def _findall(pattern, s, flags, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).findall(s)


def _search(pattern, s, flags, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).search(s)


def _match(pattern, s, flags, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).match(s)


def _fullmatch(pattern, s, flags, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).fullmatch(s)


def _split(pattern, s, maxsplit, flags, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).split(s, maxsplit)


def _sub(pattern, repl, s, count, flags, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).sub(repl, s, count)


def _subn(pattern, repl, s, count, flags, cls: Type[_MultiRe]):
    return cls(pattern, sort=True, flags=flags).subn(repl, s, count)


def _sub_dict(pattern, s, count, flags, sort, cls: Type[_MultiRe]):
    return cls(pattern, sort=sort, flags=flags).sub_dict(s, count)


def _subn_dict(pattern, s, count, flags, sort, cls: Type[_MultiRe]):
    return cls(pattern, sort=sort, flags=flags).subn_dict(s, count)


def _compile(pattern, sort, include, flags, cls: Type[_MultiRe]):
    return cls(pattern, sort, include, flags)


def findall(pattern: Union[Iterable[str], str],
            s: str, flags: int = 0) -> List:
    return _findall(pattern, s, flags, _MultiRe)


def search(pattern: Union[Iterable[str], str],
           s: str, flags: int = 0) -> Optional[Match[str]]:
    return _search(pattern, s, flags, _MultiRe)


def match(pattern: Union[Iterable[str], str],
          s: str, flags: int = 0) -> Optional[Match[str]]:
    return _match(pattern, s, flags, _MultiRe)


def fullmatch(pattern: Union[Iterable[str], str],
              s: str, flags: int = 0) -> Optional[Match[str]]:
    return _fullmatch(pattern, s, flags, _MultiRe)


def split(pattern: Union[Iterable[str], str],
          s: str, maxsplit: int = 0, flags: int = 0) -> List[str]:
    return _split(pattern, s, maxsplit, flags, _MultiRe)


def sub(pattern: Union[Iterable[str], str],
        repl: Union[None, str, Callable[[Match], str]],
        s: str, count: int = 0, flags: int = 0) -> str:
    return _sub(pattern, repl, s, count, flags, _MultiRe)


def subn(pattern: Union[Iterable[str], str],
         repl: Union[None, str, Callable[[Match], str]],
         s: str, count: int = 0, flags: int = 0) -> str:
    return _subn(pattern, repl, s, count, flags, _MultiRe)


def sub_dict(pattern: Dict[str, str], s: str,
             count: int = 0, flags: int = 0, sort: bool = True) -> str:
    return _sub_dict(pattern, s, count, flags, sort, _MultiRe)


def subn_dict(pattern: Dict[str, str], s: str,
              count: int = 0, flags: int = 0, sort: bool = True) -> str:
    return _subn_dict(pattern, s, count, flags, sort, _MultiRe)


def compile(pattern: Union[Iterable[str], str], sort: bool = True,
            include: bool = True, flags: int = 0):
    return _compile(pattern, sort, include, flags, _MultiRe)
