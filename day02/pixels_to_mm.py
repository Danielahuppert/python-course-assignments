


"""
Convert pixel area to mm² and normalize by a second value.
Formula: mm2_area = 2.1462 * pixel_area / 1_000_000
Normalized: normalized_area = mm2_area / normalization_value
"""

def pixels_to_mm2(pixel_area):
    """Convert pixel area to mm² using the given formula."""
    return 2.1462 * pixel_area / 1_000_000


def normalized_area(pixel_area, normalization_value):
    """Convert pixel area to mm² and normalize by another value."""
    mm2 = pixels_to_mm2(pixel_area)
    return mm2 / normalization_value

