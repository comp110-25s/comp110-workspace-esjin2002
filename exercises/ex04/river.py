"""File to define River class."""

__author__ = "730469891"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Defines river."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of animals."""
        new_bears: list[Bear] = []
        new_fish: list[Fish] = []
        for dabear in self.bears:
            if dabear.age <= 5:
                new_bears.append(dabear)
        for feesh in self.fish:
            if feesh.age <= 3:
                new_fish.append(feesh)

        self.bears = new_bears
        self.fish = new_fish
        return None

    def bears_eating(self):
        """When bear eat fish."""
        for dabear in self.bears:
            if len(self.fish) >= 5:
                dabear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Remove bear if dead from hunger."""
        new_bears: list[Bear] = []
        for dabear in self.bears:
            if dabear.hunger_score >= 0:
                new_bears.append(dabear)

        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """Fish make more fish."""
        how_many: int = (len(self.fish) // 2) * 4
        for _ in range(0, how_many):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Bear make more bear."""
        how_many: int = len(self.bears) // 2
        for _ in range(0, how_many):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """See how much of each animal there is."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week in river."""
        for _ in range(0, 7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes fish from river."""
        for _ in range(0, amount):
            self.fish.pop(0)
