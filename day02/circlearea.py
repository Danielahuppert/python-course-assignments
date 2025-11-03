import math


def circle_area(radius):
    """Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle. Must be non-negative.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)


if __name__ == "__main__":
    try:
        radius_str = input("Enter the radius of the circle: ")
        radius = float(radius_str)
        area = circle_area(radius)
        print(f"Circle with radius {radius} has area: {area:.4f}")
    except ValueError:
        print("Please enter a valid non-negative number for radius.")

