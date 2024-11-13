"""Module for working with linked lists."""

from __future__ import annotations

__author__ = "730475190"


class Node:
    """A single Node of a singly linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialize a new node with the given value and next pointer."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of the linked list."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def to_str(head: Node | None) -> str:
    """Represent a linked list as a string."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a non-empty linked list."""
    if head.next is None:
        return head.value
    else:
        return last(head.next)


def value_at(head: Node | None, index: int) -> int:
    """Return the value at the given index in the linked list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    max_rest = max(head.next)
    return head.value if head.value > max_rest else max_rest


def linkify(items: list[int]) -> Node | None:
    """Convert a list of integers into a linked list."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list with all values scaled by the given factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
