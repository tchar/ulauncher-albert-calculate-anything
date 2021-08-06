import pytest
from calculate_anything.utils import (
    get_module,
    is_types,
    is_not_types,
    StupidEval,
    get_or_default,
    safe_operation,
    is_integer,
)
from calculate_anything.exceptions import MissingSimpleevalException


def test_get_module():
    assert get_module('os') is not None
    assert get_module('time') is not None
    assert get_module('some module that does not exist') is None
    assert get_module('some other module') is None


@pytest.mark.parametrize('reverse', [False, True])
def test_is_types(reverse):
    if reverse:
        func = is_not_types
    else:
        func = is_types

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

    assert func(StupidEval)(StupidEval()) != reverse

    with pytest.raises(TypeError):
        func('object')('object')
        func('object')(object)
        func(object)(object)
        func(
            1,
        )(int, object)


def test_get_or_default():
    value, _type, default, allowed, expected = (1, int, 0, [], 1)
    assert get_or_default(value, _type, default) == expected
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = (1.1, int, True, [], 1)
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = ('1.1', int, 'True', [], 'True')
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = ('1', int, 'True', [], 1)
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = ('some_text', int, 4, [], 4)
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = (
        'some text',
        int,
        'some other text',
        [],
        'some other text',
    )
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = (
        'some text',
        int,
        'other text',
        [],
        'other text',
    )
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = ('0', str, 0, [], '0')
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = ('1.1', float, 0, [], 1.1)
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = ('True', bool, 2, [], True)
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = (1, int, 2, [1], 1)
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = (
        1,
        int,
        'some value',
        ['Test', 1],
        1,
    )
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = (
        '1',
        str,
        'some other value',
        ['1'],
        '1',
    )
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = (
        'Test',
        bool,
        'some other value',
        [2],
        'some other value',
    )
    assert get_or_default(value, _type, default, allowed) == expected
    value, _type, default, allowed, expected = (
        'True',
        bool,
        'some other value',
        [True],
        True,
    )
    assert get_or_default(value, _type, default, allowed) == expected


def test_safe_operation():
    @safe_operation('Safe function operation')
    def some_function(raise_exc):
        if raise_exc:
            raise Exception

    some_function(raise_exc=False)
    some_function(raise_exc=True)

    with safe_operation('Safe operation'):
        raise Exception


def test_is_integer():
    # Test some integer numbers
    integers = [1, 2.0, 1 + 0j, -17.0]
    for integer in integers:
        assert is_integer(integer)

    # Test some non integer values
    not_integers = [1.5, -1.124, 2 + 5j, 'some text', True]
    for not_integer in not_integers:
        assert not is_integer(not_integer)


def test_stupid_eval():
    stupid_eval = StupidEval()
    for i in range(10):
        assert stupid_eval.eval(str(i)) == i
        assert stupid_eval.eval(str(i + 0.1)) == pytest.approx(i + 0.1)
        assert stupid_eval.eval(str(i + 0.5j)) == pytest.approx(i + 0.5j)

    with_exception = [
        'some-text',
        'True',
        '1 + 1',
        True,
        1,
        1.2,
        1 + 2j,
        StupidEval,
        stupid_eval,
        None,
    ]
    for v in with_exception:
        with pytest.raises(MissingSimpleevalException):
            stupid_eval.eval(v)
