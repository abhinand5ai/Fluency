import itertools
import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest_string: str = min(strs, key=len)
        for i in itertools.count():
            if i == len(shortest_string) or len(set(x[i] for x in strs)) != 1:
                return shortest_string[:i]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        self.assertEqual("fl", self.sol.longestCommonPrefix(["flower", "flow", "flight"]))
        self.assertEqual("", self.sol.longestCommonPrefix(["dog", "racecar", "car"]))
        self.assertEqual("ab", self.sol.longestCommonPrefix(["abacus", "abhinand", "above"]))
        self.assertEqual("", self.sol.longestCommonPrefix(["", "abhinand", "above"]))
        self.assertEqual("", self.sol.longestCommonPrefix([]))
        self.assertEqual("", self.sol.longestCommonPrefix(["", "", ""]))
