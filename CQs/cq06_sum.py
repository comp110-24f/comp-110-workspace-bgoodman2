"""summing the elements of a list using different loops"""

__author__ = "730475190"


# Part 1: w_sum
def w_sum(vals: list[float]) -> float:
    """Sum the elements of the list using a while loop."""
    idx = 0
    total = 0.0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


# Part 2: f_sum
def f_sum(vals: list[float]) -> float:
    """Sum the elements of the list using a for ... in ... loop."""
    total = 0.0
    for val in vals:
        total += val
    return total


# Part 3: f_range_sum
def f_range_sum(vals: list[float]) -> float:
    """Sum the elements of the list using a for ... in range(...) loop."""
    total = 0.0
    for idx in range(len(vals)):
        total += vals[idx]
    return total
