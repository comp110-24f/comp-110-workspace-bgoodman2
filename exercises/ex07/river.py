"""Simulates a river ecosystem with bears and fish."""

__author__ = "730475190"

from exercises.ex07.bear import Bear
from exercises.ex07.fish import Fish


class River:
    """A river with bears and fish."""

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """Initialize with given number of fish and bears."""
        self.day: int = 0
        self.fish: list[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: list[Bear] = [Bear() for _ in range(num_bears)]

    def view_river(self) -> None:
        """Print current state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day in the river."""
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        self.day += 1

    def one_river_week(self) -> None:
        """Simulate a week (7 days) in the river."""
        for _ in range(7):
            self.one_river_day()

    def check_ages(self) -> None:
        """Remove old fish and bears."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int) -> None:
        """Remove a number of fish from the front."""
        self.fish = self.fish[amount:]

    def bears_eating(self) -> None:
        """Each bear eats 3 fish if enough are available."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Remove starving bears."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_bears(self) -> None:
        """Add new bears based on pairs."""
        new_bears = len(self.bears) // 2
        self.bears.extend(Bear() for _ in range(new_bears))

    def repopulate_fish(self) -> None:
        """Add new fish based on pairs."""
        new_fish = (len(self.fish) // 2) * 4
        self.fish.extend(Fish() for _ in range(new_fish))
