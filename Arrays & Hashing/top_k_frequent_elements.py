# https://neetcode.io/problems/top-k-elements-in-list

import unittest
import heapq
from typing import List
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    n = len(nums)

    if k > n:
        return []

    counts = Counter(nums)

    min_heap = []

    for num, count in counts.items():
        heapq.heappush(min_heap, (-count, num)) # negate the count to convert min heap to max heap

    result = []

    for _ in range(k):
        _, num = heapq.heappop(min_heap)
        result.append(num)

    return result

class Test(unittest.TestCase):
    def test_top_k_frequent(self):
        self.assertEqual(top_k_frequent([1, 2, 2, 3, 3, 3], 2), [3, 2])
        self.assertEqual(top_k_frequent([7, 7], 1), [7])
