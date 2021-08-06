import pytest
from calculate_anything.query.handlers.base import QueryHandler


class MockQueryHandler(QueryHandler):
    def __init__(self, kw):
        super().__init__(kw)

    def handle_raw(self, query):
        if query.strip() != '':
            return ['Just a result']
        return []

    @QueryHandler.Decorators.can_handle
    def handle(self, query):
        return self.handle_raw(query)


test_spec_main = [
    {
        'kw': '=',
        'query': '= Some query',
        'query_nokw': ' Some query',
        'results': ['Just a result'],
    },
    {'kw': '=', 'query': '=', 'query_nokw': '', 'results': []},
    {'kw': 'base', 'query': '=', 'query_nokw': '', 'results': None},
]


@pytest.mark.parametrize('test_spec', test_spec_main)
def test_main(test_spec):
    mock = MockQueryHandler(test_spec['kw'])
    assert mock.handle(test_spec['query']) == test_spec['results']
    assert (
        mock.query_without_keyword(test_spec['query'], check=True)
        == test_spec['query_nokw']
    )
