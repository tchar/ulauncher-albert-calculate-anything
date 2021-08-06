import pytest
from functools import lru_cache
from calculate_anything.time.json_cache import TimezoneJsonCache


@lru_cache(maxsize=None)
def get_cache():
    cache = TimezoneJsonCache()
    cache.load()
    return cache


test_spec_no_search_terms = [
    {
        'input': ('Athens',),
        'expected': [
            {
                'name': 'Athens',
                'cc': 'gr',
                'country': 'Greece',
                'timezone': 'Europe/Athens',
                'state': 'esye31',
            },
            {
                'name': 'Athens',
                'cc': 'us',
                'country': 'United States',
                'timezone': 'America/New_York',
                'state': 'ga',
            },
            {
                'name': 'Athens',
                'cc': 'us',
                'country': 'United States',
                'timezone': 'America/Chicago',
                'state': 'al',
            },
        ],
    },
    {
        'input': ('Tehran',),
        'expected': [
            {
                'name': 'Tehran',
                'cc': 'ir',
                'country': 'Iran, Islamic Republic of',
                'timezone': 'Asia/Tehran',
                'state': '26',
            },
        ],
    },
    {'input': ('Somecitythatdoesnotexist',), 'expected': []},
]


@pytest.mark.parametrize('test_spec', test_spec_no_search_terms)
def test_no_search_terms(test_spec):
    cache = get_cache()

    cities = cache.get(*test_spec['input'])
    cities = [{k: v for k, v in city.items() if k != 'id'} for city in cities]
    expected = test_spec['expected']

    assert cities == expected


test_spec_search_terms = [
    {
        'input': ('Athens', 'GR'),
        'expected': [
            {
                'name': 'Athens',
                'cc': 'gr',
                'country': 'Greece',
                'timezone': 'Europe/Athens',
                'state': 'esye31',
            },
        ],
    },
    {
        'input': ('Athens', 'GA'),
        'expected': [
            {
                'name': 'Athens',
                'cc': 'us',
                'country': 'United States',
                'timezone': 'America/New_York',
                'state': 'ga',
            },
        ],
    },
    {
        'input': ('Madrid', 'Spain'),
        'expected': [
            {
                'name': 'Madrid',
                'cc': 'es',
                'country': 'Spain',
                'timezone': 'Europe/Madrid',
                'state': '29',
            },
        ],
    },
    {
        'input': ('Berlin', 'Europe/Berlin'),
        'expected': [
            {
                'name': 'Berlin',
                'cc': 'de',
                'country': 'Germany',
                'timezone': 'Europe/Berlin',
                'state': '16',
            },
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_search_terms)
def test_search_terms(test_spec):
    cache = get_cache()
    cities = cache.get(*test_spec['input'])

    cities = [{k: v for k, v in city.items() if k != 'id'} for city in cities]
    expected = test_spec['expected']

    assert cities == expected
