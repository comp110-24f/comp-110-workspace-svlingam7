"""Mutating functions."""

__author__: str = "730814548"

# global variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(int_list: list[int], num: int) -> None:
    """to add num to the end of int_list"""
    int_list.append(num)


def double(int_list: list[int]) -> None:
    """to double each index in int_list"""

    # the lines with # below are just code that I tried out and didn't work
    # double_list: list[int] = []
    # double_num: int = 0

    index: int = 0

    while index < len(int_list):
        # b/c we aren't creating a new list but are instead changing the og list
        int_list[index] = int_list[index] * 2

        # the lines with # below are just code that I tried out and didn't work
        # double_num = 0
        # double_num = int_list[index] * 2

        # double_list.append(double_num)
        # double_list.append(int_list[index] * 2)

        index += 1


# calling the fn double
double(list_2)
print(list_1)
print(list_2)
