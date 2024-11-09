"""Defines the Bear class."""

__author__ = "730475190"


class Bear:
    """A bear in the river ecosystem."""

    def __init__(self) -> None:
        """Initialize with age and hunger_score set to 0."""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self) -> None:
        """Age the bear by one day and decrease hunger."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger score based on fish eaten."""
        self.hunger_score += num_fish
