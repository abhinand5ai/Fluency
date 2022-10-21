import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visitAndMarkNewNeighbours(x, y, gridVisit, m, n):
            if not(0 <= x < m and 0 <= y < n):
                return
            if grid[x][y] == "0" or gridVisit[x][y]:
                return
            gridVisit[x][y] = True
            visitAndMarkNewNeighbours(x + 1, y, gridVisit, m, n)
            visitAndMarkNewNeighbours(x, y + 1, gridVisit, m, n)
            visitAndMarkNewNeighbours(x - 1, y, gridVisit, m, n)
            visitAndMarkNewNeighbours(x, y - 1, gridVisit, m, n)
            return

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        gridVisit = [[False for i in range(n)] for j in range(m)]
        setCount = 0
        for i in range(m):
            for j in range(n):
                x, y = i, j
                if grid[x][y] == "0" or gridVisit[x][y]:
                    continue
                visitAndMarkNewNeighbours(x, y, gridVisit, m, n)
                setCount += 1
        return setCount


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        input = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
        self.assertEqual(1, self.sol.numIslands(input))


if __name__ == '__main__':
    unittest.main()
