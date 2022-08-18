#!/usr/bin/python3
"""tests 0-island_perimeter.py"""
import unittest
island_perimeter = __import__('0-island_perimeter').island_perimeter


class TestIslandPerimeter(unittest.TestCase):
    """tests island_perimeter"""

    def test_island_perimeter(self):
        """tests island_perimeter"""
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        result = island_perimeter(grid)
        self.assertEqual(result, 16)
        print(f'result is equal : {result}')


if __name__ == '__main__':
    unittest.main()
