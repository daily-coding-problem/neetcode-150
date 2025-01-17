# https://neetcode.io/problems/three-integer-sum

import unittest
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Pre-sort 'nums' to make it easier to skip duplicates and use two pointers

    n = len(nums)

    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate numbers
            continue

        result.extend(two_sum(nums, nums[i], i))

    return result


def two_sum(nums: List[int], current_num: int, index: int) -> List[List[int]]:
    n = len(nums)

    result = []

    left = index + 1
    right = n - 1

    while left < right:
        cumulative_sum = current_num + nums[left] + nums[right]

        if cumulative_sum < 0:
            left += 1
            continue

        if cumulative_sum > 0:
            right -= 1
            continue

        # Assume the cumulative sum is 0

        result.append([current_num, nums[left], nums[right]])

        # Skip duplicates for 'left' and 'right'
        while left < right and nums[left] == nums[left + 1]:
            left += 1

        while left < right and nums[right] == nums[right - 1]:
            right -= 1

        left += 1
        right -= 1

    return result


class Test(unittest.TestCase):
    def test_three_sum(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(three_sum([0, 1, 1]), [])
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])
