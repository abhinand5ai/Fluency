from typing import List

class Solution:
#     def rob(self, nums: List[int]) -> int:
#         print(nums)
#         n = len(nums)
#         if n < 2:
#             return max(nums)
# 
#         def circled(j, start):
#             return j % n  in [start, (start - 1) % n]
# 
#         def maxRob(i, start):
#             a, b = 0, nums[i % n]
#             if not circled(i + 1, start):
#                 a = maxRob(i + 1, start)
# 
#             if not circled(i + 2, start):
#                 b = maxRob(i + 2, start) + nums[i % n]
# 
#             return max(a, b)
# 
# 
#         return max( maxRob(x, x) for x in range(n))

class Solution



def main():
    houses = [2,3,2]
    sol = Solution()
    stash = sol.rob(houses)
    print(stash)


if __name__ == '__main__':
    main()
