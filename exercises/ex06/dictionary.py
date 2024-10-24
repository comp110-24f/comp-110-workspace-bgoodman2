"""dictonary utilization practice"""

__auhtor__ = "730475190"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the input dictionary."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate key encountered in inverted dictionary!")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the input dictionary."""
    color_count: dict[str, int] = {}  # Added type annotation for color_count

    for color in colors.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    most_frequent_color = ""
    max_count = 0

    for color, count in color_count.items():
        if count > max_count:
            most_frequent_color = color
            max_count = count
        elif count == max_count:
            continue

    return most_frequent_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the occurrences of each unique item in the input list."""
    count_dict: dict[str, int] = {}  # Added type annotation for count_dict

    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Organizes words by their starting letter into a dictionary."""
    alphabetized_dict: dict[str, list[str]] = {}  # Added type annotation

    for word in words:
        first_letter = word[0].lower()
        if first_letter in alphabetized_dict:
            alphabetized_dict[first_letter].append(word)
        else:
            alphabetized_dict[first_letter] = [word]

    return alphabetized_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    if day in attendance:
        if student not in attendance[day]:  # no duplicates
            attendance[day].append(student)
    else:
        attendance[day] = [student]
