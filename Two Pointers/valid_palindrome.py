# https://neetcode.io/problems/is-palindrome

import unittest


def is_palindrome(sentence: str) -> bool:
    n = len(sentence)

    left = 0
    right = n - 1

    while left <= right:
        left_character = sentence[left]
        right_character = sentence[right]

        if left_character == " " or not left_character.isalnum():
            left += 1
            continue

        if right_character == " " or not right_character.isalnum():
            right -= 1
            continue

        if left_character.lower() != right_character.lower():
            return False

        left += 1
        right -= 1

    return True


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertFalse(is_palindrome("tab a cat"))
