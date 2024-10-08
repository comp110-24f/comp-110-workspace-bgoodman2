"""yay for lists so exciting"""

__author__ = "73047590"


def all(numbers: list[int], num: int) -> bool:
    if len(numbers) == 0:
        return False
    idx = 0  # Start from the first element
    while idx < len(numbers):
        if numbers[idx] != num:
            return False
        idx += 1
    return True


def max(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")

    maximum = numbers[0]  # Start with the first element as the maximum

    idx = 1  # Start comparing from the second element (index 1)
    while idx < len(numbers):
        if numbers[idx] > maximum:
            maximum = numbers[idx]  # Update the maximum if a larger value is found
        idx += 1
        """only once the while loop returns false do you go past this line"""
    return maximum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False

    idx = 0  # Start from the first element
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    idx = 0  # Start from index 0
    while idx < len(list2):
        list1.append(list2[idx])  # Append elements from list2 in their original order
        idx += 1
