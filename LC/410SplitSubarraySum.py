
# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.


 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

from functools import cache
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def minimize(i, k):
            if i == n and k != 1:
                return math.inf
            if k == 1:
                return sum(nums[i:])
            ret = math.inf
            sm = 0
            for j in range(i, n):
                sm += nums[j]
                subMin = minimize(j + 1, k - 1)
                ret = min(ret, max(sm, subMin))
                if sm >= subMin:
                    break

            return ret

        return minimize(0, k)
            

def main():
    sol = Solution()
    nums = [7,2,5,10,8]
    k = 2
    ans = sol.splitArray(nums, k)
    assert ans = 18

if __name__ == "__main__":
    main()



            
            
