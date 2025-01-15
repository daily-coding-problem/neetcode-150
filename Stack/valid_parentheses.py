# https://neetcode.io/problems/validate-parentheses

import unittest

def is_valid(s: str) -> bool:
    closing = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        is_closing = char in closing

        if is_closing and (stack and stack[-1] == closing[char]):
            stack.pop()
            continue

        if is_closing and not stack:
            return False

        stack.append(char)

    return len(stack) == 0

class Test(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(is_valid('[]'))
        self.assertTrue(is_valid('([{}])'))
        self.assertFalse(is_valid('[(])'))
        self.assertFalse(is_valid(']'))
