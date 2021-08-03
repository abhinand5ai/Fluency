from functools import cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @cache
        def maxScore(j):
            if j == n:
                return 0
            return max(maxScore(j + 1), prices[j] - fee + maxProfit(j + 1) )
        @cache
        def maxProfit(i):
            if i >= n -1:
                return 0
            return max(maxProfit(i + 1), maxScore(i + 1) - prices[i])
        return maxProfit(0)



class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        mSold = 0
        mHold = -prices[0]
        for price in prices[1:]:
            mSold = max(mHold + price - fee, mSold)
            mHold = max(mSold - price, mHold)
        return mSold
        
        
        