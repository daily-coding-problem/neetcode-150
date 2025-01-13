# https://neetcode.io/problems/minimum-window-with-characters

import unittest
from collections import Counter, defaultdict


def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ''

    n = len(s)
    m = len(t)

    if m > n:
        return ''

    result = float('inf'), None, None # (window length, left, right)

    # Count characters in t
    t_counts = Counter(t)
    char_count_needed = m

    # Initialize window pointers and other variables
    left = 0
    matched_characters = 0
    window_counts = defaultdict(int)
    window = ''

    for right, char in enumerate(s):
        # Add one character from the right to the window
        window_counts[char] += 1
        window += char

        # If the current character's frequency matches the desired count in t
        if char in t_counts and window_counts[char] == t_counts[char]:
            matched_characters += 1

        # Try to shrink the window until it ceases to be 'desirable'
        while left <= right and matched_characters == char_count_needed:
            char = s[left]

            # Save the smallest window until now
            if right - left + 1 < result[0]:
                result = (right - left + 1), left, right

            # The character at the position by the 'left' pointer is no longer a part of the window
            window_counts[char] -= 1
            window = remove_leftmost_occurrence(window, char)
            if char in t_counts and window_counts[char] < t_counts[char]:
                matched_characters -= 1

            # Move the left pointer forward
            left += 1

    if result[0] == float('inf'):
        return ''

    # Build the result

    left = result[1]
    right = result[2]

    return s[left:right + 1]

def remove_leftmost_occurrence(s, char):
    # Find the position of the leftmost occurrence of the character
    index = s.find(char)

    # If the character is found, remove it using slicing
    if index != -1:
        # Return the string without the leftmost occurrence of the character
        return s[:index] + s[index + 1:]

    # If the character is not found, return the string unchanged
    return s

class Test(unittest.TestCase):
    def test_min_window(self):
        self.assertEqual(min_window("OUZODYXAZV", "XYZ"), "YXAZ")
        self.assertEqual(min_window("xyz", "xyz"), "xyz")
        self.assertEqual(min_window("x", "xy"), "")
