"""
Business logic: convert pixel area to mm² and normalize.

Formula: mm2_area = 2.1462 * pixel_area / 1_000_000
"""

def pixels_to_mm2(pixel_area: float) -> float:
    """Convert pixel area to mm² using the given formula.

    Args:
        pixel_area: area in pixels (can be zero or positive)

    Returns:
        area in mm²
    """
    return 2.1462 * pixel_area / 1_000_000


def normalized_area(pixel_area: float, normalization_value: float) -> float:
    """Convert pixel area to mm² and normalize by another value.

    Raises ZeroDivisionError if normalization_value is zero.
    """
    if normalization_value == 0:
        raise ZeroDivisionError("Normalization value must be non-zero")
    mm2 = pixels_to_mm2(pixel_area)
    return mm2 / normalization_value
