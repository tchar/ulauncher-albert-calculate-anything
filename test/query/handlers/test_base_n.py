import pytest
from calculate_anything.lang import LanguageService
from calculate_anything.query.handlers import MultiHandler
from calculate_anything.query.handlers import (
    Base10QueryHandler,
    Base16QueryHandler,
    Base2QueryHandler,
    Base8QueryHandler,
)
from calculate_anything.utils import images_dir
from calculate_anything.exceptions import (
    BaseFloatingPointException,
    MissingSimpleevalException,
    WrongBaseException,
    ZeroDivisionException,
)
from test.tutils import base_n_no_simpleeval, query_test_helper, reset_instance


LanguageService().set('en_US')
tr_calc = LanguageService().get_translator('calculator')
tr_err = LanguageService().get_translator('errors')


def result_for_base_n(base, value, query, order):
    if base == 10:
        name = str(value)
        description = 'DEC'
    elif base == 16:
        name = hex(value)[2:]
        description = 'HEX'
    elif base == 2:
        name = bin(value)[2:]
        description = 'BIN'
    elif base == 8:
        name = oct(value)[2:]
        description = 'OCT'

    return {
        'result': {
            'value': value,
            'query': query,
            'error': None,
            'order': order,
        },
        'query_result': {
            'icon': images_dir('icon.svg'),
            'name': name,
            'description': description,
            'clipboard': name,
            'error': None,
            'order': order,
            'value': value,
            'value_type': int,
        },
    }


def result_for_base16_string(value, query, order):
    return {
        'result': {
            'value': value,
            'query': query,
            'error': None,
            'order': order,
        },
        'query_result': {
            'icon': images_dir('icon.svg'),
            'name': value,
            'description': 'BYTES',
            'clipboard': value,
            'error': None,
            'order': order,
            'value': value,
            'value_type': str,
        },
    }


def result_for_colors(value, query, order, color):
    if color == 'RGB':
        name = '{}, {}, {}'.format(*value)
    elif color == 'HSV':
        name = '{:.0f}, {:.0%}, {:.0%}'.format(*value)
    elif color == 'HSL':
        name = '{:.0f}, {:.0%}, {:.0%}'.format(*value)
    elif color == 'CMYK':
        name = '{:.0%}, {:.0%}, {:.0%}, {:.0%}'.format(*value)
    return {
        'result': {
            'value': pytest.approx(value, rel=0.001),
            'query': query,
            'error': None,
            'order': order,
        },
        'query_result': {
            'icon': images_dir('color.svg'),
            'name': name,
            'description': color,
            'clipboard': name,
            'error': None,
            'order': order,
            'value': pytest.approx(value, rel=0.001),
            'value_type': tuple,
        },
    }


def result_for_zero_division_exc(query):
    return {
        'result': {
            'query': query,
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


def result_for_wrong_base_exc(query):
    return {
        'result': {
            'query': query,
            'value': None,
            'error': WrongBaseException,
            'order': WrongBaseException.order,
        },
        'query_result': {
            'icon': images_dir('icon.svg'),
            'name': tr_err('wrong-base-error'),
            'description': tr_err('wrong-base-error-description'),
            'clipboard': '',
            'error': WrongBaseException,
            'order': WrongBaseException.order,
            'value': None,
            'value_type': type(None),
        },
    }


def result_for_base_floating_point_exc(query):
    return {
        'result': {
            'query': query,
            'value': None,
            'error': BaseFloatingPointException,
            'order': BaseFloatingPointException.order,
        },
        'query_result': {
            'icon': images_dir('icon.svg'),
            'name': tr_err('base-floating-error'),
            'description': tr_err('base-floating-error-description'),
            'clipboard': '',
            'error': BaseFloatingPointException,
            'order': BaseFloatingPointException.order,
            'value': None,
            'value_type': type(None),
        },
    }


def missing_simpleeval_result(query):
    return {
        'result': {
            'query': query,
            'value': None,
            'error': MissingSimpleevalException,
            'order': MissingSimpleevalException.order,
        },
        'query_result': {
            'icon': images_dir('icon.svg'),
            'name': tr_err('missing-simpleeval-error'),
            'description': tr_err('missing-simpleeval-error-description'),
            'clipboard': '/usr/bin/python3 -m pip install simpleeval',
            'error': MissingSimpleevalException,
            'order': MissingSimpleevalException.order,
            'value': None,
            'value_type': type(None),
        },
    }


test_spec_base10 = [
    {
        # Simple test
        'query': 'dec 10',
        'results': [
            result_for_base_n(16, 10, '10', 0),
            result_for_base_n(2, 10, '10', 1),
            result_for_base_n(8, 10, '10', 2),
        ],
    },
    {
        # More complex test
        'query': 'dec (11 * 11) mod 2 + 10 div 2 + '
        '8 xor 11 + 9 and 1 + (15 or 16)',
        'results': [
            result_for_base_n(
                10,
                14,
                '(11 * 11) mod 2 + 10 div 2 + '
                '8 xor 11 + 9 and 1 + (15 or 16)',
                0,
            ),
            result_for_base_n(
                16,
                14,
                '(11 * 11) mod 2 + 10 div 2 + '
                '8 xor 11 + 9 and 1 + (15 or 16)',
                1,
            ),
            result_for_base_n(
                2,
                14,
                '(11 * 11) mod 2 + 10 div 2 + '
                '8 xor 11 + 9 and 1 + (15 or 16)',
                2,
            ),
            result_for_base_n(
                8,
                14,
                '(11 * 11) mod 2 + 10 div 2 + '
                '8 xor 11 + 9 and 1 + (15 or 16)',
                3,
            ),
        ],
    },
    {
        # Division by zero
        'query': 'dec (1 + 2) mod (1 - 1)',
        'results': [result_for_zero_division_exc('(1 + 2) mod (1 - 1)')],
    },
    {
        # Wrong base
        'query': 'dec affe',
        'results': [result_for_wrong_base_exc('affe')],
    },
    {
        # Floating point
        'query': 'dec 10.5',
        'results': [result_for_base_floating_point_exc('10.5')],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_base10)
def test_base10(test_spec):
    query_test_helper(Base10QueryHandler, test_spec)
    query_test_helper(MultiHandler, test_spec, raw=True)
    query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_base16 = [
    {
        # Simple test
        'query': 'hex 10',
        'results': [
            result_for_base_n(10, 16, '10', 0),
            result_for_base_n(2, 16, '10', 1),
            result_for_base_n(8, 16, '10', 2),
            result_for_base16_string('20:31:30', '10', 3),
        ],
    },
    {
        # More complex test
        'query': 'hex (ffab * 10) mod ffa + 10 div f + '
        '8 xor 2 + 3fad * ff + (15 or ff)',
        'results': [
            result_for_base_n(
                16,
                4157165,
                '(ffab * 10) mod ffa + 10 div f + '
                '8 xor 2 + 3fad * ff + (15 or ff)',
                0,
            ),
            result_for_base_n(
                10,
                4157165,
                '(ffab * 10) mod ffa + 10 div f + '
                '8 xor 2 + 3fad * ff + (15 or ff)',
                1,
            ),
            result_for_base_n(
                2,
                4157165,
                '(ffab * 10) mod ffa + 10 div f + '
                '8 xor 2 + 3fad * ff + (15 or ff)',
                2,
            ),
            result_for_base_n(
                8,
                4157165,
                '(ffab * 10) mod ffa + 10 div f + '
                '8 xor 2 + 3fad * ff + (15 or ff)',
                3,
            ),
            result_for_base16_string(
                '20:28:66:66:61:62:20:2a:20:31:30:29:20:6d:6f:64:20:66:66:61:'
                '20:2b:20:31:30:20:64:69:76:20:66:20:2b:20:38:20:78:6f:72:20:'
                '32:20:2b:20:33:66:61:64:20:2a:20:66:66:20:2b:20:28:31:35:20:'
                '6f:72:20:66:66:29',
                '(ffab * 10) mod ffa + 10 div f + '
                '8 xor 2 + 3fad * ff + (15 or ff)',
                4,
            ),
        ],
    },
    {
        # Test colors (color utils have been tested in tests/test_utils)
        'query': 'hex #ffabf1',
        'results': [
            result_for_colors((255, 171, 241), '#ffabf1', 0, 'RGB'),
            result_for_colors((310.0, 0.3294, 1.0), '#ffabf1', 1, 'HSV'),
            result_for_colors((310.0, 0.9999, 0.8353), '#ffabf1', 2, 'HSL'),
            result_for_colors((0.0, 0.3294, 0.0549, 0.0), '#ffabf1', 3, 'CMYK'),
            result_for_base16_string('20:23:66:66:61:62:66:31', '#ffabf1', 4),
        ],
    },
    {
        # Division by zero
        'query': 'hex (1 + 2) mod (1 - 1)',
        'results': [
            result_for_zero_division_exc('(1 + 2) mod (1 - 1)'),
            result_for_base16_string(
                '20:28:31:20:2b:20:32:29:20:6d:6f:64:20:28:31:20:2d:20:31:29',
                '(1 + 2) mod (1 - 1)',
                0,
            ),
        ],
    },
    {
        # Wrong base
        'query': 'hex gglady',
        'results': [
            result_for_wrong_base_exc('gglady'),
            result_for_base16_string('20:67:67:6c:61:64:79', 'gglady', 0),
        ],
    },
    {
        # Floating point
        'query': 'hex ff.5',
        'results': [
            result_for_base_floating_point_exc('ff.5'),
            result_for_base16_string('20:66:66:2e:35', 'ff.5', 0),
        ],
    },
]


@pytest.mark.parametrize('test_spec', test_spec_base16)
def test_base16(test_spec):
    query_test_helper(Base16QueryHandler, test_spec)
    query_test_helper(MultiHandler, test_spec, raw=True)
    query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)


test_spec_missing_simpleeval = [
    {
        'query': 'hex aff mod 2',
        'results': [
            missing_simpleeval_result('aff mod 2'),
            result_for_base16_string(
                '20:61:66:66:20:6d:6f:64:20:32', 'aff mod 2', 0
            ),
        ],
        'class': Base16QueryHandler,
    },
    {
        'query': 'dec 10 mod 2',
        'results': [missing_simpleeval_result('10 mod 2')],
        'class': Base10QueryHandler,
    },
    {
        'query': 'bin 10 mod 1',
        'results': [missing_simpleeval_result('10 mod 1')],
        'class': Base2QueryHandler,
    },
    {
        'query': 'oct 10 mod 7',
        'results': [missing_simpleeval_result('10 mod 7')],
        'class': Base8QueryHandler,
    },
]


@pytest.mark.parametrize('test_spec', test_spec_missing_simpleeval)
def test_missing_simpleeval(test_spec):
    with base_n_no_simpleeval(), reset_instance(test_spec['class']):
        query_test_helper(test_spec['class'], test_spec)
        query_test_helper(MultiHandler, test_spec, raw=True)
        query_test_helper(MultiHandler, test_spec, raw=False, only_qr=True)
