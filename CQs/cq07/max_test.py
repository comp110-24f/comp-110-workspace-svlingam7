"""Testing find_max fn"""

__author__: str = "730814548"


from CQs.cq07.find_max import find_and_remove_max


def test_farm_expected_value() -> None:
    """find max should return max val"""
    int_list: list[int] = [7, 9, 5, 4, 12, 5]
    assert find_and_remove_max(int_list) == 12


def test_farm_empty() -> None:
    int_list: list[int] = []
    assert find_and_remove_max(int_list) == -1


def test_farm_mutate() -> None:
    int_list: list[int] = [7, 9, 5, 4, 12, 5]
    find_and_remove_max(int_list)
    assert int_list == [7, 9, 5, 4, 5]


def test_farm_multiple_max() -> None:
    int_list: list[int] = [7, 9, 12, 5, 4, 12, 6]
    find_and_remove_max(int_list)
    assert int_list == [7, 9, 5, 4, 6]
