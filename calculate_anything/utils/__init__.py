from calculate_anything.utils.misc import (
    get_module, is_types, is_not_types,
    get_or_default, is_integer, StupidEval,
    safe_operation
)
from calculate_anything.utils.iter import partition, flatten, deduplicate
from calculate_anything.utils.colors import (
    hex_to_rgb, rgb_to_cmyk, rgb_to_hsv, rgb_to_hsl
)
from calculate_anything.utils.singleton import Singleton, singleton
from calculate_anything.utils.datetime import merge_dates, parsedatetime_str