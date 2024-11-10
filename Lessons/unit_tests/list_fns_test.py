from Lessons.unit_tests.list_fns import get_first, remove_first  # ,get_and_remove_first


def test_get_first() -> None:
    """get_first should return first element"""

    colors: list[str] = ["blue", "green", "yellow", "purple"]
    assert (get_first(colors)) == "blue"


def test_remove_first_return_value() -> None:
    """remove_first should return None"""
    colors: list[str] = ["blue", "green", "yellow", "purple"]
    assert remove_first(colors) is None


def test_remove_first_behavior() -> None:
    """reomve_first should remove first elem from list"""
    colors: list[str] = ["blue", "green", "yellow", "purple"]

    remove_first(colors)
    assert colors == ["green", "yellow", "purple"]

    # python -m Lessons.unit_tests.list_fns_test.py


# def test_get_first_edge_case() -> None:
# """get_first called on empty list should return " " """
# input: list[str] = []
# assert get_first(input) == ""

# or
#  assert get_first([]) == ""
