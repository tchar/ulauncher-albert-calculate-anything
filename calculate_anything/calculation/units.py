from .base import _Calculation
from ..query.result import QueryResult
from ..lang import Language

class UnitsCalculation(_Calculation):
    def __init__(self, value=None, error=None, order=0,
                rate=None, unit_from_name=None, unit_to_name=None):
        super().__init__(value=value, error=error, order=order)
        self.rate = rate
        self.unit_from_name = unit_from_name
        self.unit_to_name = unit_to_name

    @_Calculation.Decorators.handle_error_results
    def to_query_result(self):
        translator = Language().get_translator('units')

        is_temperature_from = 'degree_' in self.unit_from_name
        is_temperature_to = 'degree_' in self.unit_to_name
        is_temperature = is_temperature_from or is_temperature_to

        unit_from_name = translator(self.unit_from_name).replace('**', '^').replace('_', ' ')
        unit_to_name = translator(self.unit_to_name).replace('**', '^').replace('_', ' ')

        if self.rate is None or unit_from_name == unit_to_name or is_temperature:
            description = ''
        else:
            description = '1 {} = {:g} {}'.format(unit_from_name, self.rate, unit_to_name)
        
        name = '{:g} {}'.format(self.value, unit_to_name)

        return QueryResult(
            icon='images/convert.svg',
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )