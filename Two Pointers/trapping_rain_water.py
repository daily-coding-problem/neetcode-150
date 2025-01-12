# https://neetcode.io/problems/trapping-rain-water

import unittest
from typing import List

def trap(heights: List[int]) -> int:
    n = len(heights)

    result = 0

    left = 0
    right = n - 1

    max_left_height = heights[left]
    max_right_height = heights[right]

    while left < right:
        if max_left_height < max_right_height:
            left += 1

            max_left_height = max(max_left_height, heights[left])
            result += max_left_height - heights[left]
            continue

        right -= 1
        max_right_height = max(max_right_height, heights[right])
        result += max_right_height - heights[right]

    return result

class Test(unittest.TestCase):
    def test_trap(self):
        self.assertEqual(trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]), 9)
