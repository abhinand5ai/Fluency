class Solution:
    def missingNumber(self, nums: list[int], k) -> int:
        nums += [None] * k
        n = len(nums)
        i = 0
        j = 1
        tmp = None
        while j < n:
            print(nums)
            if i is None or nums[i] == i:
                i = j
                j += 1
            else:
                nxt_i = nums[i]
                nums[i], tmp = tmp, nums[i]
                i = nxt_i

        return [i for i, v in enumerate(nums) if v is None]


def main():
    sol = Solution()
    res = sol.missingNumber([0, 4, 3, 1], 2)
    print(res)


if __name__ == "__main__":
    main()
