# https://neetcode.io/problems/two-integer-sum

import unittest
from typing import List
from collections import defaultdict


def two_sum(nums: List[int], target) -> List[int]:
    complements = defaultdict(int)

    for i, num in enumerate(nums):
        complement = target - num

        if complement in complements:
            return [complements[complement], i]

        complements[num] = i

    return []


class Test(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([3, 4, 5, 6], 7), [0, 1])
        self.assertEqual(two_sum([4, 5, 6], 10), [0, 2])
        self.assertEqual(two_sum([5, 5], 10), [0, 1])
