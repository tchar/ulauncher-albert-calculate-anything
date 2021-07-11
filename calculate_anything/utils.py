import re
from itertools import combinations

def is_types(value, *types):
    return any(map(lambda t: isinstance(value, t), types))

def get_or_default(value, _type, default):
    try:
        return _type(value)
    except Exception:
        return default

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def partition(l):
    for i in range(len(l)):
        for comb in combinations(range(1, len(l)), i):
            result = []
            prev = 0
            for e in comb:
                result.append(l[prev:e])
                prev = e
            result.append(l[prev:])
            yield result

def or_regex(values, include=True):
    regex = sorted(values, key=len, reverse=True)
    regex = map(re.escape, regex)
    regex = '|'.join(regex)
    if include: regex = '(' + regex + ')'
    return regex

def hex_to_rgb(hex):
    r, g, b = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
    return r, g, b

def rgb_to_cmyk(rgb):
    r, g, b = map(lambda v: v / 255., rgb)
    k = 1 - max(r, g, b)
    c = (1 - r - k) / (1 - k) if k != 1 else 0
    m = (1 - g - k) / (1 - k) if k != 1 else 0
    y = (1 - b - k) / (1 - k) if k != 1 else 0
    c, m, y, k = 100 * c, 100 * m, 100 * y, 100 * k
    return c, m, y, k

def rgb_to_hsv(rgb):
    r, g, b = map(lambda v: v / 255., rgb)
    cmax, cmin = max(r, g, b), min(r, g, b)
    delta = cmax - cmin
    if delta == 0: h = 0
    elif cmax == r: h = ((g - b) / delta) % 6
    elif cmax == g: h = ((b - r) / delta) + 2
    elif cmax == b: h = ((r - g) / delta) + 4
    h *= 60
    s = 0 if cmax == 0 else 100 * delta / cmax
    v = 100 * cmax
    return h, s, v

# https://ariya.blogspot.com/2008/07/converting-between-hsl-and-hsv.html
def rgb_to_hsl(rgb):
    r, g, b = map(lambda v: v / 255., rgb)
    cmax, cmin = max(r, g, b), min(r, g, b)
    delta = cmax - cmin
    if delta == 0: h = 0
    elif cmax == r: h = ((g - b) / delta) % 6
    elif cmax == g: h = ((b - r) / delta) + 2
    elif cmax == b: h = ((r - g) / delta) + 4
    h *= 60
    l = (cmax + cmin) / 2.
    s = 0 if delta == 0 else 100 * delta / (1 - abs(2 * l - 1))
    l = 100 * l
    return h, s, l

def is_integer(value):
    if isinstance(value, float):
        if value.is_integer():
            return True
        return False
    if isinstance(value, complex):
        return value.imag == 0
    return isinstance(value, int)
