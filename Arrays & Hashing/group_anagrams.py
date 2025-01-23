# https://neetcode.io/problems/anagram-groups

import unittest
from typing import List
from collections import defaultdict


def group_anagrams(words: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for word in words:
        # Create a character frequency tuple
        char_count = [0] * 26  # Assuming only lowercase letters
        for char in word:
            char_count[ord(char) - ord("a")] += 1

        # Use the tuple of counts as the key
        key = tuple(char_count)
        anagram_groups[key].append(word)

    return list(anagram_groups.values())


class Test(unittest.TestCase):
    def assertEqualAnagramGroups(self, result, expected):
        # Sort each group and the outer list

        sorted_result = sorted([sorted(group) for group in result])
        sorted_expected = sorted([sorted(group) for group in expected])

        self.assertEqual(sorted_result, sorted_expected)

    def test_group_anagrams(self):
        self.assertEqualAnagramGroups(
            group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]),
            [["hat"], ["act", "cat"], ["stop", "pots", "tops"]],
        )
        self.assertEqualAnagramGroups(group_anagrams(["x"]), [["x"]])
        self.assertEqualAnagramGroups(group_anagrams([""]), [[""]])
