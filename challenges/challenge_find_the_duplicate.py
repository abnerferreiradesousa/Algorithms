from typing import List


def find_duplicate(nums: List[int]) -> int:
    """Faça o código aqui."""
    length = len(nums)
    if length == 1 or length == 0 or nums is None:
        return False

    index = 0
    nums.sort()

    [1, 3, 4, 5, 1]
    try:
        for num in nums:
            index += 1
            if isinstance(num, str) or num < 0:
                return False
            if num == nums[index]:
                    return num
    except IndexError:
        return False

    # Version one
    # if len(nums) == 1 or nums is None:
    #     return False

    # index = 1
    # nums.sort()

    # [1, 3, 4, 5, 1]

    # for num in nums:

    #     if isinstance(num, str) or num < 0:
    #         return False

    #     while (index < len(nums)):
    #         print(nums)
    #         print(f"{num} é igual {nums[index]}")

    #         if num == nums[index]:
    #             return num
    #         index += 1
    #     index = 1
    # return False