# https://neetcode.io/problems/merge-two-sorted-linked-lists

from typing import Optional

import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    sentinel = ListNode()
    current = sentinel

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # Attach remaining portion of list1 or list2
    current.next = list1 or list2

    return sentinel.next


class Test(unittest.TestCase):
    def test_mergeTwoLists(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))

        result = merge_two_lists(list1, list2)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.val, 4)
