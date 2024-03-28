from calculate_anything.lang import LanguageService
import pytest
from calculate_anything.calculation import CalculatorCalculation


def test_calculation_precision():
    value = complex(1.0, 0.0000000000001j)
    calculation = CalculatorCalculation(value, '')
    assert calculation.value == 1
    assert isinstance(calculation.value, int)

    value = complex(1.5124, 0.0000000000001j)
    calculation = CalculatorCalculation(value, '')
    assert calculation.value == pytest.approx(1.5124)
    assert isinstance(calculation.value, float)

    value = complex(2.000000000001)
    calculation = CalculatorCalculation(value, '')
    assert calculation.value == 2
    assert isinstance(calculation.value, int)

    value = complex(2.22122125121)
    calculation = CalculatorCalculation(value, '')
    assert calculation.value == pytest.approx(2.22122125121)
    assert isinstance(calculation.value, float)


def test_value_type():
    assert (
        CalculatorCalculation(CalculatorCalculation(0, ''), '').value_type
        == CalculatorCalculation.ValueType.UNKNOWN
    )
    assert (
        CalculatorCalculation(None, '').value_type
        == CalculatorCalculation.ValueType.NONE
    )
    assert (
        CalculatorCalculation(True, '').value_type
        == CalculatorCalculation.ValueType.BOOLEAN
    )
    assert (
        CalculatorCalculation(1245, '').value_type
        == CalculatorCalculation.ValueType.INT
    )
    assert (
        CalculatorCalculation(0.4564, '').value_type
        == CalculatorCalculation.ValueType.FLOAT
    )
    assert (
        CalculatorCalculation(1 + 0j, '').value_type
        == CalculatorCalculation.ValueType.INT
    )
    assert (
        CalculatorCalculation(1.5 + 0j, '').value_type
        == CalculatorCalculation.ValueType.FLOAT
    )
    assert (
        CalculatorCalculation(0 + 11j, '').value_type
        == CalculatorCalculation.ValueType.IMAGINARY
    )
    assert (
        CalculatorCalculation(2 + 2j, '').value_type
        == CalculatorCalculation.ValueType.COMPLEX
    )


def test_fix_number_presicion():
    assert CalculatorCalculation.fix_number_precision(0.000000000001) == 0
    assert CalculatorCalculation.fix_number_precision(-10e-16) == 0
    assert isinstance(
        CalculatorCalculation.fix_number_precision(0.000000000001), int
    )
    assert CalculatorCalculation.fix_number_precision(11.000000000001) == 11
    assert isinstance(
        CalculatorCalculation.fix_number_precision(11.000000000001), int
    )
    assert CalculatorCalculation.fix_number_precision(11.999999999999) == 12
    assert isinstance(
        CalculatorCalculation.fix_number_precision(11.999999999999), int
    )
    assert CalculatorCalculation.fix_number_precision(11.54679) == 11.54679


def test_get_description():
    translator = LanguageService().get_translator('calculator')

    description = CalculatorCalculation(1, '').get_description()
    assert description == ''

    description = CalculatorCalculation(-4.54, '').get_description()
    assert description == ''

    description = CalculatorCalculation(-4 + 5j, '').get_description()
    assert description == translator('result-complex').capitalize()

    description = CalculatorCalculation(-5j, '').get_description()
    assert description == translator('result-imaginary').capitalize()

    description = CalculatorCalculation(0, '').get_description()
    assert description == ''

    description = CalculatorCalculation(0 + 0j, '').get_description()
    assert description == ''

    description = CalculatorCalculation(
        1 + 0.00000000000001j, ''
    ).get_description()
    assert description == ''

    description = CalculatorCalculation(
        0.000000000001 + 7j, ''
    ).get_description()
    assert description == translator('result-imaginary').capitalize()


def test_format():
    assert CalculatorCalculation(0, '').format() == '0'
    assert CalculatorCalculation(-1j, '').format() == '-i'
    assert CalculatorCalculation(1j, '').format() == 'i'
    assert CalculatorCalculation(121.77j, '').format() == '{:g}i'.format(121.77)
    assert CalculatorCalculation(11.125 + 0j, '').format() == '{:g}'.format(
        11.125
    )
    assert CalculatorCalculation(12 - 1j, '').format() == '{:g} - i'.format(12)
    assert CalculatorCalculation(
        15.77555121551 - 11j, ''
    ).format() == '{:g} - {:g}i'.format(15.77555121551, 11)
    assert CalculatorCalculation(77.95 + 1j, '').format() == '{:g} + i'.format(
        77.95
    )
    assert CalculatorCalculation(
        2 + 0.4555754554j, ''
    ).format() == '{:g} + {:g}i'.format(2, 0.4555754554)
