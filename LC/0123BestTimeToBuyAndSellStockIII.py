class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 2
        @cache
        def maxScore(j, rem):
            if j == n:
                return 0
            else:
                return max(maxScore(j + 1, rem), prices[j] + best(j + 1, rem))
        @cache
        def best(i, rem):
            if i >= n-1 or rem <= 0:
                return 0
            
            bst = max(best(i + 1,rem), maxScore(i + 1,rem - 1) - prices[i])
            return bst
        
        return best(0,k)
    

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mLR = [0]*n
        mRL = [0]*n
        mn = prices[0]
        mx = prices[-1]
        for i in range(1,n):
            mn = min(mn, prices[i])
            mx = max(mx, prices[n - i - 1])
            mLR[i] = max(mLR[i - 1], prices[i] - mn)
            mRL[n - i - 1] = max(mRL[n - i], mx - prices[n - i - 1])
            # print(mRL)
        res = 0
        for i in range(n-1):
            res = max(res, mLR[i] + mRL[i + 1])
        # print(mLR)
        # print(mRL)
        return max(res,mLR[-1])