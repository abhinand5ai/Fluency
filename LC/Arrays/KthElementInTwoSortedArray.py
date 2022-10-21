# code
import unittest
from typing import List


class Solution:
    def kthElement(self, k: int, smallerArray: List[int], largerArray: List[int]) -> int:
        m, n = len(smallerArray), len(largerArray)
        if m > n:
            m, n, smallerArray, largerArray = n, m, largerArray, smallerArray

        start = max(0, k - n - 1)
        end = min(k - 1, m - 1)
        while start <= end:
            s_i = (start + end) // 2
            l_i = k - s_i - 2
            if (l_i < 0 or largerArray[l_i] <= smallerArray[s_i]) and \
                    l_i + 1 < n and smallerArray[s_i] <= largerArray[l_i + 1]:
                return smallerArray[s_i]
            elif n > l_i >= 0 and largerArray[l_i] >= smallerArray[s_i] and \
                    (s_i >= m - 1 or largerArray[l_i] < smallerArray[s_i + 1]):
                return largerArray[l_i]
            elif l_i >= 0 and largerArray[l_i] > smallerArray[s_i]:
                start = s_i + 1
            else:
                end = s_i - 1
        if end == -1:
            return largerArray[k - 1]
        elif start == m:
            return largerArray[k - m - 1]
        return -1
        # testCases = int(input())


#
# for _ in range(testCases):
#     n, m, k = map(int, input().split())
#     l1 = list(map(int, input().split()))
#     l2 = list(map(int, input().split()))
#     print(kthElement(k, l1, l2))
#

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        self.assertEquals(5, self.sol.kthElement(5, [1, 2, 3, 4], [5, 6, 7, 8, 9]))
        self.assertEquals(5, self.sol.kthElement(5, [1, 2, 3, 5], [4, 6, 7, 8, 9]))
        self.assertEquals(11, self.sol.kthElement(11, [1, 2, 7, 8], [3, 4, 5, 6, 9, 10, 11, 12]))

    def test_one(self):
        a = "1 1 1 2 3 3 5 5 7 8 8 8 8 9 9 11 11 11 12 13 15 19 21 22 24 24 24 26 27 27 29 29 29 30 30 31 31 34 34 38 38 40 41 42 43 45 45 45 45 46 47 47 48 49 49 51 51 52 52 54 56 56 57 58 58 59 59 59 60 61 62 63 66 70 72 73 73 76 79 79 79 80 82 83 83 84 84 85 86 86 87 87 88 89 90 90 93 94 95".split()
        a = list(map(int, a))
        b = [38, 42, 43, 50, 51, 57]
        self.assertEquals(5, self.sol.kthElement(7, a, b))
