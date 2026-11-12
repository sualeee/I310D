import math


def calculate_volume_of_sphere(radius):
    """Return the volume of a sphere: V = (4/3) * pi * r^3."""
    return (4 / 3) * math.pi * radius ** 3


if __name__ == "__main__":
    for r in (30, 40):
        print(f"Volume of sphere with radius {r}: {calculate_volume_of_sphere(r):.2f}")
