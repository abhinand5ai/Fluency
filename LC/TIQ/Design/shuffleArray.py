from typing import List
from random import randrange

import unittest


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums.copy()

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        num_copy = self.nums.copy()

        for i in range(len(num_copy)):
            num_copy[i], num_copy[randrange(i, len(num_copy))] = \
                num_copy[randrange(i, len(num_copy))], num_copy[i]
        return num_copy


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

class MyTestCase(unittest.TestCase):

    def test_something(self):
        prices: List[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        sol = Solution(prices)
        print(sol.shuffle())


if __name__ == '__main__':
    unittest.main()
