import pytest
from calculate_anything.lang import LanguageService
from calculate_anything.utils import StupidEval
from calculate_anything.query.handlers import MultiHandler
from calculate_anything.query.handlers import CalculatorQueryHandler
from calculate_anything.utils import images_dir
from calculate_anything.exceptions import (
    BooleanComparisonException,
    MissingSimpleevalException,
    ZeroDivisionException,
)
from test.tutils import (
    calculator_no_simpleeval,
    reset_instance,
    query_test_helper,
)

LanguageService().set('en_US')
tr_calc = LanguageService().get_translator('calculator')
tr_err = LanguageService().get_translator('errors')

test_spec_calculator = [
    {
        # Normal test
        'query': '= 1 + 1 + 1',
        'results': [
            {
                'result': {
                    'value': 3,
                    'query': '1 + 1 + 1',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
                    'name': '3',
                    'description': '1 + 1 + 1',
                    'clipboard': '3',
                    'error': None,
                    'order': 0,
                    'value': 3,
                    'value_type': int,
                },
            }
        ],
    },
    {
        # Division by zero
        'query': '= (1 + 2) / (1 - 1)',
        'results': [
            {
                'result': {
                    'query': '(1 + 2) / (1 - 1)',
                    'value': None,
                    'error': ZeroDivisionException,
                    'order': ZeroDivisionException.order,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
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
        # Complex number
        'query': '= (1 + 7 + 5i + 4i - 7i) / 2',
        'results': [
            {
                'result': {
                    'value': 4 + 1j,
                    'query': '(1 + 7 + 5j + 4j - 7j) / 2',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
                    'name': '4 + i',
                    'description': '(1 + 7 + 5i + 4i - 7i) / 2 ({})'.format(
                        tr_calc('result-complex').capitalize()
                    ),
                    'clipboard': '4 + i',
                    'error': None,
                    'order': 0,
                    'value': 4 + 1j,
                    'value_type': complex,
                },
            }
        ],
    },
    {
        # Complex number with reversed i
        'query': '= (1 + 7 + i2 + i5 - i11) / 2',
        'results': [
            {
                'result': {
                    'value': 4 - 2j,
                    'query': '(1 + 7 + 2j + 5j - 11j) / 2',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
                    'name': '4 - 2i',
                    'description': '(1 + 7 + 2i + 5i - 11i) / 2 ({})'.format(
                        tr_calc('result-complex').capitalize()
                    ),
                    'clipboard': '4 - 2i',
                    'error': None,
                    'order': 0,
                    'value': 4 - 2j,
                    'value_type': complex,
                },
            }
        ],
    },
    {
        # Test result with complex numbers that is real and not of type complex
        'query': '= e ^ (pi * i)',
        'results': [
            {
                'result': {
                    'value': -1 + 0j,
                    'query': 'e ** (pi * 1j)',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
                    'name': '-1',
                    'description': 'e ^ (π × i)',
                    'clipboard': '-1',
                    'error': None,
                    'order': 0,
                    'value': -1,
                    'value_type': int,
                },
            }
        ],
    },
    {
        # Test inequality with comples number producing error
        'query': '= 1 + i > 0.5 + 2i',
        'results': [
            {
                'result': {
                    'value': None,
                    'query': '1 + 1j > 0.5 + 2j',
                    'error': BooleanComparisonException,
                    'order': BooleanComparisonException.order,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
                    'name': tr_err('boolean-comparison-error'),
                    'description': tr_err(
                        'boolean-comparison-error-description'
                    ),
                    'clipboard': '',
                    'error': BooleanComparisonException,
                    'order': BooleanComparisonException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
    {
        # Test boolean result
        'query': '= e ^ (pi * i) + 1 = 0',
        'results': [
            {
                'result': {
                    'value': True,
                    'query': 'e ** (pi * 1j) + 1 == 0',
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
                    'name': 'true',
                    'description': 'e ^ (π × i) + 1 = 0 ({})'.format(
                        tr_calc('result-boolean').capitalize()
                    ),
                    'clipboard': 'true',
                    'error': None,
                    'order': 0,
                    'value': True,
                    'value_type': bool,
                },
            }
        ],
    },
    {
        # Test rejects 1
        'query': '= 1 % of 2',
        'results': [],
    },
    {
        # Test rejects 2
        'query': '= 1 == 2',
        'results': [],
    },
    {
        # Test rejects 3
        'query': '= 2.5 is 2.5',
        'results': [],
    },
    {
        # Test rejects 4
        'query': '= 5 // 2',
        'results': [],
    },
    {
        # Test wrong query
        'query': '= Some irrelevant query',
        'results': [],
    },
    {
        # Test missing value between equalities 1
        'query': '= 1 =  < 2',
        'results': [],
    },
    {
        # Test missing value between equalities 2
        'query': '= 5.4 >  = 4',
        'results': [],
    },
    {
        # Test missing value between equalities 3
        'query': '= 1 >=  = 5.67',
        'results': [],
    },
    {
        # Test missing value between equalities 4
        'query': '= pi <=  <= 8',
        'results': [],
    },
    {
        # Test other cases
        'query': '= 1 2 7.57',
        'results': [],
    },
    {
        # Test j not as imaginary
        'query': '= 8 + j + 4.5 - sqrt(5j)',
        'results': [],
    },
    {
        # Test i alone after number with spaces
        'query': '= 5 i',
        'results': [],
    },
    {
        # Test FunctionNotDefined
        'query': '= print(12)',
        'results': [],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_calculator)
def test_calculator(test_spec):
    query_test_helper(CalculatorQueryHandler, test_spec)
    # query_test_helper(MultiHandler, test_spec, raw=True)
    # query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_missing_simpleeval = [
    {
        'query': '= 1245',
        'results': [
            {
                'result': {
                    'query': '1245',
                    'value': 1245,
                    'error': None,
                    'order': 0,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
                    'name': '1245',
                    'description': '1245',
                    'clipboard': '1245',
                    'error': None,
                    'order': 0,
                    'value': 1245,
                    'value_type': int,
                },
            }
        ],
    },
    {
        'query': '= 1245 + sqrt(2)',
        'results': [
            {
                'result': {
                    'query': '1245 + sqrt(2)',
                    'value': None,
                    'error': MissingSimpleevalException,
                    'order': MissingSimpleevalException.order,
                },
                'query_result': {
                    'icon': images_dir('icon.svg'),
                    'name': tr_err('missing-simpleeval-error'),
                    'description': tr_err(
                        'missing-simpleeval-error-description'
                    ),
                    'clipboard': '/usr/bin/python3 -m pip install simpleeval',
                    'error': MissingSimpleevalException,
                    'order': MissingSimpleevalException.order,
                    'value': None,
                    'value_type': type(None),
                },
            }
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_missing_simpleeval)
def test_missing_simpleeval(test_spec):
    # Allow CalculatorQueryHandler to be reinstantiated

    with calculator_no_simpleeval(), reset_instance(CalculatorQueryHandler):
        # Set stupid StupidEval as SimpleEval
        assert isinstance(CalculatorQueryHandler()._simple_eval, StupidEval)
        query_test_helper(CalculatorQueryHandler, test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)
