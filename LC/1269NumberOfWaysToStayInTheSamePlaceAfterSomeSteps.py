from functools import cache
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def numWays(i, k):
            # print(k, i)
            if i == 0 and k == 0:
                return 1
            if i < 0 or i == arrLen or k <= 0:
                return 0
            return (numWays(i + 1, k - 1) + numWays(i - 1, k - 1) + numWays(i, k - 1)) % 1_000_000_007

        return numWays(0, steps)