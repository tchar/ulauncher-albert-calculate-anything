import pytest
from calculate_anything.utils.colors import (
    hex_to_rgb,
    rgb_to_cmyk,
    rgb_to_hsl,
    rgb_to_hsv,
)


@pytest.mark.parametrize(
    '_input,expected',
    [
        ('000000', (0, 0, 0)),
        ('FFFFFF', (255, 255, 255)),
        ('FF0000', (255, 0, 0)),
        ('00FF00', (0, 255, 0)),
        ('00FFFF', (0, 255, 255)),
        ('FF00FF', (255, 0, 255)),
        ('C0C0C0', (192, 192, 192)),
        ('008000', (0, 128, 0)),
        ('800080', (128, 0, 128)),
        ('008080', (0, 128, 128)),
        ('000080', (0, 0, 128)),
        ('ZFASD', ValueError),
        ('A', ValueError),
        (None, TypeError),
    ],
)
def test_hex_to_rgb(_input, expected):
    if isinstance(expected, tuple):
        assert hex_to_rgb(_input)
    else:
        with pytest.raises(expected):
            hex_to_rgb(_input)


@pytest.mark.parametrize(
    '_input,expected',
    [
        ((139, 0, 22), (0, 1, 0.8417, 0.4549)),
        ((178, 0, 31), (0, 1, 0.8258, 0.3020)),
        ((0, 174, 114), (1, 0, 0.3448, 0.3176)),
        ((103, 191, 127), (0.4607, 0, 0.3350, 0.2510)),
        ((93, 12, 123), (0.2439, 0.9024, 0, 0.5176)),
        ((121, 55, 139), (0.1294, 0.6043, 0, 0.4549)),
        ((215, 215, 215), (0, 0, 0, 0.1568)),
        ((194, 194, 194), (0, 0, 0, 0.2392)),
        ((1,), ValueError),
        (1, TypeError),
    ],
)
def test_rgb_to_cmyk(_input, expected):
    if isinstance(expected, tuple):
        result = rgb_to_cmyk(_input)
        assert result == pytest.approx(expected, 0.001)
    else:
        with pytest.raises(expected):
            rgb_to_cmyk(_input)


@pytest.mark.parametrize(
    '_input,expected',
    [
        ((139, 0, 22), (350.5035, 1.0, 0.5450)),
        ((178, 0, 31), (349.5507, 1.0, 0.6980)),
        ((0, 174, 114), (159.3103, 1.0, 0.6823)),
        ((103, 191, 127), (136.3636, 0.4607, 0.7490)),
        ((93, 12, 123), (283.7838, 0.9024, 0.4824)),
        ((121, 55, 139), (287.1429, 0.6043, 0.5451)),
        ((215, 215, 215), (0, 0.0, 0.8431)),
        ((194, 194, 194), (0, 0.0, 0.7608)),
        ((1,), ValueError),
        (1, TypeError),
    ],
)
def test_rgb_to_hsv(_input, expected):
    if isinstance(expected, tuple):
        result = rgb_to_hsv(_input)
        assert result == pytest.approx(expected, 0.001)
    else:
        with pytest.raises(expected):
            rgb_to_hsv(_input)


@pytest.mark.parametrize(
    '_input,expected',
    [
        ((139, 0, 22), (350.5036, 1.0, 0.2725)),
        ((178, 0, 31), (349.5506, 1.0, 0.3490)),
        ((0, 174, 114), (159.3103, 1.0, 0.3411)),
        ((103, 191, 127), (136.3636, 0.4074, 0.5765)),
        ((93, 12, 123), (283.7838, 0.8222, 0.2647)),
        ((121, 55, 139), (287.1429, 0.4330, 0.3804)),
        ((215, 215, 215), (0, 0, 0.8431)),
        ((194, 194, 194), (0, 0, 0.7608)),
        ((1,), ValueError),
        (1, TypeError),
    ],
)
def test_rgb_to_hsl(_input, expected):
    if isinstance(expected, tuple):
        result = rgb_to_hsl(_input)
        assert result == pytest.approx(expected, 0.001)
    else:
        with pytest.raises(expected):
            rgb_to_hsl(_input)
