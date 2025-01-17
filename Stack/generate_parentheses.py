# https://neetcode.io/problems/generate-parentheses

import unittest
from typing import List


def generate_parentheses(n: int) -> List[str]:
    result = []
    stack = []

    def backtrack(open_count, close_count):
        if open_count == close_count == n:
            return result.append("".join(stack))

        if open_count < n:
            stack.append("(")
            backtrack(open_count + 1, close_count)
            stack.pop()

        if close_count < open_count:
            stack.append(")")
            backtrack(open_count, close_count + 1)
            stack.pop()

    backtrack(0, 0)

    return result


class Test(unittest.TestCase):
    def test_generate_parentheses(self):
        self.assertEqual(generate_parentheses(1), ["()"])
        self.assertEqual(
            generate_parentheses(3), ["((()))", "(()())", "(())()", "()(())", "()()()"]
        )
