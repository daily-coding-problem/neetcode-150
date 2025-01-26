# https://neetcode.io/problems/two-integer-sum-ii

import unittest
from typing import List

# This approach works because we are told that `nums` is sorted
# If the array was not sorted, we would have to sort it first, and
# incur a O(n log n) time complexity.


def two_sum_II(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    left = 0
    right = n - 1

    result = []

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum < target:
            left += 1
            continue

        if current_sum > target:
            right -= 1
            continue

        # Assume current sum = target

        return [left + 1, right + 1]

    return result


class Test(unittest.TestCase):
    def test_two_sum_II(self):
        self.assertEqual(two_sum_II([1, 2, 3, 4], 3), [1, 2])
