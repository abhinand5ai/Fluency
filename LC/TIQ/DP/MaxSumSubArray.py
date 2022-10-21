import unittest
from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        curr_sum = 0
        for i in range(0, n):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_something(self):
        prices: List[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(6, self.sol.max_sub_array(prices))


if __name__ == '__main__':
    unittest.main()
