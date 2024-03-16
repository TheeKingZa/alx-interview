#!/usr/bin/python3
import unittest
from lockboxes import canUnlockAll

class TestCanUnlockAll(unittest.TestCase):
    def test_can_unlock_all_true(self):
        # Test cases where all boxes can be unlocked
        boxes1 = [[1], [2], [3], [4], []]
        self.assertTrue(canUnlockAll(boxes1))

        boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        self.assertTrue(canUnlockAll(boxes2))

    def test_can_unlock_all_false(self):
        # Test cases where not all boxes can be unlocked
        boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        self.assertFalse(canUnlockAll(boxes3))

        # Add more test cases for False scenarios if needed

if __name__ == '__main__':
    unittest.main()
