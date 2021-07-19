from typing import List, Any, Generator, Iterable, Hashable
from itertools import combinations


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
