"""Practice with lists"""

__author__: str = "730814548"


def only_evens(int_list: list[int]) -> list:
    """goes through the input list and returns the even numbers"""
    evens_list: list[int] = []
    # index: int = 0

    for num in int_list:
        if num % 2 == 0:
            evens_list.append(num)

    # while index < len(int_list):
    # if int_list[index] % 2 == 0:
    #     evens_list.append(int_list[index])
    # else:
    #     return []
    # index += 1
    return evens_list


def sub(int_list: list[int], start_idx: int, stop_idx: int) -> list:
    """returning a subset of ints from int_list"""
    sub_list: list[int] = []
    index: int = 0

    if start_idx < 0:
        start_idx = 0

    if stop_idx > len(int_list):
        stop_idx = len(int_list)

    if (len(int_list) == 0) or (start_idx >= len(int_list)) or (stop_idx == 0):
        return sub_list

    while index < len(int_list):
        if (index >= start_idx) and (index < stop_idx):
            sub_list.append(int_list[index])
        index += 1

    # sub_list.append(int_list[start_idx])
    # sub_list.append(int_list[stop_idx - 1])

    return sub_list


def add_at_index(int_list: list[int], add_int: int, idx_add: int) -> None:
    """adding an int at the given index"""
    if idx_add < 0 or idx_add > len(int_list):  # or 0 == len(int_list):
        raise IndexError("Index is out of bounds for the input list")

    int_list.append(0)
    index: int = len(int_list) - 1
    # copy_list: list[int] = []

    # int_list.insert(idx_add, add_int)

    # while index < len(int_list):
    #     copy_list.append(int_list[index])
    #     index += 1

    # index = 0

    # while index < len(int_list):
    #     # print(int_list)

    #     if idx_add == index:
    #         if index == len(int_list) - 1:
    #             int_list[len(int_list) - 1] = add_int
    #         else:
    #             int_list[(index + 1)] = copy_list[index]
    #             int_list[index] = add_int
    #     index += 1

    while index > idx_add:
        int_list[index] = int_list[index - 1]
        index -= 1
    int_list[idx_add] = add_int


# testing

# list_1: list[int] = [1, 2, 3, 5]
# list_2: list[int] = [1]
# list_3: list[int] = []

# add_at_index(list_1, 4, 3)
# print(list_1)

# add_at_index(list_2, 2, 1)
# print(list_2)

# add_at_index(list_3, 1, 1)
