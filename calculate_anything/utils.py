def is_types(value, *types):
    return any(map(lambda t: isinstance(value, t), types))

class Singleton:
    objects = {}

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        if self._func in Singleton.objects:
            return Singleton.objects[self._func]

        instance = self._func(*args, **kwargs)
        Singleton.objects[self._func] = instance
        return instance
