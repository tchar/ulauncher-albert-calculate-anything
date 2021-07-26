import re
import pytest
from collections import OrderedDict
from calculate_anything.utils import misc as utils_misc
from calculate_anything.utils import iter as utils_iter
from calculate_anything.utils import multi_re
from calculate_anything.utils import colors as utils_colors
from calculate_anything.utils import Singleton
from calculate_anything.exceptions import MissingSimpleevalException


def test_get_module():
    assert utils_misc.get_module('os') is not None
    assert utils_misc.get_module('time') is not None
    assert utils_misc.get_module('some module that does not exist') is None
    assert utils_misc.get_module('some other module') is None


@pytest.mark.parametrize('reverse', [False, True])
def test_is_types(reverse):
    if reverse:
        func = utils_misc.is_not_types
    else:
        func = utils_misc.is_types

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

    assert func(utils_misc.StupidEval)(utils_misc.StupidEval()) != reverse

    with pytest.raises(TypeError):
        func('object')('object')
        func('object')(object)
        func(object)(object)
        func(1, )(int, object)


def test_get_or_default():
    value, type, default, allowed, expected = (1, int, 0, [], 1)
    assert utils_misc.get_or_default(value, type, default) == expected
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (1.1, int, True, [], 1)
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('1.1', int, 'True', [], 'True')
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('1', int, 'True', [], 1)
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('some_text', int, 4, [], 4)
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        'some text', int, 'some other text', [], 'some other text')
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        'some text', int, 'other text', [], 'other text')
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('0', str, 0, [], '0')
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('1.1', float, 0, [], 1.1)
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = ('True', bool, 2, [], True)
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (1, int, 2, [1], 1)
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        1, int, 'some value', ['Test', 1], 1)
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        '1', str, 'some other value', ['1'], '1')
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        'Test', bool, 'some other value', [2], 'some other value')
    assert utils_misc.get_or_default(value, type, default, allowed) == expected
    value, type, default, allowed, expected = (
        'True', bool, 'some other value', [True], True)
    assert utils_misc.get_or_default(value, type, default, allowed) == expected


def test_safe_operation():
    @utils_misc.safe_operation('Safe function operation')
    def some_function(raise_exc):
        if raise_exc:
            raise Exception

    some_function(raise_exc=False)
    some_function(raise_exc=True)

    with utils_misc.safe_operation('Safe operation'):
        raise Exception


def test_is_integer():
    # Test some integer numbers
    integers = [1, 2.0, 1 + 0j, -17.0]
    for integer in integers:
        assert utils_misc.is_integer(integer)

    # Test some non integer values
    not_integers = [1.5, -1.124, 2 + 5j, 'some text', True]
    for not_integer in not_integers:
        assert not utils_misc.is_integer(not_integer)


def test_singleton():
    class SingletonClass(metaclass=Singleton):
        pass

    class SingletonClassWithArgs(SingletonClass):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    @Singleton.function
    def singletonfunc(value):
        return value

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

    v1 = singletonfunc(1)
    v2 = singletonfunc(2)
    assert v1 == v2 == 1


def test_stupid_eval():
    stupid_eval = utils_misc.StupidEval()
    for i in range(10):
        assert stupid_eval.eval(str(i)) == i

    with_exception = [
        '1.1', 'some-text', 'True', '1 + 1',
        True, 1, 1.2, 1 + 2j, utils_misc.StupidEval,
        stupid_eval, None
    ]
    for v in with_exception:
        with pytest.raises(MissingSimpleevalException):
            stupid_eval.eval(v)


test_spec = [{
    'list': [],
    'expected': [],
    'max_parts': None,
}, {
    'list': [1],
    'expected': [([1],)],
    'max_parts': None,
}, {
    'list': [1, 2],
    'expected': [([1, 2],), ([1], [2])],
    'max_parts': None,
}, {
    'list': [1, 2, 3],
    'expected': [([1, 2, 3],), ([1, 2], [3]), ([1], [2, 3])],
    'max_parts': None,
}, {
    'list': [1, 2, 3],
    'expected': [([1, 2, 3],), ([1, 2], [3])],
    'max_parts': 2,
}]


@pytest.mark.parametrize('test_spec', test_spec)
def test_partition(test_spec):
    list_part = test_spec['list']
    max_parts = test_spec['max_parts']
    expected = test_spec['expected']

    gen = utils_iter.partition(list_part, max_parts)
    assert list(gen) == expected


test_spec = [{
    'input': [(1, 2, 3,)],
    'expected': [1, 2, 3]
}, {
    'input': [(1, 2, 3,), (4, 5, 6), 7],
    'expected': [1, 2, 3, 4, 5, 6, 7]
}, {
    'input': [[[[[1]]]], [[[2]], [3, 4]], [5, 6, 7]],
    'expected': [1, 2, 3, 4, 5, 6, 7]
}, {
    'input': [(1, 2, 3,), 'some', ['text', ['in', [[['nested'], 'lists']]]]],
    'expected': [1, 2, 3, 'some', 'text', 'in', 'nested', 'lists']
}, {
    'input': [1, 2, 3, 4],
    'expected': [1, 2, 3, 4]
}, {
    'input': [[[[[[], [[[], []]]]]]]],
    'expected': []
}]


@pytest.mark.parametrize('test_spec', test_spec)
def test_flatten(test_spec):
    input = test_spec['input']
    expected = test_spec['expected']

    assert list(utils_iter.flatten(input)) == expected


test_spec = [{
    'input': [1, 2, 3, 4, 5, 6],
    'expected': [1, 2, 3, 4, 5, 6]
}, {
    'input': [1, 2, 1, 2, 4, 6],
    'expected': [1, 2, 4, 6]
}, {
    'input': set([1, 2, 3, 4]),
    'expected': set([1, 2, 3, 4])
}, {
    'input': [],
    'expected': []
}]


@pytest.mark.parametrize('test_spec', test_spec)
def test_deduplicate(test_spec):
    input = test_spec['input']
    expected = test_spec['expected']

    _t = type(input)
    assert _t(utils_iter.deduplicate(input)) == expected


test_spec = [{
    # Test match
    'pattern':  'x^y',
    'func': multi_re.match,
    'args': ('^yx123',),
    'kwargs': {},
    'assert_func': lambda r: r is not None,
}, {
    # Test fullmatch
    'pattern':  'x^y123',
    'func': multi_re.fullmatch,
    'args': ('^yx',),
    'assert_func': lambda r: r is None,
}, {
    # Test split
    'pattern':  '=*/+-><^',
    'func': multi_re.split,
    'args': ('x^2+5x-21*2=0',),
    'assert_func': lambda r: r == ['x', '^', '2', '+', '5x', '-', '21', '*', '2', '=', '0']
}, {
    # Test findall
    'pattern':  '1=2',
    'args': (),
    'func': multi_re.findall,
    'args': ('=$#=123',),
    'assert_func': lambda r: r == ['=', '=', '1', '2']
}, {
    # Test search
    'pattern':  '+-*/',
    'func': multi_re.search,
    'args': ('1+2/3',),
    'assert_func': lambda r: r is not None and r.group(0) == '+'
}, {
    # Test sub
    'pattern':  'abacd',
    'func': multi_re.sub,
    'args': ('', 'abracadabra'),
    'assert_func': lambda r: r == 'rr'
}, {
    # Test subn
    'pattern':  ['Harry potter', 'Hermione'],
    'func': multi_re.subn,
    'args': ('Lord Voldermort', 'My name is harry potter, HeRmiOnE is awesome'),
    'kwargs': {'flags': re.IGNORECASE},
    'assert_func': lambda r: r == ('My name is Lord Voldermort, Lord Voldermort is awesome', 2)
}]


@pytest.mark.parametrize('test_spec', test_spec)
def test_multi_re(test_spec):
    pattern = test_spec['pattern']
    func = test_spec['func']
    args = test_spec['args']
    kwargs = test_spec.get('kwargs', {})
    assert_func = test_spec['assert_func']

    assert assert_func(func(pattern, *args, **kwargs))

    with pytest.raises(ValueError):
        multi_re.sub_dict(pattern, args[0])
    with pytest.raises(ValueError):
        multi_re.subn_dict(pattern, args[0])
    with pytest.raises(ValueError):
        multi_re.compile(pattern).sub_dict(args[0])
    with pytest.raises(ValueError):
        multi_re.compile(pattern).subn_dict(args[0])


test_spec = [{
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
}]


@pytest.mark.parametrize('test_spec', test_spec)
def test_multi_re_dict(test_spec):
    string = test_spec.get('string')
    d = test_spec['dict']
    kwargs = test_spec.get('kwargs', {})

    obj = multi_re.compile(d, **kwargs)

    exception = test_spec.get('exception')
    if exception and string is None:
        with pytest.raises(exception):
            obj.sub_dict(string)
        with pytest.raises(exception):
            obj.sub_dict(string)
        return

    if string is None:
        raise Exception('Did not provide string')

    string = test_spec['string']
    expected = test_spec['expected']

    result = obj.sub_dict(string)
    assert result == expected[0]
    result = obj.subn_dict(string)
    assert result == expected

    result = multi_re.sub_dict(d, string, **kwargs)
    assert result == expected[0]
    result = multi_re.subn_dict(d, string, **kwargs)
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
        assert utils_colors.hex_to_rgb(input)
    else:
        with pytest.raises(expected):
            utils_colors.hex_to_rgb(input)


@pytest.mark.parametrize('input,expected', [
    ((139, 0, 22), (0, 1, 0.8417, 0.4549)),
    ((178, 0, 31), (0, 1, 0.8258, 0.3020)),
    ((0, 174, 114), (1, 0, 0.3448, 0.3176)),
    ((103, 191, 127), (0.4607, 0, 0.3350, 0.2510)),
    ((93, 12, 123), (0.2439, 0.9024, 0, 0.5176)),
    ((121, 55, 139), (0.1294, 0.6043, 0, 0.4549)),
    ((215, 215, 215), (0, 0, 0, 0.1568)),
    ((194, 194, 194), (0, 0, 0, 0.2392)),
    ((1,), ValueError),
    (1, TypeError),
])
def test_rgb_to_cmyk(input, expected):
    if isinstance(expected, tuple):
        result = utils_colors.rgb_to_cmyk(input)
        assert result == pytest.approx(expected, 0.001)
    else:
        with pytest.raises(expected):
            utils_colors.rgb_to_cmyk(input)


@pytest.mark.parametrize('input,expected', [
    ((139, 0, 22), (350.5035, 1.0, 0.5450)),
    ((178, 0, 31), (349.5507, 1.0, 0.6980)),
    ((0, 174, 114), (159.3103, 1.0, 0.6823)),
    ((103, 191, 127), (136.3636, 0.4607, 0.7490)),
    ((93, 12, 123), (283.7838, 0.9024, 0.4824)),
    ((121, 55, 139), (287.1429, 0.6043, 0.5451)),
    ((215, 215, 215), (0, 0.0, 0.8431)),
    ((194, 194, 194), (0, 0.0, 0.7608)),
    ((1,), ValueError),
    (1, TypeError),
])
def test_rgb_to_hsv(input, expected):
    if isinstance(expected, tuple):
        result = utils_colors.rgb_to_hsv(input)
        assert result == pytest.approx(expected, 0.001)
    else:
        with pytest.raises(expected):
            utils_colors.rgb_to_hsv(input)


@pytest.mark.parametrize('input,expected', [
    ((139, 0, 22), (350.5036, 1.0, 0.2725)),
    ((178, 0, 31), (349.5506, 1.0, 0.3490)),
    ((0, 174, 114), (159.3103, 1.0, 0.3411)),
    ((103, 191, 127), (136.3636, 0.4074, 0.5765)),
    ((93, 12, 123), (283.7838, 0.8222, 0.2647)),
    ((121, 55, 139), (287.1429, 0.4330, 0.3804)),
    ((215, 215, 215), (0, 0, 0.8431)),
    ((194, 194, 194), (0, 0, 0.7608)),
    ((1,), ValueError),
    (1, TypeError),
])
def test_rgb_to_hsl(input, expected):
    if isinstance(expected, tuple):
        result = utils_colors.rgb_to_hsl(input)
        assert result == pytest.approx(expected, 0.001)
    else:
        with pytest.raises(expected):
            utils_colors.rgb_to_hsl(input)
