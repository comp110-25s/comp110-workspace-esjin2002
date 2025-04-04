"""File to define Fish class."""

__author__ = "730469891"


class Fish:
    """Defines a fish."""

    age: int

    def __init__(self):
        """A fish is born."""
        self.age = 0
        return None

    def one_day(self):
        """A fish ages a day."""
        self.age += 1
        return None
