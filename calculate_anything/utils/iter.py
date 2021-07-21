from typing import Collection, List, Any, Generator, Iterable, Hashable, Optional, Tuple, Union
from itertools import combinations


def partition(l: Collection[Any], max_parts: Optional[int]=None) -> Generator[Collection[Any], None, None]:
    yields = 0
    for i in range(len(l), 0, -1):
        if max_parts is not None and yields >= max_parts:
            break
        head = l[:i]
        tail = l[i:]
        if not tail:
            yield (head,)
        else:
            yield head, tail
        yields += 1

# https://stackoverflow.com/a/10824484
def flatten(iterable: Iterable[Any]) -> Generator[Any, None, None]:
    iterator, sentinel, stack = iter(iterable), object(), []
    while True:
        value = next(iterator, sentinel)
        if value is sentinel:
            if not stack:
                break
            iterator = stack.pop()
        elif isinstance(value, str):
            yield value
        else:
            try:
                new_iterator = iter(value)
            except TypeError:
                yield value
            else:
                stack.append(iterator)
                iterator = new_iterator


def deduplicate(iterable: Iterable[Hashable]) -> Generator[Hashable, None, None]:
    items_set = set()
    for item in iterable:
        if item in items_set:
            continue
        items_set.add(item)
        yield item
