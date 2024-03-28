import pytest
from test.tutils import query_test_helper
from calculate_anything.query.handlers import MultiHandler
from calculate_anything.query.handlers import PercentagesQueryHandler
from calculate_anything.lang import LanguageService
from calculate_anything.utils import images_dir
from calculate_anything.exceptions import (
    BooleanPercetageException,
    ZeroDivisionException,
)


LanguageService().set('en_US')
tr_calc = LanguageService().get_translator('calculator')
tr_err = LanguageService().get_translator('errors')


# Test Normal
test_spec_normal = [
    {
        # Normal test
        'query': '= 10% of 10',
        'results': [
            {
                'result': {
                    'value': 1,
                    'query': '(10)% of (10)',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': '1',
                    'description': '10% of 10',
                    'clipboard': '1',
                    'error': None,
                    'order': 0,
                    'value': 1,
                    'value_type': int,
                },
            }
        ],
    },
    {
        # Complex test
        'query': '= sqrt(1) + 2 + 5i + 125% of 3.5',
        'results': [
            {
                'result': {
                    'value': pytest.approx(4.48 + 0.175j),
                    'query': '(sqrt(1) + 2 + 5j + 125)% of (3.5)',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': '4.48 + 0.175i',
                    'description': '(128 + 5i)% of 3.5 ({})'.format(
                        tr_calc('result-complex').capitalize()
                    ),
                    'clipboard': '4.48 + 0.175i',
                    'error': None,
                    'order': 0,
                    'value': pytest.approx(4.48 + 0.175j),
                    'value_type': complex,
                },
            }
        ],
    },
    {
        # Division by zero
        'query': '= 1231 / (1-1) % of 2.477',
        'results': [
            {
                'result': {
                    'query': '1231 / (1-1) % of 2.477',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('zero-division-error'),
                    'description': tr_err('zero-division-error-description'),
                    'clipboard': '',
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Boolean result
        'query': '= 10 = 10% of 2',
        'results': [
            {
                'result': {
                    'query': '10 = 10% of 2',
                    'value': None,
                    'error': BooleanPercetageException,
                    'order': BooleanPercetageException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('boolean-percentage-error'),
                    'description': tr_err(
                        'boolean-percentage-error-description'
                    ),
                    'clipboard': '',
                    'error': BooleanPercetageException,
                    'order': BooleanPercetageException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Leftmost error
        'query': '= 1=0 % of 0',
        'results': [
            {
                'result': {
                    'query': '1=0 % of 0',
                    'value': None,
                    'error': BooleanPercetageException,
                    'order': BooleanPercetageException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('boolean-percentage-error'),
                    'description': tr_err(
                        'boolean-percentage-error-description'
                    ),
                    'clipboard': '',
                    'error': BooleanPercetageException,
                    'order': BooleanPercetageException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Amount uncalculateable
        'query': '= Some amount% of 4.7777',
        'results': [],
    },
    {
        # Percentage uncalculateable
        'query': '= 2.255% of Some amount',
        'results': [],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_normal)
def test_normal(test_spec):
    query_test_helper(PercentagesQueryHandler, test_spec)
    query_test_helper(MultiHandler, test_spec, raw=True)
    query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


# Test Inverse
test_spec_inverse = [
    {
        # Normal test
        'query': '= 10 as % of 200',
        'results': [
            {
                'result': {
                    'value': 5,
                    'query': '(10) as % of (200)',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': '5%',
                    'description': '(10) is 5% of (200)',
                    'clipboard': '5%',
                    'error': None,
                    'order': 0,
                    'value': 5,
                    'value_type': int,
                },
            }
        ],
    },
    {
        # More complex
        'query': '= 10i + sqrt(2) as % of tan(pi) + e ^ pi * i',
        'results': [
            {
                'result': {
                    'value': pytest.approx(
                        43.21391826377226 - 6.111370929190913j
                    ),
                    'query': '(10j + sqrt(2)) as % of '
                    '(tan(pi) + e ** pi * 1j)',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': '(43.2139 - 6.11137i)%',
                    'description': '(1.41421 + 10i) is '
                    '(43.2139 - 6.11137i)% of (23.1407i) ({})'.format(
                        tr_calc('result-complex').capitalize()
                    ),
                    'clipboard': '(43.2139 - 6.11137i)%',
                    'error': None,
                    'order': 0,
                    'value': pytest.approx(
                        43.21391826377226 - 6.111370929190913j
                    ),
                    'value_type': complex,
                },
            }
        ],
    },
    {
        # Division by zero
        'query': '= 1 /0 as % of  10',
        'results': [
            {
                'result': {
                    'query': '1 /0 as % of  10',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('zero-division-error'),
                    'description': tr_err('zero-division-error-description'),
                    'clipboard': '',
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Boolean leftmost as %
        'query': '= 1 =1 as % of  2',
        'results': [
            {
                'result': {
                    'query': '1 =1 as % of  2',
                    'value': None,
                    'error': BooleanPercetageException,
                    'order': BooleanPercetageException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('boolean-percentage-error'),
                    'description': tr_err(
                        'boolean-percentage-error-description'
                    ),
                    'clipboard': '',
                    'error': BooleanPercetageException,
                    'order': BooleanPercetageException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Two errors, leftmost prevails
        'query': '= 1 / 0 as % of  1 = 1',
        'results': [
            {
                'result': {
                    'query': '1 / 0 as % of  1 = 1',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('zero-division-error'),
                    'description': tr_err('zero-division-error-description'),
                    'clipboard': '',
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Percentage of 0
        'query': '= 2.25 as % of 0',
        'results': [
            {
                'result': {
                    'query': '2.25 as % of 0',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('zero-division-error'),
                    'description': tr_err('zero-division-error-description'),
                    'clipboard': '',
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Percentage of right expression wrong
        'query': '= 2.25 as % of something',
        'results': [],
    },
    {
        # Percentage of Left expression wrong
        'query': '= something as % of 125.5',
        'results': [],
    },
    {
        # Not matching query
        'query': '= 2.25 % 2',
        'results': [],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_inverse)
def test_inverse(test_spec):
    query_test_helper(PercentagesQueryHandler, test_spec)


# Test Calc
test_spec_calc = [
    {
        # Normal test
        'query': '= 10 + 10%',
        'results': [
            {
                'result': {
                    'value': 11,
                    'query': '(10) + (10)%',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': '11',
                    'description': '(10) + (10)%',
                    'clipboard': '11',
                    'error': None,
                    'order': 0,
                    'value': 11,
                    'value_type': int,
                },
            }
        ],
    },
    {
        # Complex test
        'query': '= sqrt(1) + 2 + 5i + 125 + 5i + 3.5% ',
        'results': [
            {
                'result': {
                    'value': pytest.approx(132.48 + 10.35j),
                    'query': '(sqrt(1) + 2 + 5j + 125 + 5j) + (3.5)%',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': '132.48 + 10.35i',
                    'description': '(128 + 10i) + (3.5)% ({})'.format(
                        tr_calc('result-complex').capitalize()
                    ),
                    'clipboard': '132.48 + 10.35i',
                    'error': None,
                    'order': 0,
                    'value': pytest.approx(132.48 + 10.35j),
                    'value_type': complex,
                },
            }
        ],
    },
    {
        # Imaginary test
        'query': '= 5i + sqrt(2)%',
        'results': [
            {
                'result': {
                    'value': pytest.approx(5.07071j),
                    'query': '(5j) + (sqrt(2))%',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': '5.07071i',
                    'description': '(5i) + (1.41421)% ({})'.format(
                        tr_calc('result-imaginary').capitalize()
                    ),
                    'clipboard': '5.07071i',
                    'error': None,
                    'order': 0,
                    'value': pytest.approx(5.07071j),
                    'value_type': complex,
                },
            }
        ],
    },
    {
        # Division by zero
        'query': '= 10 + 0.5/0 + 2%',
        'results': [
            {
                'result': {
                    'query': '10 + 0.5/0 + 2%',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('zero-division-error'),
                    'description': tr_err('zero-division-error-description'),
                    'clipboard': '',
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Boolean result
        'query': '= 10 = 10 + 2%',
        'results': [
            {
                'result': {
                    'query': '10 = 10 + 2%',
                    'value': None,
                    'error': BooleanPercetageException,
                    'order': BooleanPercetageException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('boolean-percentage-error'),
                    'description': tr_err(
                        'boolean-percentage-error-description'
                    ),
                    'clipboard': '',
                    'error': BooleanPercetageException,
                    'order': BooleanPercetageException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Leftmost error
        'query': '= 1/0 + 2=2%',
        'results': [
            {
                'result': {
                    'query': '1/0 + 2=2%',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('zero-division-error'),
                    'description': tr_err('zero-division-error-description'),
                    'clipboard': '',
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Rightmost error
        'query': '= 1 + 2/0%',
        'results': [
            {
                'result': {
                    'query': '1 + 2/0%',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('percent.svg'),
                    'name': tr_err('zero-division-error'),
                    'description': tr_err('zero-division-error-description'),
                    'clipboard': '',
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Amount uncalculateable
        'query': '= Some amount + 40%',
        'results': [],
    },
    {
        # Percentage uncalculateable
        'query': '= 2.255 + Some amount%',
        'results': [],
    },
    {
        # Amount empty
        'query': '= 100 + %',
        'results': [],
    },
    {
        # No 2 amounts 1
        'query': '= 100%',
        'results': [],
    },
    {
        # No 2 amounts 2
        'query': '= + 100%',
        'results': [],
    },
    {
        # Unmatched paren (for custom parsing)
        'query': '= 100 + ((100)%',
        'results': [],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_calc)
def test_calc(test_spec):
    query_test_helper(PercentagesQueryHandler, test_spec)
    query_test_helper(MultiHandler, test_spec, raw=True)
    query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


def test_complete_cov():
    PercentagesQueryHandler().handle('= 12 + 12')
