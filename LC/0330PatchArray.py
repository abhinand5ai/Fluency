# Given a sorted integer array nums and an integer n, add/patch elements to the array
# such that any number in the range [1, n] inclusive can be formed by the sum of some
# elements in the array.

# Return the minimum number of patches required.

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums is sorted in ascending order.
# 1 <= n <= 2^31 - 1

class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        curr = 0
        j = 0
        num_patches = 0
        while curr < n:
            if j < len(nums) and nums[j] < curr + 2:
                curr += nums[j]
                j += 1
            else:
                curr += curr + 1
                num_patches += 1
        return num_patches


def main():
    sol = Solution()
    # v = sol.minPatches([1, 2, 16, 19, 31, 35, 36, 64, 64,
    #                    67, 69, 71, 73, 74, 76, 79, 80, 91, 95, 96, 97], 8)
    # print(v)
    v = sol.minPatches([1, 5, 10], 20)
    print(v)

    v = sol.minPatches([1, 2, 2], 5)
    print(v)


if __name__ == "__main__":
    main()
