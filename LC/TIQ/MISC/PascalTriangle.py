import unittest
from typing import List


class PascalTriangle:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = [[] for i in range(num_rows)]
        triangle[0] = [1]
        for i in range(1, num_rows):
            triangle[i] = [1] + [triangle[i - 1][j] + triangle[i - 1][j - 1] for j in range(1, i)] + [1]
        return triangle


class TestPascalTriangle(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = PascalTriangle()

    def test_generate(self):
        self.assertEqual([
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ], self.sol.generate(5))

