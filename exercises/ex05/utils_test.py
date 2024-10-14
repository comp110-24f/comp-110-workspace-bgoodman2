""""where unit tests are defined"""

__author__ = "730475190"


from exercises.ex05.utils import only_evens, sub, add_at_index


# Tests for only_evens
def test_only_evens_with_no_evens():
    """Test only_evens with a list that contains no even numbers."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_with_all_evens():
    """Test only_evens with a list that contains all even numbers."""
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens_with_mixed_list():
    """Test only_evens with a list containing both even and odd numbers."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


# Tests for sub
def test_sub_normal_case():
    """Test sub with a typical range."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_out_of_range_case():
    """Test sub with indices out of range."""
    assert sub([10, 20, 30, 40], -1, 5) == [10, 20, 30, 40]


def test_sub_empty_list_case():
    """Test sub with an empty list."""
    assert sub([], 1, 3) == []


# Tests for add_at_index
def test_add_at_index_in_the_middle():
    """Test add_at_index by adding an element in the middle."""
    test_list = [1, 2, 4]
    add_at_index(test_list, 3, 2)
    assert test_list == [1, 2, 3, 4]


def test_add_at_index_at_start():
    """Test add_at_index by adding an element at the start."""
    test_list = [2, 3]
    add_at_index(test_list, 1, 0)
    assert test_list == [1, 2, 3]


def test_add_at_index_at_end():
    """Test add_at_index by adding an element at the end."""
    test_list = [1, 2, 3]
    add_at_index(test_list, 4, 3)
    assert test_list == [1, 2, 3, 4]
