# https://neetcode.io/problems/daily-temperatures

import unittest
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    result = [0] * n
    seen_temperatures = []  # (temperature, index)

    for index, temperature in enumerate(temperatures):
        while seen_temperatures and temperature > seen_temperatures[-1][0]:
            seen_temperature, seen_index = seen_temperatures.pop()
            result[seen_index] = index - seen_index

        seen_temperatures.append((temperature, index))

    return result


class Test(unittest.TestCase):
    def test_daily_temperatures(self):
        self.assertEqual(
            daily_temperatures([30, 38, 30, 36, 35, 40, 28]), [1, 4, 1, 2, 1, 0, 0]
        )
        self.assertEqual(daily_temperatures([22, 21, 20]), [0, 0, 0])
