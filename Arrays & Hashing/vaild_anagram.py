# https://neetcode.io/problems/is-anagram

import unittest


def is_anagram(word_one: str, word_two: str) -> bool:
    n = len(word_one)
    m = len(word_two)

    if n != m:
        return False

    seen = {}

    for char in word_one:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for char in word_two:
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
