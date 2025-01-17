# https://neetcode.io/problems/longest-consecutive-sequence

import unittest
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if (num - 1) not in nums_set:  # Are we are the start of a sequence?
            length = 1

            while (num + length) in nums_set:
                length += 1

            longest = max(longest, length)

    return longest


class Test(unittest.TestCase):
    def test_longest_consecutive(self):
        self.assertEqual(longest_consecutive([2, 20, 4, 10, 3, 4, 5]), 4)
        self.assertEqual(longest_consecutive([0, 3, 2, 5, 4, 6, 1, 1]), 7)
