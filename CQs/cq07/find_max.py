"""some function defintions included below"""

__author__ = "730475190"


def find_and_remove_max(lst: list[int]) -> int:
    if not lst:
        return -1

    max_value = max(lst)

    # Remove all instances of the max value
    while max_value in lst:
        lst.remove(max_value)

    return max_value
