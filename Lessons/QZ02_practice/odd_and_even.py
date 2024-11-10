def odd_and_even(nums: list[int]) -> list[int]:
    index: int = 0

    odd_with_even_idx: list[int] = []

    while index < len(nums):
        if nums[index] % 2 == 1 and index % 2 == 0:
            odd_with_even_idx.append(nums[index])
        index += 1
    return odd_with_even_idx


print(odd_and_even([2, 3, 4, 5]))

print(odd_and_even([7, 8, 10, 10, 5, 12, 3, 2, 11, 8]))
