class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low, hi = 0, len(nums)
        while low < hi:
            mid = (low + hi) // 2
            if nums[mid + 1] < nums[mid]:
                hi = mid
            else:
                low = mid + 1
        return low


def main():
    sol = Solution()
    index = sol.findPeakElement([1, 2, 3, 1])
    print(index == 2)


if __name__ == '__main__':
    main()
