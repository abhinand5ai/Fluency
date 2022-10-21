class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn  = prices[0]
        res = 0
        for price in prices:
            mn = min(mn, price)
            res = max(res, price - mn)
        return res