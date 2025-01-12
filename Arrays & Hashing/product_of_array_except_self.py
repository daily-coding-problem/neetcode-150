# https://neetcode.io/problems/products-of-array-discluding-self

import unittest
from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result

class Test(unittest.TestCase):
    def test_product_except_self(self):
        self.assertEqual(product_except_self([1, 2, 4, 6]), [48, 24, 12, 8])
        self.assertEqual(product_except_self([-1, 0, 1, 2, 3]), [0, -6, 0, 0, 0])
