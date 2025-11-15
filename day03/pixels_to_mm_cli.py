"""
CLI using Click that uses the business logic in pixels_to_mm.py
"""
import sys
import click
from pixels_to_mm import pixels_to_mm2, normalized_area


@click.command()
@click.option('--pixel-area', '-p', type=float, required=False, help='Pixel area value')
@click.option('--normalization-value', '-n', type=float, required=False, help='Normalization value')
def main(pixel_area, normalization_value):
    """Run conversion from CLI or prompt interactively when missing."""
    try:
        if pixel_area is None:
            pixel_area = float(click.prompt('Enter pixel area', type=float))
        if normalization_value is None:
            normalization_value = float(click.prompt('Enter normalization value', type=float))

        mm2 = pixels_to_mm2(pixel_area)
        norm = normalized_area(pixel_area, normalization_value)

        click.echo(f"Area in mm²: {mm2:.6f}")
        click.echo(f"Normalized area: {norm:.6f}")
    except ValueError:
        click.echo('Please enter valid numeric values.', err=True)
        sys.exit(1)
    except ZeroDivisionError:
        click.echo('Normalization value must be non-zero.', err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
