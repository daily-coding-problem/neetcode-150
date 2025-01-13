# https://neetcode.io/problems/longest-repeating-substring-with-replacement

import unittest

from collections import Counter

def character_replacement(s: str, k: int) -> int:
    counts = Counter(s)

    left = 0
    result = 0

    for right, char in enumerate(s):
        # Shrink the window when the current window size minus the count of the most
        # frequent character in the window exceeds k. This means we have more characters
        # to replace than allowed by k, so we need to move the left pointer to reduce
        # the window size.

        while (right - left + 1) - counts[char] > k:
            left += 1

        result = max(result, right - left + 1)

    return result

class Test(unittest.TestCase):
    def test_character_replacement(self):
        self.assertEqual(character_replacement("XYYX", 2), 4)
        self.assertEqual(character_replacement("AAABABB", 1), 5)
