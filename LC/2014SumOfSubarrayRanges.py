from operator import lt, gt, le, ge


class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        def previous(comparison, arr):
            stk = []
            prev = []
            nxt = [len(arr)] * len(arr)
            for j, v in enumerate(arr):
                while stk and not comparison(arr[stk[-1]], v):
                    nxt[stk.pop()] = j
                prev.append(stk[-1] if stk else -1)
                stk.append(j)
            return prev, nxt

        previous_greater, next_greater_equal = previous(gt, nums)
        previous_smaller, next_smaller_equal = previous(lt, nums)

        # print(nums, "\n")
        # print(f"{previous_greater=}")
        # print(f"{next_smaller_equal=}")
        #
        # print(f"{previous_smaller=}")
        # print(f"{next_greater_equal=}")

        sm = 0
        for i, (pg, ps, nge, nse) in enumerate(
                zip(previous_greater, previous_smaller, next_greater_equal, next_smaller_equal)):
            numGreater = (i - pg) * (nge - i)
            numSmaller = (i - ps) * (nse - i)
            sm += (numGreater - numSmaller) * nums[i]

        return sm


def main():
    sol = Solution()
    sumSub = sol.subArrayRanges([4, -2, -3, 4, 1])
    print(sumSub)


if __name__ == '__main__':
    main()
