"""Using loops for various different purposes"""

__author__: str = "730814548"


def all(all_list: list[int], num: int) -> bool:
    """To see if all the elems in a list are the same as the num"""
    index: int = 0
    # have to add an second local variable to keep track of
    # how many of the elems are the same as num
    occurances: int = 0

    while index < len(all_list):
        if num == all_list[index]:
            occurances += 1

        if occurances == len(all_list):
            return True
        index += 1  # will increase no matter what
    return False  # default return


# Testing all function
# print(all([1, 2, 3], 1)) # result = False
# print(all([1, 1, 1], 2)) # result =  False
# print(all([1, 1, 1], 1)) # result = True


def max(max_list: list[int]) -> int:
    """To find the biggest number in the list"""

    index: int = 0
    max_num: int = -100000000  # so that even neg ints list can find the max

    # the code below works but is what I did before noticing that
    # the beginning of max was given
    # if max_list == []:
    # print("ValueError: max() arg is an empty List")
    # quit() #if error occurs take this out

    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")

    while index < len(max_list):
        if max_num < max_list[index]:
            # max_num will become equal to the number that is bigger & store it
            max_num = max_list[index]
        index += 1  # index must always increase
    return max_num


# Testing max function
# print(max([1, 3, 2])) # result = 3
# print(max([100, 99, 98])) # result = 100
# print(max([])) # result = empty list


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """To check and see if both lists are exactly the same"""

    index: int = 0

    # if statement will allow the fn to not waste time by checking each elem in list
    if len(list_1) != len(list_2):
        return False

    while index < len(list_1):
        if list_1[index] != list_2[index]:
            return False
        index += 1
    return True  # default


# testing is_equal function
# print(is_equal([1, 0, 1], [1, 0, 1])) # result = True
# print(is_equal([1, 1, 0], [1, 0, 1])) # result = False


def extend(a: list[int], b: list[int]) -> None:
    """To add list b to the end of list a"""

    index: int = 0
    while index < len(b):
        a.append(b[index])
        # print(a) # -> testing the function
        index += 1
