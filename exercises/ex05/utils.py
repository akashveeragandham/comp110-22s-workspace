"""Definitions of functions being tested in EX05."""

__author__ = "730425241"


def only_evens(a: list[int]) -> list[int]:
    """Given a list of integers, will return a list of only the even numbers."""
    evens: list[int] = list()
    i: int = 0
    while i < len(a):
        if a[i] == (a[i] // 2) * 2:
            evens.append(a[i])
        i += 1
    return evens


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list of integers as well as a start and end index, will return a subset of given list."""
    subset: list[int] = list()
    i: int = start_index
    if len(a_list) >= 1:
        while i < end_index:
            if i >= 0:
                subset.append(a_list[i])
            i += 1
    return subset


def concat(a: list[int], b: list[int]) -> list[int]:
    """Given two lists of integers, will return a new list containing all elements of the first list followed by all elements of the second list."""
    combined: list[int] = list()
    i: int = 0
    while i < len(a):
        combined.append(a[i])
        i += 1
    i = 0
    while i < len(b):
        combined.append(b[i])
        i += 1
    return combined
