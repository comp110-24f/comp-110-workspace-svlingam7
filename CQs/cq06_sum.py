"""Summing the elements of a list using different loops"""

__author__: str = "730814548"

# vals: list[float] = []


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0

    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


# testing w-sum function
print(w_sum([1.1, 0.9, 1.0]))
print(w_sum([]))


def f_sum(vals: list[float]) -> float:
    sum_f: float = 0.0

    # elem will now reference the values not the index like before
    for elem in vals:
        sum_f += elem

    return sum_f


# testing f-sum function
print(f_sum([1.1, 0.9, 1.0]))
print(f_sum([]))


# testing out code for f-sum

# for num in vals:
#   sum: float = 0.0
#  sum += vals[num]
# print(sum)


def f_range_sum(vals: list[float]) -> float:
    sum_r: float = 0.0

    for num in range(0, len(vals)):
        sum_r += vals[num]
    return sum_r


# testing f_range_sum function
print(f_range_sum([1.1, 0.9, 1.0]))
print(f_range_sum([]))
