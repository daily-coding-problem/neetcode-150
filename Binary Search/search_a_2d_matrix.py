# https://neetcode.io/problems/search-2d-matrix

import unittest
from typing import List

# 'bisect_left' can be used here, but requires flattening the matrix first
# from bisect import bisect_left
#
# def search_matrix(matrix: List[List[int]], target: int) -> bool:
#     if not matrix or not matrix[0]:
#         return False
#
#     # Flatten the matrix
#     flat_list = [element for row in matrix for element in row]
#
#     # Use bisect_left to find the insertion point
#     index = bisect_left(flat_list, target)
#
#     # Check if the target is actually at the found index
#     return index < len(flat_list) and flat_list[index] == target


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])

    rows = n
    cols = m

    left = 0
    right = (rows * cols) - 1

    while left <= right:
        mid = (left + right) // 2

        row = mid // rows
        col = mid // cols

        if matrix[row][col] == target:
            return True

        if matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


class Test(unittest.TestCase):
    def test_search_matrix(self):
        self.assertTrue(
            search_matrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10)
        )
        self.assertFalse(
            search_matrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15)
        )
