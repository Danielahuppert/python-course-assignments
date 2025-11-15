import pytest
from day03.pixels_to_mm import pixels_to_mm2, normalized_area


def test_pixels_to_mm2_zero():
    assert pixels_to_mm2(0) == pytest.approx(0.0)


def test_pixels_to_mm2_positive():
    # 100000 pixels => 2.1462 * 100000 / 1_000_000 = 0.21462
    assert pixels_to_mm2(100000) == pytest.approx(0.21462)


def test_normalized_area():
    # Use 100000 pixels and normalization 2 => normalized = 0.21462 / 2
    assert normalized_area(100000, 2) == pytest.approx(0.21462 / 2)


def test_normalized_area_zero_division():
    with pytest.raises(ZeroDivisionError):
        normalized_area(1000, 0)


def test_negative_pixel_area():
    # Negative pixel area should still compute (depends on domain), verify formula
    assert pixels_to_mm2(-100000) == pytest.approx(-0.21462)
