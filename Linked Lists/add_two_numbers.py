# https://neetcode.io/problems/add-two-numbers

from typing import Optional

import unittest

# We can use `divmod` to get the quotient and the remainder of the division
# see https://docs.python.org/3/library/functions.html#divmod
# Doing it by hand:
# new_digit = a + b + carry
# carry = new_digit // 10
# new_digit %= 10


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    sentinel = ListNode()
    current = sentinel

    carry = 0

    while l1 or l2 or carry:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0

        carry, new_digit = divmod(a + b + carry, 10)

        current.next = ListNode(new_digit)

        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return sentinel.next


class Test(unittest.TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        self.assertEqual(add_two_numbers(l1, l2).val, 7)
        self.assertEqual(add_two_numbers(l1, l2).next.val, 0)
        self.assertEqual(add_two_numbers(l1, l2).next.next.val, 8)
