"""mutating functions"""

__author__ = "730475190"


def manual_append(a: list[int], num: int) -> None:
    """adds the given number to the list"""
    a.append(num)


def double(a: list[int]) -> None:
    """doubles each elemenet found in the list"""
    idx = 0  # index variable
    while idx < len(a):
        a[idx] *= 2  # multiplying the current element by 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
