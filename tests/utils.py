

def query_test_helper(cls, test_spec):
    results = cls().handle(test_spec['query'])

    if results is None:
        assert len(test_spec['results']) == 0
        return

    assert len(results) == len(test_spec['results'])

    for result, item in zip(results, test_spec['results']):
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
        # Although seems stupid we use this to distinguish between equalities in floats and ints
        # For example 3.0 is not equal to 3 we want the type to be correct
        assert isinstance(query_result.value,
                          item['query_result']['value_type'])
