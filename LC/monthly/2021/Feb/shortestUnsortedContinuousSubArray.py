class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = end = 0
        n = len(nums)