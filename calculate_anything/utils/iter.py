'''Utility functions for iterable related operations.'''

from typing import (
    Collection,
    Any,
    Generator,
    Iterable,
    Hashable,
    Optional,
    Tuple,
)


__all__ = ['partition', 'flatten', 'deduplicate']


def partition(
    collection: Collection[Any], max_parts: Optional[int] = None
) -> Generator[Tuple[Collection[Any]], None, None]:
    '''Partitions a collection into head and tail for all possible partitions up
    to max_parts.

    Args:
        collection (Collection[Any]): A collection to partition.
        max_parts (Union[int, None], optional): Max partitions for the
            provided collection. If None or left empty, it will provide all
            possible partitions.

    Yields:
        Any: Partitions in the format of (head, tail) or (head,) if no tail is
            found.
    '''
    yields = 0
    for i in range(len(collection), 0, -1):
        if max_parts is not None and yields >= max_parts:
            break
        head = collection[:i]
        tail = collection[i:]
        if not tail:
            yield (head,)
        else:
            yield head, tail
        yields += 1


# https://stackoverflow.com/a/10824484


def flatten(iterable: Iterable[Any]) -> Generator[Any, None, None]:
    '''Flattens an iterable

    Args:
        iterable (Iterable[Any]): An iterable to flatten.

    Yields:
        Any: The iterable's elements one by one.
    '''
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


def deduplicate(
    iterable: Iterable[Hashable],
) -> Generator[Hashable, None, None]:
    '''Deduplicates an iterable without changing the order

    Args:
        iterable (Iterable[Any]): An iterable to deduplicate.

    Yields:
        Any: The elements of the provided iterable without duplicates in the
            same order.
    '''
    items_set = set()
    for item in iterable:
        if item in items_set:
            continue
        items_set.add(item)
        yield item
