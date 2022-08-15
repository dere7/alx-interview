#!/usr/bin/python3
"""tests 0-island_perimeter.py"""
import unittest
island_perimeter = __import__('0-island_perimeter').island_perimeter


class TestIslandPerimeter(unittest.TestCase):
    """tests island_perimeter"""

    def test_island_perimeter(self):
        """tests island_perimeter"""
        grid = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(island_perimeter(grid), 12)


if __name__ == '__main__':
    unittest.main()
