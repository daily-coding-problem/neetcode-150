# https://neetcode.io/problems/find-duplicate-integer

import unittest


def find_duplicate(nums: list[int]) -> int:
    # Use Floyd's Tortoise and Hare algorithm to detect cycles.
    # This algorithm is used here to find the duplicate number in the list.
    # The problem guarantees that there is exactly one duplicate number.

    # Initialize both pointers to the start of the list.
    slow = nums[0]
    fast = nums[0]

    # Phase 1: Finding the intersection point of the two pointers.
    # Move 'slow' by one step and 'fast' by two steps until they meet.
    # Since there is a duplicate, a cycle must exist, and they will meet inside the cycle.
    while True:
        slow = nums[slow]  # Move slow pointer by one step.
        fast = nums[nums[fast]]  # Move fast pointer by two steps.

        if slow == fast:
            # Pointers have met, indicating a cycle.
            break

    # Phase 2: Finding the entrance to the cycle,
    # which is the duplicate number.
    slow = nums[0]  # Move slow pointer back to the start of the list.

    # Move both pointers at the same speed until they meet again.
    # The meeting point is the start of the cycle, i.e., the duplicate number.
    while slow != fast:
        slow = nums[slow]  # Move slow pointer by one step.
        fast = nums[fast]  # Move fast pointer by one step.

    return slow  # The duplicate number.


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_duplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(find_duplicate([3, 1, 3, 4, 2]), 3)
        self.assertEqual(find_duplicate([1, 1]), 1)
        self.assertEqual(find_duplicate([1, 1, 2]), 1)
