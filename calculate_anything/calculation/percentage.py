from typing import List, Tuple, Union
from calculate_anything.exceptions import ExtendedException
from calculate_anything.calculation.base import CalculationError
from calculate_anything.calculation import CalculatorCalculation
from calculate_anything.query.result import QueryResult
from calculate_anything.lang import LanguageService
from calculate_anything.utils import images_dir


__all__ = [
    'PercentageCalculation',
    'NormalPercentageCalculation',
    'InversePercentageCalculation',
]


class PercentageCalculationError(CalculationError):
    def __init__(
        self, error: ExtendedException, query: str, amounts=()
    ) -> None:
        super().__init__(error, query)
        self.amounts = amounts


class PercentageCalculation(CalculatorCalculation):
    def __init__(
        self,
        value: Union[float, int, complex, bool],
        query: str,
        amounts: Tuple[CalculatorCalculation, CalculatorCalculation] = (),
        order: int = 0,
    ):
        super().__init__(value, query=query, order=order)
        self.amounts = amounts

    def _get_extra_descriptions(self) -> List[str]:
        translator = LanguageService().get_translator('calculator')

        value_type = self.value_type
        extra_descriptions = []
        if value_type == CalculatorCalculation.ValueType.COMPLEX:
            extra_descriptions.append(translator('result-complex').capitalize())
        elif value_type == CalculatorCalculation.ValueType.IMAGINARY:
            extra_descriptions.append(
                translator('result-imaginary').capitalize()
            )

        return extra_descriptions

    def to_query_result(self) -> QueryResult:
        name = self.format()
        description = '({}) + ({:})%'.format(
            self.amounts[0].format(), self.amounts[1].format()
        )

        extra_descriptions = self._get_extra_descriptions()
        if extra_descriptions:
            extra_descriptions = ', '.join(extra_descriptions)
            description = '{} ({})'.format(description, extra_descriptions)

        return QueryResult(
            icon=images_dir('percent.svg'),
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )


class NormalPercentageCalculation(PercentageCalculation):
    def to_query_result(self) -> QueryResult:
        translator = LanguageService().get_translator('calculator')
        result_formatted = self.format()
        name = result_formatted

        amount1 = self.amounts[0]
        if (
            amount1.value_type == CalculatorCalculation.ValueType.IMAGINARY
            or amount1.value_type == CalculatorCalculation.ValueType.COMPLEX
        ):
            amount1 = '({})'.format(amount1.format())
        else:
            amount1 = amount1.format()

        amount2 = self.amounts[1].format()

        description = '{}% {{}} {}'.format(amount1, amount2)
        description = description.format(translator('of'))

        extra_descriptions = self._get_extra_descriptions()
        if extra_descriptions:
            extra_descriptions = ', '.join(extra_descriptions)
            description = '{} ({})'.format(description, extra_descriptions)

        return QueryResult(
            icon=images_dir('percent.svg'),
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )


class InversePercentageCalculation(PercentageCalculation):
    def to_query_result(self) -> QueryResult:
        translator = LanguageService().get_translator('calculator')
        result_formatted = self.format()

        if (
            self.value_type == CalculatorCalculation.ValueType.IMAGINARY
            or self.value_type == CalculatorCalculation.ValueType.COMPLEX
        ):
            result_formatted = '({})'.format(result_formatted)

        name = '{}%'.format(result_formatted)

        amount1 = self.amounts[0].format()
        amount2 = self.amounts[1].format()

        description = '({}) {{}} {}% {{}} ({})'.format(
            amount1, result_formatted, amount2
        )
        description = description.format(translator('is'), translator('of'))

        extra_descriptions = self._get_extra_descriptions()
        if extra_descriptions:
            extra_descriptions = ', '.join(extra_descriptions)
            description = '{} ({})'.format(description, extra_descriptions)

        return QueryResult(
            icon=images_dir('percent.svg'),
            name=name,
            description=description,
            clipboard=name,
            value=self.value,
            order=self.order,
        )
