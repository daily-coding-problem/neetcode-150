# https://neetcode.io/problems/string-encode-and-decode

import unittest
from typing import List

def encode(words: List[str]) -> str:
    encoded_words = []

    for word in words:
        encoded_word = str(len(word)) + "#" + word
        encoded_words.append(encoded_word)

    return ' '.join(encoded_words)

def decode(encoded_words: str) -> List[str]:
    n = len(encoded_words)
    decoded_words = []
    i = 0

    while i < n:
        j = i
        # Find the position of the next '#'
        while j < n and encoded_words[j] != '#':
            j += 1

        # If no '#' is found, break the loop to avoid infinite loop
        if j == n:
            break

        # Try to convert the substring to an integer
        try:
            length = int(encoded_words[i:j])
        except ValueError:
            raise ValueError(f"Invalid length found: {encoded_words[i:j]}")

        # Move i to the start of the actual word
        i = j + 1
        j = i + length

        # Check if the end of the word is within bounds
        if j > n:
            raise ValueError(f"Word length {length} is out of bounds for the string: {encoded_words[i:]}")

        decoded_word = encoded_words[i:j]
        decoded_words.append(decoded_word)

        # Move i to the start of the next length
        i = j

    return decoded_words

class Test(unittest.TestCase):
    def setUp(self):
        self.example1 = ["neet","code","love","you"]
        self.example2 = ["we","say",":","yes"]

        self.expected_encoding1 = '4#neet 4#code 4#love 3#you'
        self.expected_encoding2 = '2#we 3#say 1#: 3#yes'

    def test_encode(self):

        self.assertEqual(encode(self.example1), self.expected_encoding1)
        self.assertEqual(encode(self.example2), self.expected_encoding2)

    def test_decode(self):
        self.assertEqual(decode(self.expected_encoding1), self.example1)
        self.assertEqual(decode(self.expected_encoding2), self.example2)
