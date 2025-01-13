# https://neetcode.io/problems/permutation-string

import unittest
from collections import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)

    # It is impossible s2 has a permutation of n if
    # s1 is larger than s2
    if n > m:
        return False

    s1_count = Counter(s1)

    # count the frequency of characters in a window of size 'n'
    window_count = Counter(s2[:n])

    # Determine if the initial window matches 's1_count'
    if window_count == s1_count:
        return True

    for right in range(n, m): # Fixed window size of m - n
        left = right - n

        # Add new character to the window
        window_count[s2[right]] += 1

        # Remove the leftmost character from the window
        window_count[s2[left]] -= 1

        # Delete the leftmost character from 'window_count' if
        # its frequency reaches 0
        if window_count[s2[left]] == 0:
            del window_count[s2[left]]

        # Check if the current window matches 's1_count'
        if window_count == s1_count:
            return True

    return False

class Test(unittest.TestCase):
    def test_check_inclusion(self):
        self.assertTrue(check_inclusion("abc", "lecabee"))
        self.assertFalse(check_inclusion("abc", "lecaabee"))
