# https://neetcode.io/problems/eating-bananas
import math
import unittest
from typing import List

def min_eating_speed(piles: List[int], hours: int) -> int:
    piles.sort()

    left =  1
    right = max(piles)
    
    result = right

    while left <= right:
        k = (left + right) // 2

        total_time = 0
        for pile in piles:
            total_time += math.ceil(float(pile) / k)

        if total_time <= hours:
            result = k
            right = k - 1
        else:
            left = k + 1

    return result

class Test(unittest.TestCase):
    def test_min_eating_speed(self):
        self.assertEqual(min_eating_speed([1, 4, 3, 2], 9), 2)
        self.assertEqual(min_eating_speed([25, 10, 23, 4], 4), 25)
