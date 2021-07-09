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
