class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2
            if nums[l] > nums[m] and nums[r] > nums[m]:
                r = m
            else:
                l = m + 1
        return r    

def main():
    sol = Solution()
    nums = [9,10,11,0,1,2,4,5,6,7,8]
    target = 0
    res = sol.search(nums, target)
    print(res)


if __name__ == '__main__':
    main()