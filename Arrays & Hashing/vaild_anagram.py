# https://neetcode.io/problems/is-anagram

import unittest

def is_anagram(s: str, t: str) -> bool:
    n = len(s)
    m = len(t)

    if n != m:
        return False

    seen = {}

    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for char in t:
        if char in seen:
            seen[char] -= 1
        else:
            return False

    for value in seen.values():
        if value != 0:
            return False

    return True

class Test(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram("racecar", "carrace"))
        self.assertFalse(is_anagram("jar", "jam"))
