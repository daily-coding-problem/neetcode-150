# https://neetcode.io/problems/anagram-groups

import unittest
from typing import List
from collections import defaultdict


def group_anagrams(words: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for word in words:
        sorted_word = "".join(sorted(word))

        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
            continue

        anagram_groups[sorted_word].append(word)

    return [group for group in anagram_groups.values()]


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
