# https://neetcode.io/problems/minimum-stack

import unittest


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        value = min(value, self.min_stack[-1] if self.min_stack else value)
        self.min_stack.append(value)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

        if self.min_stack:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack()

    def test_push(self):
        self.min_stack.push(3)
        self.assertEqual(self.min_stack.top(), 3)
        self.assertEqual(self.min_stack.get_min(), 3)

        self.min_stack.push(5)
        self.assertEqual(self.min_stack.top(), 5)
        self.assertEqual(self.min_stack.get_min(), 3)

        self.min_stack.push(2)
        self.assertEqual(self.min_stack.top(), 2)
        self.assertEqual(self.min_stack.get_min(), 2)

        self.min_stack.push(2)
        self.assertEqual(self.min_stack.top(), 2)
        self.assertEqual(self.min_stack.get_min(), 2)

        self.min_stack.push(1)
        self.assertEqual(self.min_stack.top(), 1)
        self.assertEqual(self.min_stack.get_min(), 1)

    def test_pop(self):
        self.min_stack.push(3)
        self.min_stack.push(5)
        self.min_stack.push(2)
        self.min_stack.push(2)
        self.min_stack.push(1)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 2)
        self.assertEqual(self.min_stack.get_min(), 2)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 2)
        self.assertEqual(self.min_stack.get_min(), 2)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 5)
        self.assertEqual(self.min_stack.get_min(), 3)

        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 3)
        self.assertEqual(self.min_stack.get_min(), 3)

    def test_top(self):
        self.min_stack.push(3)
        self.assertEqual(self.min_stack.top(), 3)

        self.min_stack.push(5)
        self.assertEqual(self.min_stack.top(), 5)

    def test_get_min(self):
        self.min_stack.push(3)
        self.assertEqual(self.min_stack.get_min(), 3)

        self.min_stack.push(5)
        self.assertEqual(self.min_stack.get_min(), 3)

        self.min_stack.push(2)
        self.assertEqual(self.min_stack.get_min(), 2)

        self.min_stack.push(1)
        self.assertEqual(self.min_stack.get_min(), 1)
