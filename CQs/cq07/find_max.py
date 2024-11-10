"""Finding the max of a list of ints and removing all instances of it"""

__author__: str = "730814548"


def find_and_remove_max(input: list[int]) -> int:
    """Locating and removing all instances of max num from the list"""
    index: int = 0
    max_num: int = -100000000  # so that even neg ints list can find the max
    # max_occur: list[int] = []

    if len(input) == 0:
        return -1

    while index < len(input):
        if max_num < input[index]:
            # max_num will become equal to the number that is bigger & store it
            max_num = input[index]
        index += 1  # index must always increase

    index = 0

    while index < len(input):
        if max_num == input[index]:
            input.pop(index)

        else:
            index += 1

    # for elem in max_occur:
    #  input.pop(elem)

    return max_num


# testing
# a: list[int] = []
# print(find_and_remove_max(a))
# print(a)

# b: list[int] = [10, 9, 8, 7, 10]
# print(find_and_remove_max(b))
# print(b)

# c: list[int] = [9, 9, 8, 7]
# print(find_and_remove_max(c))
# print(c)

int_list: list[int] = [7, 9, 5, 4, 12, 5]
print(find_and_remove_max(int_list))
print(int_list)
