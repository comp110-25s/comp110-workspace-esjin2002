"""File to define Bear class."""

__author__ = "730469891"


class Bear:
    """Defines a bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """A bear is born."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """A bear ages a day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bear eat fish."""
        self.hunger_score += num_fish
