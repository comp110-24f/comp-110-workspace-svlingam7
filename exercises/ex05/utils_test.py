"""testing utils and its functions"""

__author__: str = "730814548"


from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest

# testing for only_evens fn


# only_evens edge case
def test_only_evens_edge_case_odds() -> None:
    """In the instance of an odd only list it shoudld return [] back"""
    input_list: list[int] = [1, 5, 7]
    assert only_evens(input_list) == []


# def test_only_evens_odds_ec() -> None:
# "return empty list in case of all odds"


# # only_evens expected return
# def test_only_evens_return() -> None:
#     """checking to see that the return value of only_evens is a list"""
#     num_list: list[int] = [2, 4, 5, 5, 8, 7, 10, 10]
#     assert only_evens(num_list) is list


# only_evens even only case
def test_only_evens_evens() -> None:
    input_list: list[int] = [6, 4, 8]
    assert only_evens(input_list) == [6, 4, 8]


# only_evens expected value
def test_only_evens_mutate() -> None:
    """only_evens should return a mutated list with only the even ints of input list"""
    num_list: list[int] = [2, 7, 4]
    assert only_evens(num_list) == [2, 4] and num_list == [2, 7, 4]


# Testing sub fn


# sub edge case
def test_sub_edge_case() -> None:
    """In the instance of an empty list it shoudld return [] back"""
    input_list: list[int] = []
    assert sub(input_list, 2, 3) == []


# sub expected return
# def test_sub_return() -> None:
#     """checking to see what the return value of sub"""
#     num_list: list[int] = [2, 4, 5, 5, 8, 7, 10, 10]
#     assert sub(num_list, 1, 3) == list

# sub expected val- out of bound indexes


def test_sub_idx_bounds() -> None:
    """testing sub to see how it reacts when the start
    and stop indexes are out of bounds"""
    input_list: list[int] = [1, 3, 2, 8, 7]
    assert sub(input_list, -2, 8) == [1, 3, 2, 8, 7]


# sub expected value
def test_sub_mutate() -> None:
    """should return a sub_list from the input list"""
    input_list: list[int] = [2, 4, 5, 5, 10]
    assert sub(input_list, 0, 3) == [2, 4, 5]


# test add_to_index


# add_to_index edge case
def test_ati_raise_index_error() -> None:
    """checks to see if it raises an IndexError"""
    with pytest.raises(IndexError):
        input_list: list[int] = []
        add_at_index(input_list, 3, 2)


# add_to_index return
def test_ati_return() -> None:
    """checking what the return value of add_at_index is"""
    input_list: list[int] = [2, 4, 5, 5, 8, 7, 10, 10]
    assert add_at_index(input_list, 3, 2) is None


# add_to index expected value
def test_ati_expected_value() -> None:
    """checking to see if the input int is added correctly"""
    num_list: list[int] = [2, 7, 4]
    add_at_index(num_list, 3, 1)
    assert num_list == [2, 3, 7, 4]
