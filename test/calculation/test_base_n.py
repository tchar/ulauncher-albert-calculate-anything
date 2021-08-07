# TODO: For all calculations
# For now they are tested indirectly through the relevant QueryHandler

from calculate_anything.calculation import BaseNCalculation


def test_cov():
    calculation = BaseNCalculation('some value', 'some_query', order=1)
    assert calculation.format() == 'some value'
    assert calculation.get_description() == ''
    assert calculation.query == 'some_query'

    query_result = calculation.to_query_result()
    assert query_result.name == 'some value'
    assert query_result.description == ''
    assert query_result.order == 1
    assert query_result.error is None
