from functools import cache


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def maxScore(j, rem):
            if j == n:
                return 0
            else:
                return max(maxScore(j + 1, rem), prices[j] + best(j + 1, rem))

        @cache
        def best(i, rem):
            if i >= n - 1 or rem <= 0:
                return 0

            bst = max(best(i + 1, rem), maxScore(i + 1, rem - 1) - prices[i])
            return bst

        return best(0, k)