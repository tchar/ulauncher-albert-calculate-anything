from calculate_anything.utils import Singleton


def test_singleton():
    class SingletonClass(metaclass=Singleton):
        pass

    class SingletonClassWithArgs(SingletonClass):
        def __init__(self, v):
            self._v = v

        @property
        def v(self):
            return self._v

        @v.setter
        def v(self, v):
            self._v = v

    @Singleton.function
    def singletonfunc(value):
        return value

    t1 = SingletonClass()
    t2 = SingletonClass()

    assert t1 == t2
    assert id(t1) == id(t2)

    t1 = SingletonClassWithArgs(1)
    t2 = SingletonClassWithArgs(2)

    assert t1 == t2
    assert id(t1._v) == id(t2._v)

    assert t1._v == t2._v == 1
    assert t1.v == t2.v == 1

    t1.v = 2
    assert t1._v == t2._v == 2
    assert t1.v == t2.v == 2

    t2.v = 4
    assert t1._v == t2._v == 4
    assert t1.v == t2.v == 4

    t2._v = 16
    assert t1._v == t2._v == 16
    assert t1.v == t2.v == 16

    assert t1 == t2

    v1 = singletonfunc(1)
    v2 = singletonfunc(2)
    assert v1 == v2 == 1
