class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = None
        for curr,nxt in zip(prices[:-1],prices[1:]):
            if nxt > curr:
                prof += nxt - curr
        return prof