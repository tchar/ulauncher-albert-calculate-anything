from calculate_anything.utils.misc import (
    get_module, is_types, is_not_types, get_or_default,
    is_integer, StupidEval, safe_operation, lock
)
from calculate_anything.utils.iter import (
    partition, flatten, deduplicate
)
from calculate_anything.utils.singleton import Singleton


__all__ = ['get_module', 'is_types', 'is_not_types', 'get_or_default',
           'is_integer', 'StupidEval', 'safe_operation', 'lock',
           'partition', 'flatten', 'deduplicate', 'Singleton']
