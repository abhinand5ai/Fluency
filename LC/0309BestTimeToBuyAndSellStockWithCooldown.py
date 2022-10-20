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


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #at each i, we have 3 states
        #1 has stock
        #2 no stock , cannot buy tmr,i.e. cooldown, we sold today
        #3 no stock,  can buy tmr
        #at i+1
        #1 -> 1' by doing nothing ; 3->1' by buying
        #1 -> 2' by selling
        #2 -> 3' by doing nothing ; 3->3' by doing nothing 
        #s_j[i] = max profit at day i in state j
        #max[s_2[n],s_3[n]] is what we want 
        n = len(prices)
        if n ==1 :
            return 0
        s_1 = [0 for i in range(0,n)]
        s_2 = [0 for i in range(0,n)]
        s_3 = [0 for i in range(0,n)]
        
        s_1[0] = -prices[0]
        s_2[0] = float("-inf")
        s_3[0] = 0
        for i in range(1,n):
            s_1[i] = max(s_1[i-1],s_3[i-1] - prices[i])
            s_2[i] = s_1[i-1] + prices[i] 
            s_3[i] = max(s_2[i-1],s_3[i-1])
        return max(s_2[-1],s_3[-1])