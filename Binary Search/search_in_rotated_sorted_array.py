# https://neetcode.io/problems/find-target-in-rotated-sorted-array

from typing import List

import unittest


def search(nums: List[int], target: int) -> int:
    n = len(nums)

    if n == 0:
        return -1

    left = 0
    right = n - 1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


class Test(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(search([1], 0), -1)
        self.assertEqual(search([1], 1), 0)
        self.assertEqual(search([1, 3], 3), 1)
        self.assertEqual(search([3, 1], 3), 0)
        self.assertEqual(search([3, 1], 1), 1)
        self.assertEqual(search([3, 1], 0), -1)
