"""More practice with linked lists."""

from __future__ import annotations

__author__: str = "730469891"


class Node:
    """Defines Node class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Constructor for Node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Prints Node as str."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Returns value of Node at index."""
    if head is None:
        raise IndexError("Index out of range.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns max value of Node."""
    if head is None:
        raise ValueError("Cannot call max with None.")

    if head is None:
        raise ValueError("Linked list is empty")

    if head.next is None:
        return head.value

    max_in_rest = max(head.next)
    return head.value if head.value > max_in_rest else max_in_rest


def linkify(items: list[int]) -> Node | None:
    """Converts list to linked list."""
    if not items:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list with values scaled by the given factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
