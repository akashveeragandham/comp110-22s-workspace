"""Tests for the functions defined in EX05 utils."""

__author__ = "730425241"


from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Basic test of function only_evens."""
    a: list[int] = [1, 2, 3]
    assert only_evens(a) == [2]


def test_only_evens_no_evens() -> None:
    """Test of function only_evens if there are no evens in given list."""
    a: list[int] = [1, 3, 5]
    assert only_evens(a) == []


def test_only_evens_all_evens() -> None:
    """Test of function only_evens if all elements of given list are evens."""
    a: list[int] = [2, 4, 6, 8, 10, 12]
    assert only_evens(a) == [2, 4, 6, 8, 10, 12]


def test_sub() -> None:
    """Basic test of function sub."""
    a_list: list[int] = [10, 20, 30, 40]
    start_index = 1
    end_index = 3
    assert sub(a_list, start_index, end_index) == [20, 30]


def test_sub_larger_sub() -> None:
    """Test of function sub for a subset greater than one additional element."""
    a_list: list[int] = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    start_index = 1
    end_index = 9
    assert sub(a_list, start_index, end_index) == [10, 15, 20, 25, 30, 35, 40, 45]


def test_sub_empty() -> None:
    """Test of function sub if given indexes will produce an empty list."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start_index = 2
    end_index = 2
    assert sub(a_list, start_index, end_index) == []


def test_concat() -> None:
    """Basic test for function concat."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [2, 4, 6]
    assert concat(a, b) == [1, 2, 3, 2, 4, 6]


def test_concat_duplicate() -> None:
    """Test for function concat if a and b are identical lists."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [1, 2, 3]
    assert concat(a, b) == [1, 2, 3, 1, 2, 3]


def test_concat_empty() -> None:
    """Test for function concat if a and b are both empty lists."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []
