# https://neetcode.io/problems/longest-substring-without-duplicates

import unittest

def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    result = 0

    for right, char in enumerate(s):
        # Continuously remove leftmost characters from seen and move
        # the left pointer forward whenever a duplicate is encountered

        while char in seen:
            seen.remove(s[left]) # Remove the leftmost character
            left += 1 # Shrink the window until the duplicate is removed
            continue

        seen.add(char)

        # Update the result with the current size of the window
        result = max(result, right - left + 1)

    return result

class Test(unittest.TestCase):
    def test_length_of_longest_substring(self):
        self.assertEqual(length_of_longest_substring("zxyzxyz"), 3)
        self.assertEqual(length_of_longest_substring("xxxx"), 1)
