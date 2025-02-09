# https://neetcode.io/problems/remove-node-from-end-of-linked-list

from typing import Optional

import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def get_length(head: Optional[ListNode]):
        length: int = 0

        current: ListNode = head

        while current:
            length += 1

            current = current.next

        return length

    length: int = get_length(head)

    # When the node to remove is the `head` itself
    if length == n:
        return head.next

    target_index: int = length - n

    current: ListNode = head
    previous: ListNode = ListNode()
    count: int = 0

    while current:
        if count == target_index:
            previous.next = current.next
            break

        previous = current
        current = current.next

        count += 1

    return head


class Test(unittest.TestCase):
    def test_example(self):
        # Create the linked list 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        # Remove the 2nd node from the end, which is '4'
        new_head = remove_nth_from_end(head, 2)

        # Verify the new linked list is 1 -> 2 -> 3 -> 5
        self.assertEqual(new_head.val, 1)
        self.assertEqual(new_head.next.val, 2)
        self.assertEqual(new_head.next.next.val, 3)
        self.assertEqual(new_head.next.next.next.val, 5)
        self.assertIsNone(new_head.next.next.next.next)
