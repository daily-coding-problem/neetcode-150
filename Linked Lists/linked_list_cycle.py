# https://neetcode.io/problems/linked-list-cycle-detection

from typing import Optional

import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


class Test(unittest.TestCase):
    def test_hasCycle(self):
        head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
        head.next.next.next.next = head.next

        self.assertTrue(has_cycle(head))

        head = ListNode(1, ListNode(2))
        head.next.next = head

        self.assertTrue(has_cycle(head))

        head = ListNode(1)

        self.assertFalse(has_cycle(head))

        head = ListNode(1, ListNode(2, ListNode(3)))

        self.assertFalse(has_cycle(head))
