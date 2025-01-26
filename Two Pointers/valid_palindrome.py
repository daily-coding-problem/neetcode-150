# https://neetcode.io/problems/is-palindrome

# `isalnum()` method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# `isalpha()` method returns True if all the characters are alphabet letters (a-z).
# `isdigit()` method returns True if all the characters are digits (0-9).
# `islower()` method returns True if all the characters are in lower case.

# Therefore, for this problem, we can use `isalnum()` to check if the character is an alphabet letter or a number.
# However, if we are asked to implement `isalnum()` method, we can use the following code:

# def is_alnum(character: str) -> bool:
#     return (
#          ord('A') <= ord(character) <= ord('Z') or
#          ord('a') <= ord(character) <= ord('z') or
#          ord('0') <= ord(character) <= ord('9')
#    )

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
        self.assertFalse(is_palindrome("0P"))
