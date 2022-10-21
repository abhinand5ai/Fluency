class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        left = 0
        n = len(nums)
        prev = nums[0]
        while left < n - 1 and prev <= nums[left + 1]:
            left += 1

        right = n - 1
        prev = nums[right]

        while right > 0 and prev >= nums[right - 1]:
            right -= 1

        i, j = 0, right
        while i <= left and j < n:
            if nums[i] <= nums[j]:
                i += 1
            else:
                j += 1

        return j - i - 1
