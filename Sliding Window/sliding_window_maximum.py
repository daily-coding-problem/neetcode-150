# https://neetcode.io/problems/sliding-window-maximum

import unittest
from typing import List
import heapq


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    result = []
    heap = []

    for i, num in enumerate(nums):
        heapq.heappush(heap, (-num, i))  # Add number to the current window maximum

        if i >= k - 1:  # Did we fall outside the window?
            while heap[0][1] <= i - k:  # Shrink the window
                heapq.heappop(heap)

            result.append(
                -heap[0][0]
            )  # Add the current maximum in the window to the result

    return result


class Test(unittest.TestCase):
    def test_max_sliding_window(self):
        self.assertEqual(max_sliding_window([1, 2, 1, 0, 4, 2, 6], 3), [2, 2, 4, 4, 6])
