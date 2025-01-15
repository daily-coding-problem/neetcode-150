# https://neetcode.io/problems/evaluate-reverse-polish-notation

import unittest
from typing import List

def evaluate_reverse_polish_notation(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token in '+-*/':
            # The values are in reverse order, so 'b' is first then 'a' due
            # to the order of stack operations
            b = stack.pop()
            a = stack.pop()

            # Perform the computation and push result back onto the stack

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(a // b)

            continue

        stack.append(int(token)) # Convert token to int and push into the stack

    return stack.pop() # The final result will be the only element left on the stack

class Test(unittest.TestCase):
    def test_evaluate_reverse_polish_notation(self):
        self.assertEqual(evaluate_reverse_polish_notation(["1", "2", "+", "3", "*", "4", "-"]), 5)
