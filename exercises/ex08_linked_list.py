"""recursion practice"""

__author__ = "730475190"


class Node:
    """Class representing a single Node in a singly linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """Return a string representation of the linked list."""
        return f"{self.data} -> {repr(self.next)}"


def value_at(head, index):
    """Return the value at the given index in a linked list or raise IndexError."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.data
    return value_at(head.next, index - 1)


def max(head):
    """Return the maximum value in the linked list or raise ValueError id empty"""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.data
    max_rest = max(head.next)
    return head.data if head.data > max_rest else max_rest


def linkify(items):
    """Convert a list of integers into a linked list."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head, factor):
    """Return a new linked list where each value is scaled by the given factor."""
    if head is None:
        return None
    return Node(head.data * factor, scale(head.next, factor))
