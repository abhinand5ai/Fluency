import unittest
from functools import reduce
from typing import List, Tuple, Set
from collections import defaultdict


class Solution:
    def productExceptSelf(self, nums: List[int]):
        countZeros = sum((1 for num in nums if num == 0))
        if countZeros > 1:
            return [0] * len(nums)
        product = reduce(lambda x, y: x * y, (num for num in nums if num != 0))
        if countZeros == 1:
            return [0 if num != 0 else product for num in nums]
        if countZeros == 0:
            return [product // num for num in nums]

    def checkValidString(self, s: str) -> bool:
        lStack = []
        starLocations = []
        for i, c in enumerate(s):
            if c == '(':
                lStack.append(i)
            elif c == ')':
                if lStack:
                    lStack.pop()
                elif starLocations:
                    starLocations.pop()
                else:
                    return False
            else:
                starLocations.append(i)

        if not lStack:
            return True
        if len(starLocations) < len(lStack):
            return False
        else:
            li, si = 0, 0
            while li < len(lStack) and si < len(starLocations):
                if lStack[li] < starLocations[si]:
                    li += 1
                    si += 1
                else:
                    si += 1
            return li == len(lStack)

    def numIslands(self, grid: List[List[str]]) -> int:
        isLandCount = 0
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        def markNeighbours(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "V"
                neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for x, y in neighbours:
                    markNeighbours(x, y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    isLandCount += 1
                    markNeighbours(i, j)
        return isLandCount

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        dp = [[-1] * n for _ in range(m)]

        def computeMinPathSum(i, j):
            if dp[i][j] > 0:
                return dp[i][j]
            if i + 1 < m and j + 1 < n:
                dp[i][j] = grid[i][j] + \
                    min(computeMinPathSum(i + 1, j),
                        computeMinPathSum(i, j + 1))
            elif i + 1 < m:
                dp[i][j] = grid[i][j] + computeMinPathSum(i + 1, j)
            elif j + 1 < n:
                dp[i][j] = grid[i][j] + computeMinPathSum(i, j + 1)
            else:
                dp[i][j] = grid[i][j]
            return dp[i][j]

        return computeMinPathSum(0, 0)

    def isHappy(self, n: int) -> bool:
        def isHappy(n: int, history: Set[int]) -> bool:
            if n == 1:
                return True
            elif n in history:
                return False
            nextNum = 0
            history.add(n)
            while n != 0:
                nextNum = nextNum + ((n % 10) ** 2)
                n = n / 10
            return isHappy(nextNum, history)

        return isHappy(n, set())

    def numJewelsInStones(self, J: str, S: str) -> int:
        freq = defaultdict(lambda: 0)
        for s in S:
            freq[s] += 1
        return sum([freq[j] for j in J])


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        self.assertFalse(self.sol.checkValidString(
            "(())((())()()(*)(*()(())())())()()((()())((()))(*"
        ))

        self.assertFalse(self.sol.checkValidString(
            "(*(()))((())())*(**(()))((*)()(()))*(())()(())(()"
        ))
        self.assertFalse(self.sol.checkValidString(
            "(())((())()()(*)(*()(())())())()()((()())((()))(*"
        ))
