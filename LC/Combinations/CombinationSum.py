import unittest
from typing import List, Set


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinations(index: int, target: int, currResult: List[int], result: List[List[int]]) -> None:
            if (not (index < len(candidates))) or target < 0:
                return
            if target == 0:
                result.append([x for x in currResult])
                return

            currResult.append(candidates[index])
            combinations(index, target - candidates[index], currResult, result)
            currResult.pop()
            combinations(index + 1, target, currResult, result)

        result: List[List[int]] = []
        combinations(0, target, [], result)
        return result


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        # self.assertEqual(3.5, self.sol.findMedianSortedArrays([5, 6], [1, 2]))
        # self.assertEqual(2.5, self.sol.findMedianSortedArrays([1, 3], [2, 4]))
        # self.assertEqual(2, self.sol.findMedianSortedArrays([1, 3], [2]))
        # self.assertEqual(2, self.sol.findMedianSortedArrays([1, 3], []))
        self.assertEqual([
            [2, 2, 3],
            [7]
        ], self.sol.combinationSum([2, 3, 6, 7], 7))
