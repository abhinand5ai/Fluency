from typing import List
class Solution:
    def findBuildings(self, heights:List[int]) -> List[int]:
        n = len(heights)
        res = [n - 1]
        i = n - 2
        while i >= 0:
            if heights[i] > heights[res[-1]]:
                res.append(i)
            i -= 1

        res.reverse()
        return res
