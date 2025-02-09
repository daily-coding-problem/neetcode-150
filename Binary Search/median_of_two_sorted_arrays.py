# https://neetcode.io/problems/median-of-two-sorted-arrays

import unittest
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2

    if len(B) < len(A):
        (
            A,
            B,
        ) = (
            B,
            A,
        )

    total = len(A) + len(B)
    half = total // 2

    left = 0
    right = len(A) - 1

    while True:
        i = (left + right) // 2  # A
        j = half - i - 2  # B

        a_left = A[i] if i >= 0 else float("-inf")
        a_right = A[i + 1] if i + 1 < len(A) else float("inf")

        b_left = B[j] if j >= 0 else float("-inf")
        b_right = B[j + 1] if j + 1 < len(B) else float("inf")

        # Did we find the correct partition?
        if a_left <= b_right and b_left <= a_right:
            # partition is of odd length
            if total % 2 == 1:
                return min(a_right, b_right)

            # partition is of even length
            return (max(a_left, b_left) + min(a_right, b_right)) / 2

        if a_left > b_right:
            right = i - 1
        else:
            left = i + 1


class Test(unittest.TestCase):
    def test_basic_case(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected_result = 2.0
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), expected_result)

    def test_even_total_length(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected_result = 2.5
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), expected_result)

    def test_one_empty_array(self):
        nums1 = []
        nums2 = [1]
        expected_result = 1.0
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), expected_result)

        nums1 = [2]
        nums2 = []
        expected_result = 2.0
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), expected_result)

    def test_single_element_each(self):
        nums1 = [1]
        nums2 = [2]
        expected_result = 1.5
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), expected_result)

    def test_large_unequal_arrays(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6, 7]
        expected_result = 4.0
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), expected_result)

    def test_identical_elements(self):
        nums1 = [2, 2, 2]
        nums2 = [2, 2]
        expected_result = 2.0
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), expected_result)

    def test_one_large_one_small(self):
        nums1 = [1, 2]
        nums2 = [3]
        expected_result = 2.0
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), expected_result)
