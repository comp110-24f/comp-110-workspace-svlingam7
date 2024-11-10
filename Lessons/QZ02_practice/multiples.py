def multiples(nums: list[int]) -> list[bool]:
    bool_list: list[bool] = []
    # occurs: int = 0
    index: int = 0
    last_num: int = nums[len(nums) - 1]

    if index == 0 and nums[index] % last_num == 0:
        bool_list.append(True)
    else:
        bool_list.append(False)

    index = 1
    while index < len(nums):
        if nums[index] % nums[index - 1] == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
        index += 1
    return bool_list


print(multiples([2, 3, 4, 8, 16, 2, 4, 2]))
