class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        prev = None
        freq = 0
        while True:
            if nums[i] == prev:
                :
