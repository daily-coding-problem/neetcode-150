# https://neetcode.io/problems/car-fleet

import unittest
from typing import List

def car_fleet(target: int, positions: List[int], speeds: List[int]) -> int:
    # Create a list of tuples where each tuple contains a car's position and speed.
    cars = [(position, speed) for position, speed in zip(positions, speeds)]

    # Sort the cars by their starting positions in descending order.
    # This ensures that we process cars starting closest to the target first.
    # A car can only form a fleet with another car that is ahead of it,
    # so sorting by descending position helps in determining if a car will
    # catch up to another car in front of it.
    cars.sort(reverse=True)

    # Initialize a stack to keep track of the time each car fleet takes to reach the target.
    stack = []

    for position, speed in cars:
        # Calculate the time it takes for the current car to reach the target.
        time_to_target = (target - position) / speed
        # Push the time to the stack, representing a new fleet or an existing fleet's time.
        stack.append(time_to_target)

        # Check if the current car can catch up to the fleet in front of it.
        # If the current car's time is less than or equal to the fleet's time in front,
        # it means it will merge into the same fleet, so we remove it from the stack.
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    # The number of distinct times in the stack represents the number of car fleets.
    return len(stack)

class Test(unittest.TestCase):
    def test_car_fleet(self):
        self.assertEqual(car_fleet(10, [1, 4], [3, 2]), 1)
        self.assertEqual(car_fleet(10, [4, 1, 0, 7], [2, 2, 1, 1]), 3)
