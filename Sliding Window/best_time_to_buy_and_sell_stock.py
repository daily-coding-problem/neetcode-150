# https://neetcode.io/problems/buy-and-sell-crypto

import unittest
from typing import List


def max_profit(prices: List[int]) -> int:
    result = 0
    min_price = float("inf")

    for price in prices:
        min_price = min(min_price, price)
        result = max(result, price - min_price)

    return result


class Test(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([10, 1, 5, 6, 7, 1]), 6)
        self.assertEqual(max_profit([10, 8, 7, 5, 2]), 0)
