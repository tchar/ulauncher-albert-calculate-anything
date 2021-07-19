import re
import pytest
from collections import OrderedDict
import calculate_anything.utils as utils
from calculate_anything.exceptions import MissingSimpleevalException


def test_get_module():
    assert utils.get_module('os') is not None
    assert utils.get_module('time') is not None
    assert utils.get_module('some module that does not exist') is None
    assert utils.get_module('some other module') is None


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


@pytest.mark.parametrize('input,expected', [
    ([], []),
    ([1], [[[1]]]),
    ([1, 2], [[[1, 2]], [[1], [2]]]),
    ([1, 2, 3], [[[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]], [[1], [2], [3]]])
])
def test_partition(input, expected):
    gen = utils.partition(input)
    assert list(gen) == expected

@pytest.mark.parametrize('input,expected', [
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]), 
    ([1, 2, 1, 2, 4, 6], [1, 2, 4, 6]), 
    (set([1, 2, 3, 4]), set([1, 2, 3, 4])), 
    ([], []), 
])
def test_deduplicate(input, expected):
    _t = type(input)
    assert _t(utils.deduplicate(input)) == expected

@pytest.mark.parametrize('test_spec', [{
    # Test match
    'pattern':  'x^y',
    'args': (),
    'kwargs': {'include': False},
    'f': {
        'func': utils.MultiRe.match,
        'args': ('^yx123',),
        'kwargs': {},
    },
    'assert_func': lambda r: r is not None,
}, {
    # Test fullmatch
    'pattern':  'x^y123',
    'args': (),
    'kwargs': {'include': False},
    'f': {
        'func': utils.MultiRe.fullmatch,
        'args': ('^yx',),
        'kwargs': {},
    },
    'assert_func': lambda r: r is None,
},{
    # Test split
    'pattern':  '=*/+-><^',
    'args': (),
    'kwargs': {'include': True},
    'f': {
        'func': utils.MultiRe.split,
        'args': ('x^2+5x-21*2=0',),
        'kwargs': {},
    },
    'assert_func': lambda r: r == ['x', '^', '2', '+', '5x', '-', '21', '*', '2', '=', '0']
}, {
    # Test findall
    'pattern':  '1=2',
    'args': (),
    'kwargs': {'include': True},
    'f': {
        'func': utils.MultiRe.findall,
        'args': ('=$#=123',),
        'kwargs': {},
    },
    'assert_func': lambda r: r == ['=', '=', '1', '2']
}, {
    # Test search
    'pattern':  '+-*/',
    'args': (),
    'kwargs': {'include': True},
    'f': {
        'func': utils.MultiRe.search,
        'args': ('1+2/3',),
        'kwargs': {},
    },
    'assert_func': lambda r: r is not None and r.group(0) == '+'
}, {
    # Test sub
    'pattern':  'abacd',
    'args': (),
    'kwargs': {'include': True},
    'f': {
        'func': utils.MultiRe.sub,
        'args': ('', 'abracadabra'),
        'kwargs': {},
    },
    'assert_func': lambda r: r == 'rr'
}, {
    # Test subn
    'pattern':  ['Harry Potter'],
    'args': (),
    'kwargs': {'include': True, 'flags': re.IGNORECASE},
    'f': {
        'func': utils.MultiRe.subn,
        'args': ('Lord Voldermort', 'My name is hArRy PotTeR, haRrY PotTer is awesome'),
        'kwargs': {},
    },
    'assert_func': lambda r: r == ('My name is Lord Voldermort, Lord Voldermort is awesome', 2)
}])
def test_multi_re(test_spec):
    multi_re = utils.MultiRe(
        test_spec['pattern'], *test_spec['args'], **test_spec['kwargs'])
    result = test_spec['f']['func'](
        multi_re, *test_spec['f']['args'], **test_spec['f']['kwargs'])
    assert test_spec['assert_func'](result)


@pytest.mark.parametrize('test_spec', [{
    # Test normal
    'string': 'abcdefgh',
    'dict':  {'abcd': '1234', 'efgh': '5678'},
    'expected': ('12345678', 2)
}, {
    'string': 'abcdefgh',
    'dict':  {'abc': '1', 'ef': '2'},
    'expected': ('1d2gh', 2)
}, {
    # Test with substrings
    'string': 'abcdefgh',
    'dict':  {'abcd': '1', 'abc': '2'},
    'expected': ('1efgh', 1)
}, {
    # Test with ordered dict sort
    'string': 'abcdefgh',
    'kwargs': {'sort': False},
    'dict':  OrderedDict([('abc', '2'), ('abcd', '1')]),
    'expected': ('2defgh', 1)
}, {
    # Test with ordered dict no sort
    'string': 'abcdefgh',
    'kwargs': {'sort': True},
    'dict':  OrderedDict([('abc', '2'), ('abcd', '1')]),
    'expected': ('1efgh', 1)
}, {
    # Test ignore case (No ignore)
    'string': 'abcdefgh',
    'kwargs': {'flags': 0},
    'dict':  {'ABCD': '1', 'efgh': '2'},
    'expected': ('abcd2', 1)
}, {
    # Test ignore case (Ignore)
    'string': 'abcdefgh',
    'kwargs': {'flags': re.IGNORECASE},
    'dict':  {'ABCD': '1', 'efgh': '2'},
    'expected': ('12', 2)
}, {
    # Test unicode
    'string': 'αβγδεηζθ',
    'dict':  {'αβγδ': 'ικλμ', 'εηζθ': 'νξοπ'},
    'expected': ('ικλμνξοπ', 2)
}, {
    # Test Exception 1
    'string': 'abcdefgh',
    'dict': {'abc': 1},
    'exception': TypeError,
}, {
    # Test Exception 1
    'string': 'abcdefgh',
    'dict': {1: '1'},
    'exception': TypeError,
}])
def test_multi_re_dict(test_spec):
    string = test_spec['string']
    d = test_spec['dict']
    args = test_spec.get('args', ())
    kwargs = test_spec.get('kwargs', {})

    exception = test_spec.get('exception')
    if exception:
        result = None
        with pytest.raises(exception):
            utils.MultiReDict(d, *args, **kwargs).sub(string)
        return
    
    expected = test_spec['expected']
    result = utils.MultiReDict(d, *args, **kwargs).sub(string)
    assert result == expected[0]
    result = utils.MultiReDict(d, *args, **kwargs).subn(string)
    assert result == expected


@pytest.mark.parametrize('input,expected', [
    ('000000', (0, 0, 0)),
    ('FFFFFF', (255, 255, 255)),
    ('FF0000', (255, 0, 0)),
    ('00FF00', (0, 255, 0)),
    ('00FFFF', (0, 255, 255)),
    ('FF00FF', (255, 0, 255)),
    ('C0C0C0', (192, 192, 192)),
    ('008000', (0, 128, 0)),
    ('800080', (128, 0, 128)),
    ('008080', (0, 128, 128)),
    ('000080', (0, 0, 128)),
    ('ZFASD', ValueError),
    ('A', ValueError),
    (None, TypeError),
])
def test_hex_to_rgb(input, expected):
    if isinstance(expected, tuple):
        assert utils.hex_to_rgb(input)
    else:
        with pytest.raises(expected):
            utils.hex_to_rgb(input)


@pytest.mark.parametrize('input,expected', [
    ((139, 0, 22), (0, 100, 84, 45)),
    ((178, 0, 31), (0, 100, 83, 30)),
    ((0, 174, 114), (100, 0, 34, 32)),
    ((103, 191, 127), (46, 0, 34, 25)),
    ((93, 12, 123), (24, 90, 0, 52)),
    ((121, 55, 139), (13, 60, 0, 45)),
    ((215, 215, 215), (0, 0, 0, 16)),
    ((194, 194, 194), (0, 0, 0, 24)),
    ((1,), ValueError),
    (1, TypeError),
])
def test_rgb_to_cmyk(input, expected):
    if isinstance(expected, tuple):
        result = utils.rgb_to_cmyk(input)
        for r, e in zip(result, expected):
            assert r == pytest.approx(e, 0.1)
    else:
        with pytest.raises(expected):
            utils.rgb_to_cmyk(input)


@pytest.mark.parametrize('input,expected', [
    ((139, 0, 22), (351, 100, 54.4)),
    ((178, 0, 31), (350, 100, 69.8)),
    ((0, 174, 114), (159, 100, 68.2)),
    ((103, 191, 127), (136, 46.1, 74.9)),
    ((93, 12, 123), (284, 90.2, 48.2)),
    ((121, 55, 139), (287, 60.4, 54.5)),
    ((215, 215, 215), (0, 0, 84.3)),
    ((194, 194, 194), (0, 0, 76.1)),
    ((1,), ValueError),
    (1, TypeError),
])
def test_rgb_to_hsv(input, expected):
    if isinstance(expected, tuple):
        result = utils.rgb_to_hsv(input)
        for r, e in zip(result, expected):
            assert r == pytest.approx(e, 0.1)
    else:
        with pytest.raises(expected):
            utils.rgb_to_hsv(input)


@pytest.mark.parametrize('input,expected', [
    ((139, 0, 22), (351, 100, 27.3)),
    ((178, 0, 31), (350, 100, 34.9)),
    ((0, 174, 114), (159, 100, 34.1)),
    ((103, 191, 127), (136, 40.7, 57.6)),
    ((93, 12, 123), (284, 82.2, 26.5)),
    ((121, 55, 139), (287, 43.3, 38.0)),
    ((215, 215, 215), (0, 0, 84.3)),
    ((194, 194, 194), (0, 0, 76.1)),
    ((1,), ValueError),
    (1, TypeError),
])
def test_rgb_to_hsl(input, expected):
    if isinstance(expected, tuple):
        result = utils.rgb_to_hsl(input)
        for r, e in zip(result, expected):
            assert r == pytest.approx(e, 0.1)
    else:
        with pytest.raises(expected):
            utils.rgb_to_hsl(input)


def test_is_integer():
    # Test some integer numbers
    integers = [1, 2.0, 1 + 0j, -17.0]
    for integer in integers:
        assert utils.is_integer(integer)

    # Test some non integer values
    not_integers = [1.5, -1.124, 2 + 5j, 'some text', True]
    for not_integer in not_integers:
        assert not utils.is_integer(not_integer)
