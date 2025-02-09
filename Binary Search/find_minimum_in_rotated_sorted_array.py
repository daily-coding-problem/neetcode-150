# https://neetcode.io/problems/find-minimum-in-rotated-sorted-array

from typing import List

import unittest


def find_min(nums: List[int]) -> int:
    n = len(nums)

    left = 0
    right = n - 1

    while left < right:
        mid = (right + left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


class Test(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(find_min([11, 13, 15, 17]), 11)
