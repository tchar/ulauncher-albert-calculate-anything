from calculate_anything.lang import LanguageService
import pytest
from calculate_anything.calculation.calculation import Calculation


def test_calculation_precision():
    value = complex(1.0, 0.0000000000001j)
    calculation = Calculation(value)
    assert calculation.value == 1
    assert isinstance(calculation.value, int)

    value = complex(1.5124, 0.0000000000001j)
    calculation = Calculation(value)
    assert calculation.value == pytest.approx(1.5124)
    assert isinstance(calculation.value, float)

    value = complex(2.000000000001)
    calculation = Calculation(value)
    assert calculation.value == 2
    assert isinstance(calculation.value, int)

    value = complex(2.22122125121)
    calculation = Calculation(value)
    assert calculation.value == pytest.approx(2.22122125121)
    assert isinstance(calculation.value, float)


def test_value_type():
    assert Calculation(Calculation(0)).value_type == Calculation.VALUE_UNKNOWN
    assert Calculation(None).value_type == Calculation.VALUE_NONE
    assert Calculation(True).value_type == Calculation.VALUE_BOOLEAN
    assert Calculation(1245).value_type == Calculation.VALUE_INT
    assert Calculation(0.4564).value_type == Calculation.VALUE_FLOAT
    assert Calculation(1+0j).value_type == Calculation.VALUE_INT
    assert Calculation(1.5+0j).value_type == Calculation.VALUE_FLOAT
    assert Calculation(0+11j).value_type == Calculation.VALUE_IMAGINARY
    assert Calculation(2+2j).value_type == Calculation.VALUE_COMPLEX


def test_fix_number_presicion():
    assert Calculation.fix_number_precision(0.000000000001) == 0
    assert isinstance(Calculation.fix_number_precision(0.000000000001), int)
    assert Calculation.fix_number_precision(11.000000000001) == 11
    assert isinstance(Calculation.fix_number_precision(11.000000000001), int)
    assert Calculation.fix_number_precision(11.999999999999) == 12
    assert isinstance(Calculation.fix_number_precision(11.999999999999), int)
    assert Calculation.fix_number_precision(11.54679) == 11.54679


def test_get_description():
    translator = LanguageService().get_translator('calculator')

    description = Calculation(1).get_description()
    assert description == ''

    description = Calculation(-4.54).get_description()
    assert description == ''

    description = Calculation(-4 + 5j).get_description()
    assert description == translator('result-complex').capitalize()

    description = Calculation(-5j).get_description()
    assert description == translator('result-imaginary').capitalize()

    description = Calculation(0).get_description()
    assert description == ''

    description = Calculation(0 + 0j).get_description()
    assert description == ''

    description = Calculation(1 + 0.00000000000001j).get_description()
    assert description == ''

    description = Calculation(0.000000000001 + 7j).get_description()
    assert description == translator('result-imaginary').capitalize()


def test_format_query():
    # TODO: Implement
    pass


def test_format():
    assert Calculation(0).format() == '0'
    assert Calculation(-1j).format() == '-i'
    assert Calculation(1j).format() == 'i'
    assert Calculation(121.77j).format() == '{:g}i'.format(121.77)
    assert Calculation(11.125 + 0j).format() == '{:g}'.format(11.125)
    assert Calculation(12 - 1j).format() == '{:g} - i'.format(12)
    assert Calculation(
        15.77555121551 - 11j).format() == '{:g} - {:g}i'.format(15.77555121551, 11)
    assert Calculation(77.95 + 1j).format() == '{:g} + i'.format(77.95)
    assert Calculation(
        2 + 0.4555754554j).format() == '{:g} + {:g}i'.format(2, 0.4555754554)
