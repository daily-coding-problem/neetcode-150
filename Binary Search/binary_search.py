# https://neetcode.io/problems/binary-search

import unittest
from typing import List

# Python has a builtin binary search function: 'bisect_left'.
# The bisect_left function from Python's bisect module is used
# to find the insertion point for an element in a sorted list to
# maintain sorted order.
#
# from bisect import bisect_left
# def binary_search(nums: List[int], target: int) -> int:
#     # Find the index where target should be inserted
#     index = bisect_left(nums, target)
#
#     # Check if the target is actually present at the found index
#     if index != len(nums) and nums[index] == target:
#         return index
#
#     # If target is not present, return -1
#     return -1


def binary_search(nums: List[int], target: int) -> int:
    n = len(nums)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


class Test(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([-1, 0, 2, 4, 6, 8], 4), 3)
        self.assertEqual(binary_search([-1, 0, 2, 4, 6, 8], 3), -1)
