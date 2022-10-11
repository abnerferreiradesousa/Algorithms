from typing import List


def find_duplicate(nums: List[int]) -> int:
    """Faça o código aqui."""

    # Case one
    # nums = [3, 1, 3, 4, 2]
    # saída: 3

    if len(nums) < 1:
        return False

    repeat_nums = []
    nums.sort()
    for num in nums:
        if num > 0:
            if num in repeat_nums:
                return num
            else:
                repeat_nums.append(num)
        else:
            return False
