from .calculation import Calculation
from ..query.result import QueryResult
from ..lang import Language

class PercentageCalculation(Calculation):
    def __init__(self, value=None, amounts=(), error=None, order=0):
        super().__init__(value, has_boolean=False, error=error, order=order)
        self.amounts = amounts
        self.has_boolean = any(map(lambda amount: amount.has_boolean, self.amounts))

    def is_error(self, _type=None):
        if _type is None:
            return (
                super().is_error() or
                all(map(lambda amount: amount.error is not None, self.amounts))
            )
        return (
            super().is_error(_type) or
            any(map(lambda amount: amount.error == _type, self.amounts))
        )

    def _get_extra_descriptions(self):
        translator = Language().get_translator('calculator')
    
        value_type = self.value_type
        extra_descriptions = []
        if value_type == Calculation.VALUE_COMPLEX:
            extra_descriptions.append(translator('result-complex'))
        elif value_type == Calculation.VALUE_IMAGINARY:
            extra_descriptions.append(translator('result-imaginary'))
        
        value_1_type = self.amounts[0].value_type
        value_2_type = self.amounts[1].value_type
        if value_1_type == Calculation.VALUE_COMPLEX or value_2_type == Calculation.VALUE_COMPLEX:
            extra_descriptions.append(translator('value-complex'))
        elif value_1_type == Calculation.VALUE_IMAGINARY or value_2_type == Calculation.VALUE_IMAGINARY:
            extra_descriptions.append(translator('value-imaginary'))

        if self.has_boolean:
            extra_descriptions.append(translator('query-boolean'))

        return extra_descriptions

    @Calculation.Decorators.handle_error_results
    def to_query_result(self):
        name = self.format()
        description = '{} + {:}%'.format(self.amounts[0].format(), self.amounts[1].format())
   
        extra_descriptions = self._get_extra_descriptions()
        if extra_descriptions:
            extra_descriptions = ' '.join(extra_descriptions)
            description = '{} ({})'.format(description, extra_descriptions)

        return QueryResult(
            icon='images/icon.svg',
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order
        )

class NormalPercentageCalculation(PercentageCalculation):
    @PercentageCalculation.Decorators.handle_error_results
    def to_query_result(self):
        translator = Language().get_translator('calculator')
        result_formatted = self.format()
        name = result_formatted

        amount1 = self.amounts[0]
        if amount1.value_type == Calculation.VALUE_IMAGINARY or amount1.value_type == Calculation.VALUE_COMPLEX:
            amount1 = '({})'.format(amount1.format())
        else:
            amount1 = amount1.format()

        amount2 = self.amounts[1].format()

        description = '{}% {{}} {}'.format(amount1, amount2)
        description = description.format(translator('of'))

        return QueryResult(
            icon='images/icon.svg',
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order
        )

class InversePercentageCalculation(PercentageCalculation):
    @PercentageCalculation.Decorators.handle_error_results
    def to_query_result(self):
        translator = Language().get_translator('calculator')
        result_formatted = self.format()

        if self.value_type == Calculation.VALUE_IMAGINARY or self.value_type == Calculation.VALUE_COMPLEX:
            result_formatted = '({})'.format(result_formatted)

        name = '{}%'.format(result_formatted)

        amount1 = self.amounts[0]
        if amount1.value_type == Calculation.VALUE_IMAGINARY or amount1.value_type == Calculation.VALUE_COMPLEX:
            amount1 = '({})'.format(amount1.format())
        else:
            amount1 = amount1.format()

        amount2 = self.amounts[1].format()
            
        description = '{} {{}} {}% {{}} {}'.format(amount1, result_formatted, amount2)
        description = description.format(translator('is'), translator('of'))

        return QueryResult(
            icon='images/icon.svg',
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order
        )
