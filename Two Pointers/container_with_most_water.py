# https://neetcode.io/problems/max-water-container

import unittest
from typing import List

def max_area(heights: List[int]) -> int:
    n = len(heights)

    result = 0

    left = 0
    right = n - 1

    while left <= right:
        height = min(heights[left], heights[right])
        width = right - left

        result = max(result, height * width)

        # Move the pointer that points to the shorter line
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return result

class Test(unittest.TestCase):
    def test_max_area(self):
        self.assertEqual(max_area([1, 7, 2, 5, 4, 7, 3, 6]), 36)
        self.assertEqual(max_area([2, 2, 2]), 4)
