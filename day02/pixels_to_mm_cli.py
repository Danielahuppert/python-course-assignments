"""
CLI and interactive entry point for pixels_to_mm library.

Usage (command-line):
    python pixels_to_mm_cli.py --pixel_area 12345 --normalization_value 10

If arguments are omitted, the script will prompt interactively.
"""
import argparse
import sys
from pixels_to_mm import pixels_to_mm2, normalized_area


def main(argv=None):
    parser = argparse.ArgumentParser(description="Convert pixel area to mm² and normalize.")
    parser.add_argument('--pixel_area', type=float, help='Pixel area value')
    parser.add_argument('--normalization_value', type=float, help='Normalization value')
    args = parser.parse_args(argv)

    if args.pixel_area is not None and args.normalization_value is not None:
        pixel_area = args.pixel_area
        normalization_value = args.normalization_value
    else:
        try:
            pixel_area = float(input("Enter pixel area: "))
            normalization_value = float(input("Enter normalization value: "))
        except ValueError:
            print("Please enter valid numbers.")
            return 1

    if normalization_value == 0:
        print("Normalization value must be non-zero.")
        return 1

    mm2 = pixels_to_mm2(pixel_area)
    norm = normalized_area(pixel_area, normalization_value)
    print(f"Area in mm²: {mm2:.6f}")
    print(f"Normalized area: {norm:.6f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
