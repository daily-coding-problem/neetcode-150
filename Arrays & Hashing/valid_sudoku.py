# https://neetcode.io/problems/valid-sudoku

import unittest
from typing import List
from collections import defaultdict


def is_valid_sudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for row in range(9):
        for col in range(9):
            cell = board[row][col]

            if cell == ".":  # Skip empty cells
                continue

            if (
                cell in rows[row]
                or cell in cols[col]
                or cell in squares[(row // 3, col // 3)]
            ):
                return False

            rows[row].add(cell)
            cols[col].add(cell)
            squares[(row // 3, col // 3)].add(cell)

    return True


class Test(unittest.TestCase):
    def test_is_valid_sudoku(self):
        self.assertTrue(
            is_valid_sudoku(
                [
                    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", ".", ".", ".", ".", ".", "2", ".", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
        )
        self.assertFalse(
            is_valid_sudoku(
                [
                    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", ".", ".", ".", ".", ".", "2", ".", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
        )
