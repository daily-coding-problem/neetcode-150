# https://neetcode.io/problems/reorder-linked-list

from typing import Optional

import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    # Find middle of linked list

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Slow now points to the middle of the list
    second = slow.next
    previous = slow.next = None  # Detach the second half

    # Reverse

    while second:
        nxt = second.next

        second.next = previous
        previous = second

        second = nxt

    # Merge

    first = head
    second = previous

    while second:
        nxt1, nxt2 = first.next, second.next

        first.next = second
        second.next = nxt1

        first, second = nxt1, nxt2


class Test(unittest.TestCase):
    def test_reorderList(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)

        reorder_list(head)

        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 4)
        self.assertEqual(head.next.next.val, 2)
        self.assertEqual(head.next.next.next.val, 3)
