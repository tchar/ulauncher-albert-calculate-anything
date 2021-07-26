from typing import Tuple, Collection


__all__ = ['hex_to_rgb', 'rgb_to_cmyk', 'rgb_to_hsv', 'rgb_to_hsl']


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
    s = 0 if cmax == 0 else delta / cmax
    v = cmax
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
    s = 0 if delta == 0 else delta / (1 - abs(2 * l - 1))
    return h, s, l
