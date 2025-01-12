# https://neetcode.io/problems/duplicate-integer

import unittest
from typing import List

def has_duplicate(nums: List[int]) -> bool:
     seen = set()

     for num in nums:
            if num in seen:
                return True

            seen.add(num)

     return False

class Test(unittest.TestCase):
    def test_has_duplicate(self):
        self.assertEqual(has_duplicate([1, 2, 3, 1]), True)
        self.assertEqual(has_duplicate([1, 2, 3, 4]), False)
        self.assertEqual(has_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)

if __name__ == '__main__':
    unittest.main()
