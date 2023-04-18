# You are given an integer array nums and two integers indexDiff and valueDiff.

# Find a pair of indices (i, j) such that:

# i != j,
# abs(i - j) <= indexDiff.
# abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        k = indexDiff + 1
        t = valueDiff + 1
        window = {}
        for i, num in enumerate(nums):
            if i - k - 1 >= 0:
                del window[nums[i - k - 1] // t]
            bucket = num // t
            if bucket in window:
                return True
            elif bucket - 1 in window and num - window[bucket - 1] <= valueDiff:
                return True
            elif bucket + 1 in window and window[bucket + 1] - num <= valueDiff:
                return True
            else:
                window[bucket] = num
        return False