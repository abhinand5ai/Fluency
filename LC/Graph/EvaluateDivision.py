import unittest
from collections import defaultdict
from typing import Set, List, Tuple


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        edgeValues = defaultdict
        for equation, value in zip(equations, values):
            n, d = equation
            graph[n].append((d, value))
            graph[d].append((n, 1 / value))

        def dfs(start: str, end: str, visited: Set[str]) -> Tuple[bool, float]:
            if start not in graph or end not in graph:
                return False, 0
            visited.add(start)
            if start == end:
                return True, 1.0
            else:
                for d, value in graph[start]:
                    if d in visited:
                        continue
                    found, pathValue = dfs(d, end, visited)
                    if found:
                        return found, value * pathValue
                return False, 0

        queryResults = [dfs(start, end, set()) for start, end in queries]
        return [value if found else -1.0 for found, value in queryResults]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        eq = [["a", "b"], ["b", "c"]]
        val = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        self.assertEqual([6.00000, 0.50000, -1.00000, 1.00000, -1.00000], self.sol.calcEquation(eq, val, queries))
