"""Runs a simulation of a river ecosystem with bears and fish."""

__author__ = "730475190"

from exercises.ex07.river import River


def main() -> None:
    """Run the river simulation."""
    # Create a river with 10 fish and 2 bears
    my_river = River(10, 2)
    my_river.view_river()

    # Simulate one week in the river
    my_river.one_river_week()
    my_river.view_river()


if __name__ == "__main__":
    main()
