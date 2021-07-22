import pytest
from calculate_anything.lang import LanguageService
from calculate_anything.query.handlers import CalculatorQueryHandler
from calculate_anything.exceptions import ZeroDivisionException

tr_calc = LanguageService().get_translator('calculator')
tr_err = LanguageService().get_translator('errors')

tests = [{
    # Normal test
    'query': '1 + 1 + 1',
    'results': [{
        'result': {
            'value': 3,
            'query': '1 + 1 + 1',
            'error': None,
            'order': 0
        },
        'query_result': {
            'icon': 'images/icon.svg',
            'name': '3',
            'description': '1 + 1 + 1',
            'clipboard': '3',
            'error': None,
            'order': 0,
            'value': 3,
            'value_type': int
        }
    }],
}, {
    # Division by zero
    'query': '(1 + 2) / (1 - 1)',
    'results': [{
        'result': {
            'query': '(1 + 2) / (1 - 1)',
            'value': None,
            'error': ZeroDivisionException,
            'order': 0
        },
        'query_result': {
            'icon': 'images/icon.svg',
            'name': tr_err('infinite-result-error'),
            'description': tr_err('infinite-result-error-description'),
            'clipboard': None,
            'error': ZeroDivisionException,
            'order': 0,
            'value': None,
            'value_type': type(None)
        }
    }],
}, {
    # Complex number
    'query': '(1 + 7 + 5i + 4i - 7i) / 2',
    'results': [{
        'result': {
            'value': 4 + 1j,
            'query': '(1 + 7 + 5j + 4j - 7j) / 2',
            'error': None,
            'order': 0
        },
        'query_result': {
            'icon': 'images/icon.svg',
            'name': '4 + i',
            'description': '(1 + 7 + 5i + 4i - 7i) / 2 ({})'.format(tr_calc('result-complex').capitalize()),
            'clipboard': '4 + i',
            'error': None,
            'order': 0,
            'value': 4 + 1j,
            'value_type': complex
        }
    }],
}, {
    # Test result with complex numbers that is real and not of type complex
    'query': 'e ^ (pi * i)',
    'results': [{
        'result': {
            'value': -1 + 0j,
            'query': 'e ** (pi * 1j)',
            'error': None,
            'order': 0
        },
        'query_result': {
            'icon': 'images/icon.svg',
            'name': '-1',
            'description': 'e ^ (π × i)',
            'clipboard': '-1',
            'error': None,
            'order': 0,
            'value': -1,
            'value_type': int
        }
    }],
}, {
    # Test boolean result
    'query': 'e ^ (pi * i) + 1 = 0',
    'results': [{
        'result': {
            'value': True,
            'query': 'e ** (pi * 1j) + 1 == 0',
            'error': None,
            'order': 0
        },
        'query_result': {
            'icon': 'images/icon.svg',
            'name': 'true',
            'description': 'e ^ (π × i) + 1 = 0 ({})'.format(tr_calc('result-boolean').capitalize()),
            'clipboard': 'true',
            'error': None,
            'order': 0,
            'value': True,
            'value_type': bool
        }
    }],
}]


@pytest.mark.parametrize('test', tests)
def test_calculator(test):
    results = CalculatorQueryHandler().handle_raw(test['query'])

    assert len(results) == len(test['results'])

    for result, item in zip(results, test['results']):
        assert result.value == item['result']['value']
        assert result.query == item['result']['query']
        assert result.error == item['result']['error']
        assert result.order == item['result']['order']

        query_result = result.to_query_result()
        assert query_result.icon == item['query_result']['icon']
        assert query_result.name == item['query_result']['name']
        assert query_result.description == item['query_result']['description']
        assert query_result.clipboard == item['query_result']['clipboard']
        assert query_result.error == item['query_result']['error']
        assert query_result.order == item['query_result']['order']
        assert query_result.value == item['query_result']['value']
        assert isinstance(query_result.value,
                          item['query_result']['value_type'])
