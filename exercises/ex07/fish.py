"""Defines the Fish class."""

__author__ = "730475190"


class Fish:
    """A fish in the river ecosystem."""

    def __init__(self) -> None:
        """Initialize with age set to 0."""
        self.age: int = 0

    def one_day(self) -> None:
        """Age the fish by one day."""
        self.age += 1
