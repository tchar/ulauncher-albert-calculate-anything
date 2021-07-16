import re
import pytest
from collections import OrderedDict
import calculate_anything.utils as utils
from calculate_anything.exceptions import MissingSimpleevalException


@pytest.mark.parametrize('reverse', [False, True])
def test_is_types(reverse):
    if reverse:
        func = utils.is_not_types
    else:
        func = utils.is_types

    for i in range(-1, 10):
        assert func(int)(i) != reverse
        assert func(int)(i + 0.2) == reverse
        assert func(float)(i + 0.1) != reverse
        assert func(float)(i) == reverse
        assert func(str)(str(i)) != reverse
        assert func(str)(i) == reverse
        assert func(bool)(bool(i)) != reverse
        assert func(bool)(i) == reverse

    # Multi
    assert func(int, float, str)(1) != reverse
    assert func(int, float, str)('test_string') != reverse

    # Assert opposite
    assert func(str)(2.5) == reverse
    assert func(int, float, complex)('test_string') == reverse

    assert func(utils.StupidEval)(utils.StupidEval()) != reverse

    with pytest.raises(TypeError):
        func('object')('object')
        func('object')(object)
        func(object)(object)
        func(1, )(int, object)


def test_get_or_default():
    value, type, default, allowed, expected = (1, int, 0, [], 1)
    assert utils.get_or_default(value, type, default) == expected
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (1.1, int, True, [], 1)
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('1.1', int, 'True', [], 'True')
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('1', int, 'True', [], 1)
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('some_text', int, 4, [], 4)
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        'some text', int, 'some other text', [], 'some other text')
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        'some text', int, 'other text', [], 'other text')
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('0', str, 0, [], '0')
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('1.1', float, 0, [], 1.1)
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('True', bool, 2, [], True)
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (1, int, 2, [1], 1)
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        1, int, 'some value', ['Test', 1], 1)
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        '1', str, 'some other value', ['1'], '1')
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        'Test', bool, 'some other value', [2], 'some other value')
    assert utils.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        'True', bool, 'some other value', [True], True)
    assert utils.get_or_default(value, type, default, allowed) == expected


def test_singleton():
    class SingletonClass(metaclass=utils.Singleton):
        pass

    class SingletonClassWithArgs(SingletonClass):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    t1 = SingletonClass()
    t2 = SingletonClass()

    assert t1 == t2
    assert id(t1) == id(t2)

    t1 = SingletonClassWithArgs(1, 2, a='a', b='b')
    t2 = SingletonClassWithArgs(3, 4, c='c', d='d')

    assert t1.args == t2.args
    assert id(t1.args) == id(t2.args)
    assert t1.kwargs == t2.kwargs
    assert id(t1.kwargs) == id(t2.kwargs)
    assert t1 == t2
    assert id(t1) == id(t2)


def test_stupid_eval():
    stupid_eval = utils.StupidEval()
    for i in range(10):
        assert stupid_eval.eval(str(i)) == i

    with_exception = [
        '1.1', 'some-text', 'True', '1 + 1',
        True, 1, 1.2, 1 + 2j, utils.StupidEval,
        stupid_eval, None
    ]
    for v in with_exception:
        with pytest.raises(MissingSimpleevalException):
            stupid_eval.eval(v)


def test_partition():
    # TODO: Complete
    pass


def test_or_regex():
    # TODO: Complete
    pass


def test_replace_dict_re_func():
    f = utils.replace_dict_re_func

    s = 'abcdefgh'

    # Test normal
    d = {'abcd': '1234', 'efgh': '5678'}
    assert f(d)(s) == '12345678'

    d = {'abc': '1', 'ef': '2'}
    assert f(d)(s) == '1d2gh'

    # Test with substrings
    d = {'abcd': '1', 'abc': '2'}
    assert f(d)(s) == '1efgh'

    # Test with ordered dict
    d = OrderedDict([('abc', '2'), ('abcd', '1')])
    assert f(d, sort=False)(s) == '2defgh'
    assert f(d, sort=True)(s) == '1efgh'

    # Test ignore case
    d = {'ABCD': '1', 'efgh': '2'}
    assert f(d, flags=0)(s) == 'abcd2'
    assert f(d, flags=re.IGNORECASE)(s) == '12'

    # Test unicode
    s_unicode = 'αβγδεηζθ'
    d = {'αβγδ': 'ικλμ', 'εηζθ': 'νξοπ'}
    assert f(d)(s_unicode) == 'ικλμνξοπ'

    # Test exceptions
    with pytest.raises(TypeError):
        assert f({'abc': 1})(s)
        assert f({1: '1'})(s)


def test_hex_to_rgb():
    # TODO: Complete
    pass


def test_rgb_to_cmyk():
    # TODO: Complete
    pass


def test_rgb_to_hsv():
    # TODO: Complete
    pass


def test_rgb_to_hsl():
    # TODO: Complete
    pass


def test_is_integer():
    # Test some integer numbers
    integers = [1, 2.0, 1 + 0j, -17.0]
    for integer in integers:
        assert utils.is_integer(integer)

    # Test some non integer values
    not_integers = [1.5, -1.124, 2 + 5j, 'some text', True]
    for not_integer in not_integers:
        assert not utils.is_integer(not_integer)
