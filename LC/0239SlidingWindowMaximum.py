from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        qu = deque()
        res = []
        for i, v in enumerate(nums):
            while qu and v > nums[qu[-1]]:
                qu.pop()
            qu.append(i)
            while qu[0] <= i - k:
                qu.popleft()
            res.append(nums[qu[0]])

        return res[k - 1:]
