# https://neetcode.io/problems/time-based-key-value-store

import unittest


class TimeMap:
    def __init__(self):
        self.history = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.history:
            self.history[key] = []

        self.history[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""  # Most recent value for given timestamp
        values = self.history.get(key, [])

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            prev_timestamp = values[mid][1]

            if prev_timestamp <= timestamp:
                result = values[mid][0]

                left = mid + 1
            else:
                right = mid - 1

        return result


class TestTimeMap(unittest.TestCase):
    def setUp(self):
        self.time_map = TimeMap()

    def test_set_and_get_single_value(self):
        self.time_map.set("foo", "bar", 1)
        self.assertEqual(self.time_map.get("foo", 1), "bar")

    def test_get_most_recent_value(self):
        self.time_map.set("foo", "bar", 1)
        self.time_map.set("foo", "bar2", 2)
        self.assertEqual(self.time_map.get("foo", 2), "bar2")
        self.assertEqual(self.time_map.get("foo", 3), "bar2")

    def test_get_before_any_set_value(self):
        self.assertEqual(self.time_map.get("foo", 1), "")

    def test_key_with_multiple_values_and_timestamp(self):
        self.time_map.set("key1", "alpha", 1)
        self.time_map.set("key1", "beta", 3)
        self.time_map.set("key1", "gamma", 5)

        # Exact match for timestamps
        self.assertEqual(self.time_map.get("key1", 3), "beta")
        self.assertEqual(self.time_map.get("key1", 5), "gamma")

        # Fetching closest lower timestamp
        self.assertEqual(self.time_map.get("key1", 4), "beta")
        self.assertEqual(self.time_map.get("key1", 2), "alpha")

        # Fetching before the first timestamp
        self.assertEqual(self.time_map.get("key1", 0), "")

    def test_multiple_keys(self):
        self.time_map.set("foo", "bar", 1)
        self.time_map.set("baz", "qux", 2)
        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.assertEqual(self.time_map.get("baz", 2), "qux")
        self.assertEqual(self.time_map.get("baz", 1), "")
