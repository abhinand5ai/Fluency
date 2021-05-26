from functools import cache, lru_cache


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        @lru_cache(maxsize=1)
        def maxScore(j):
            if j == n:
                return 0
            return max(prices[j] + maxProfit(j + 2), maxScore(j + 1))

        @lru_cache(maxsize=2)
        def maxProfit(i):
            if i >= n - 1:
                return 0
            maxGainFromI = maxScore(i + 1) - prices[i]
            return max(maxProfit(i + 1), maxGainFromI)

        return maxProfit(0)


class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        mx,p_mx,p_p_mx = 0,0,0
        s_mx = 0
        i = n -1
        while i >= 0:
            p_mx,p_p_mx = mx, p_mx
            mx = max(mx, s_mx - prices[i])
            s_mx = max(s_mx, p_p_mx + prices[i])
            i -= 1

        # print(dp)
        return mx