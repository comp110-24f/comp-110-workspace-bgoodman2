"""implement list utility functions"""

__author__ = "730475190"


__author__ = "Your PID"


def only_evens(index: list[int]) -> list[int]:
    """Return a list of even integers from the input list."""
    result = []
    idx = 0
    while idx < len(index):
        if index[idx] % 2 == 0:
            result.append(index[idx])
        idx += 1
    return result


def sub(index: list[int], start: int, end: int) -> list[int]:
    """Return a subset of the list from start index to end index - 1."""
    result = []
    if len(index) == 0 or start >= len(index) or end <= 0:
        return result

    if start < 0:
        start = 0
    if end > len(index):
        end = len(index)

    idx = start
    while idx < end:
        result.append(index[idx])
        idx += 1
    return result


def add_at_index(index: list[int], element: int, idx: int) -> None:
    """Add an element at the specified index of the input list."""
    if idx < 0 or idx > len(index):
        raise IndexError("Index is out of bounds for the input list")

    index.append(0)  # Append a dummy element to increase the size of the list

    # Shift all elements to the right starting from the last element to the idx
    i = len(index) - 1
    while i > idx:
        index[i] = index[i - 1]
        i -= 1

    # Insert the element at idx
    index[idx] = element
