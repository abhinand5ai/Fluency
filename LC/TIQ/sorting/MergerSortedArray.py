import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = m + n - 1
        while start >= 0 and n > 0:
            if m - 1 < 0 or nums1[m - 1] < nums2[n - 1]:
                nums1[start] = nums2[n - 1]
                n -= 1
            else:
                nums1[start] = nums1[m - 1]
                m -= 1
            start -= 1


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_something(self):
        a = [1, 2, 3, 3, 0, 0, 0]
        b = [2, 5, 6]
        self.sol.merge(a, 4, b, 3)
        self.assertEqual([1, 2, 2, 3, 3, 5, 6], a)
        a = [0]
        b = [6]
        self.sol.merge(a, 0, b, 1)
        self.assertEqual([6], a)


if __name__ == '__main__':
    unittest.main()
