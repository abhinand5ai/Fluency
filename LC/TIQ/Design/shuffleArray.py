from typing import List
from random import randrange


class Solution:

    def __init__(self, nums: List[int]):
        self.array: List[int] = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.array.copy()

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.array)
        shuffled_array = self.array.copy()
        for i in range(n):
            swap_index = randrange(i, n)
            shuffled_array[i], shuffled_array[swap_index] = shuffled_array[swap_index], shuffled_array[i]

        return shuffled_array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
