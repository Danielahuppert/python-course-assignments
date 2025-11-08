


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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert pixel area to mm² and normalize.")
    parser.add_argument('--pixel_area', type=float, help='Pixel area value')
    parser.add_argument('--normalization_value', type=float, help='Normalization value')
    args = parser.parse_args()

    if args.pixel_area is not None and args.normalization_value is not None:
        pixel_area = args.pixel_area
        normalization_value = args.normalization_value
    else:
        try:
            pixel_area = float(input("Enter pixel area: "))
            normalization_value = float(input("Enter normalization value: "))
        except ValueError:
            print("Please enter valid numbers.")
            exit(1)

    mm2 = pixels_to_mm2(pixel_area)
    norm = normalized_area(pixel_area, normalization_value)
    print(f"Area in mm²: {mm2:.6f}")
    print(f"Normalized area: {norm:.6f}")
