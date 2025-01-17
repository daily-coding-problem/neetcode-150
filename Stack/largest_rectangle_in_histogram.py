# https://neetcode.io/problems/largest-rectangle-in-histogram

import unittest
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    num_bars = len(heights)
    stack = []  # This stack will store tuples of (start_index, bar_height)
    max_area = 0  # Variable to keep track of the maximum area found

    for current_index, current_height in enumerate(heights):
        start_index = current_index  # Start index for the current bar

        # While stack is not empty and the current bar height is less
        # than the height of the bar at the top of the stack
        while stack and stack[-1][1] > current_height:
            popped_index, popped_height = stack.pop()  # Pop the top of the stack

            # Calculate the area with the popped height as the smallest height
            max_area = max(max_area, popped_height * (current_index - popped_index))

            start_index = popped_index  # Update start index to the popped index

        # Push the current bar onto the stack with its start index
        stack.append((start_index, current_height))

    # After processing all bars, compute area for remaining bars in the stack
    for start_index, bar_height in stack:
        # Calculate area with the remaining heights in the stack
        max_area = max(max_area, bar_height * (num_bars - start_index))

    return max_area


class Test(unittest.TestCase):
    def test_largest_rectangle_area(self):
        self.assertEqual(largest_rectangle_area([7, 1, 7, 2, 2, 4]), 8)
        self.assertEqual(largest_rectangle_area([1, 3, 7]), 7)
