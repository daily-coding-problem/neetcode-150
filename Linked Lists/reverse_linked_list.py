# https://neetcode.io/problems/reverse-a-linked-list

from typing import Optional

import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current:
        next_node = current.next

        current.next = prev

        prev = current
        current = next_node

    return prev


class Test(unittest.TestCase):
    def test_reverse_linked_list(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        reversed_head = reverse_linked_list(head)

        self.assertEqual(reversed_head.val, 5)
        self.assertEqual(reversed_head.next.val, 4)
        self.assertEqual(reversed_head.next.next.val, 3)
        self.assertEqual(reversed_head.next.next.next.val, 2)
        self.assertEqual(reversed_head.next.next.next.next.val, 1)
        self.assertIsNone(reversed_head.next.next.next.next.next)
