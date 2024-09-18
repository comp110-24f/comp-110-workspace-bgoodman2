"""practice using while loops!"""

__author__ = "730475190"


def num_instances(
    phrase: str, search_char: str
) -> int:  # defining the function and parameters
    if len(search_char) != 1:
        raise ValueError("search_char must be a single character")

    count = 0  # defining count
    index = 0  # defining index

    while index < len(phrase):  # while loop
        if phrase[index] == search_char:
            count += 1
        index += 1

    return count
