import pytest
import re
from collections import OrderedDict
from calculate_anything.utils import multi_re


test_spec = [
    {
        # Test match
        'pattern': 'x^y',
        'func': multi_re.match,
        'args': ('^yx123',),
        'kwargs': {},
        'assert_func': lambda r: r is not None,
    },
    {
        # Test fullmatch
        'pattern': 'x^y123',
        'func': multi_re.fullmatch,
        'args': ('^yx',),
        'assert_func': lambda r: r is None,
    },
    {
        # Test split
        'pattern': '=*/+-><^',
        'func': multi_re.split,
        'args': ('x^2+5x-21*2=0',),
        'assert_func': lambda r: r
        == ['x', '^', '2', '+', '5x', '-', '21', '*', '2', '=', '0'],
    },
    {
        # Test findall
        'pattern': '1=2',
        'func': multi_re.findall,
        'args': ('=$#=123',),
        'assert_func': lambda r: r == ['=', '=', '1', '2'],
    },
    {
        # Test search
        'pattern': '+-*/',
        'func': multi_re.search,
        'args': ('1+2/3',),
        'assert_func': lambda r: r is not None and r.group(0) == '+',
    },
    {
        # Test sub
        'pattern': 'abacd',
        'func': multi_re.sub,
        'args': ('', 'abracadabra'),
        'assert_func': lambda r: r == 'rr',
    },
    {
        # Test subn
        'pattern': ['Harry potter', 'Hermione'],
        'func': multi_re.subn,
        'args': (
            'Lord Voldermort',
            'My name is harry potter, HeRmiOnE is awesome',
        ),
        'kwargs': {'flags': re.IGNORECASE},
        'assert_func': lambda r: r
        == ('My name is Lord Voldermort, Lord Voldermort is awesome', 2),
    },
]


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


test_spec = [
    {
        # Test normal
        'string': 'abcdefgh',
        'dict': {'abcd': '1234', 'efgh': '5678'},
        'expected': ('12345678', 2),
    },
    {
        'string': 'abcdefgh',
        'dict': {'abc': '1', 'ef': '2'},
        'expected': ('1d2gh', 2),
    },
    {
        # Test with substrings
        'string': 'abcdefgh',
        'dict': {'abcd': '1', 'abc': '2'},
        'expected': ('1efgh', 1),
    },
    {
        # Test with ordered dict sort
        'string': 'abcdefgh',
        'kwargs': {'sort': False},
        'dict': OrderedDict([('abc', '2'), ('abcd', '1')]),
        'expected': ('2defgh', 1),
    },
    {
        # Test with ordered dict no sort
        'string': 'abcdefgh',
        'kwargs': {'sort': True},
        'dict': OrderedDict([('abc', '2'), ('abcd', '1')]),
        'expected': ('1efgh', 1),
    },
    {
        # Test ignore case (No ignore)
        'string': 'abcdefgh',
        'kwargs': {'flags': 0},
        'dict': {'ABCD': '1', 'efgh': '2'},
        'expected': ('abcd2', 1),
    },
    {
        # Test ignore case (Ignore)
        'string': 'abcdefgh',
        'kwargs': {'flags': re.IGNORECASE},
        'dict': {'ABCD': '1', 'efgh': '2'},
        'expected': ('12', 2),
    },
    {
        # Test unicode
        'string': 'αβγδεηζθ',
        'dict': {'αβγδ': 'ικλμ', 'εηζθ': 'νξοπ'},
        'expected': ('ικλμνξοπ', 2),
    },
]


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
