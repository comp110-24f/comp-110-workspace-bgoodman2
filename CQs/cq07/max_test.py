"""where tests are written to validate the function"""

__author__ = "730475190"


from CQs.cq07.find_max import find_and_remove_max


def test_expected_behavior():
    """Test if the function returns the correct max and removes it."""
    a = [4, 2, 8, 3, 8]
    assert find_and_remove_max(a) == 8
    assert a == [4, 2, 3]


def test_edge_case_empty_list():
    """Test the function with an empty list."""
    a = []
    assert find_and_remove_max(a) == -1
    assert a == []


def test_single_element_list():
    """Test the function with a single element list."""
    a = [5]
    assert find_and_remove_max(a) == 5


if __name__ == "__main__":
    test_expected_behavior()
    test_edge_case_empty_list()
    test_single_element_list()
    print("All tests passed!")  # this will print when all the tests have been passed
