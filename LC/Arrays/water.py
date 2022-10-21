import unittest
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0]) if m != 0 else -1
        if n < 0:
            return 0
        rMax = [[0] * n for _ in range(m)]
        bMax = [[0] * n for _ in range(m)]
        lMax = [[0] * n for _ in range(m)]
        tMax = [[0] * n for _ in range(m)]
        for i in range(m):
            currMax = 0
            for j in range(n):
                lMax[i][j] = currMax
                currMax = max(currMax, heightMap[i][j])

        for j in range(n):
            currMax = 0
            for i in range(m):
                tMax[i][j] = currMax
                currMax = max(currMax, heightMap[i][j])

        for i in range(m):
            currMax = 0
            for j in range(1, n + 1):
                rMax[i][n - j] = currMax
                currMax = max(currMax, heightMap[i][n - j])

        for j in range(n):
            currMax = 0
            for i in range(1, m + 1):
                bMax[m - i][j] = currMax
                currMax = max(currMax, heightMap[m - i][j])

        water = 0
        for i in range(m):
            for j in range(n):
                h, l, r, t, b = [x[i][j] for x in [heightMap, lMax, rMax, tMax, bMax]]
                wtr = min(l, r, t, b) - h
                if wtr > 0:
                    print(l, r, t, b, h, i, j, wtr)
                water += wtr if wtr > 0 else 0

        return water


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        input1 = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
        input2 = [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]
        # self.assertEquals(4, self.sol.trapRainWater(input1))
        self.assertEquals(14, self.sol.trapRainWater(input2))
