"""coornidatees python module cq04"""

__author__ = "730475190"


def get_coords(xs: str, ys: str) -> None:  # defining get cords
    """Prints formatted pairs of each character in the two input strings."""
    for x, y in zip(xs, ys):
        print(f"({x}, {y})")
