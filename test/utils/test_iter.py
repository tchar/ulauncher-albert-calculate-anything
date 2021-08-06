import pytest
from calculate_anything.utils import partition, flatten, deduplicate

test_spec = [
    {
        'list': [],
        'expected': [],
        'max_parts': None,
    },
    {
        'list': [1],
        'expected': [([1],)],
        'max_parts': None,
    },
    {
        'list': [1, 2],
        'expected': [([1, 2],), ([1], [2])],
        'max_parts': None,
    },
    {
        'list': [1, 2, 3],
        'expected': [([1, 2, 3],), ([1, 2], [3]), ([1], [2, 3])],
        'max_parts': None,
    },
    {
        'list': [1, 2, 3],
        'expected': [([1, 2, 3],), ([1, 2], [3])],
        'max_parts': 2,
    },
]


@pytest.mark.parametrize('test_spec', test_spec)
def test_partition(test_spec):
    list_part = test_spec['list']
    max_parts = test_spec['max_parts']
    expected = test_spec['expected']

    gen = partition(list_part, max_parts)
    assert list(gen) == expected


test_spec = [
    {
        'input': [
            (
                1,
                2,
                3,
            )
        ],
        'expected': [1, 2, 3],
    },
    {
        'input': [
            (
                1,
                2,
                3,
            ),
            (4, 5, 6),
            7,
        ],
        'expected': [1, 2, 3, 4, 5, 6, 7],
    },
    {
        'input': [[[[[1]]]], [[[2]], [3, 4]], [5, 6, 7]],
        'expected': [1, 2, 3, 4, 5, 6, 7],
    },
    {
        'input': [
            (
                1,
                2,
                3,
            ),
            'some',
            ['text', ['in', [[['nested'], 'lists']]]],
        ],
        'expected': [1, 2, 3, 'some', 'text', 'in', 'nested', 'lists'],
    },
    {'input': [1, 2, 3, 4], 'expected': [1, 2, 3, 4]},
    {'input': [[[[[[], [[[], []]]]]]]], 'expected': []},
]


@pytest.mark.parametrize('test_spec', test_spec)
def test_flatten(test_spec):
    _input = test_spec['input']
    expected = test_spec['expected']

    assert list(flatten(_input)) == expected


test_spec = [
    {'input': [1, 2, 3, 4, 5, 6], 'expected': [1, 2, 3, 4, 5, 6]},
    {'input': [1, 2, 1, 2, 4, 6], 'expected': [1, 2, 4, 6]},
    {'input': set([1, 2, 3, 4]), 'expected': set([1, 2, 3, 4])},
    {'input': [], 'expected': []},
]


@pytest.mark.parametrize('test_spec', test_spec)
def test_deduplicate(test_spec):
    _input = test_spec['input']
    expected = test_spec['expected']

    _t = type(_input)
    assert _t(deduplicate(_input)) == expected
