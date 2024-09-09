"""planning a cozy tea party!"""

_author_: str = "730475190"  # my PID and identification for the professor :)


def main_planner(guests: int) -> int:
    """number of guests attending"""
    tea_count = tea_bags(guests)
    treat_count = treats(guests)
    total_cost = cost(tea_count, treat_count)
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_count))
    print("Treats: " + str(treat_count))
    print(
        "Cost: $" + str(total_cost)
    )  # all of the above print functions should return the computations already done in the earlier definitions (this was by far the hardest for myself to complete)


def tea_bags(people: int) -> int:
    """defining the teabag function, number of tea bags"""
    return people * 2  # want to do *2 because we are accounting for 2 teas per person


def treats(people: int) -> int:
    """defining the treat function, number of treats"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """cost of tea and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(
        guests=int(input("how many guests are attending your tea party"))
    )  # always you to use the "run" function in the trailhead
