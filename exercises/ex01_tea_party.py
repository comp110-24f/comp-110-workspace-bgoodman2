"""planning a cozy tea party!"""

__author__ = "730475190"  # my identification for the professor :)


def main_planner(guests: int) -> None:
    """number of guests attending"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(people=guests)))
    )  # above print functions should return the computations done earlier in def.


def tea_bags(people: int) -> int:
    """defining the teabag function, number of tea bags"""
    return people * 2  # want to do *2 because we are accounting for 2 teas per person


def treats(people: int) -> int:
    """defining the treat function, number of treats"""
    return int(
        tea_bags(people=people) * 1.5
    )  # call to tea_bags with a keyword argument


def cost(tea_count: int, treat_count: int) -> float:
    """cost of tea and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(
        guests=int(input("how many guests are attending your tea party"))
    )  # need to write to use the "run" function in the trailhead
