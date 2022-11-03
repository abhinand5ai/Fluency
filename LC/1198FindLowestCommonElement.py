import bisect
from typing import List
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for x in mat[0]:
            found = 0
            for row in mat[1:]:
                loc = bisect.bisect_left(row, x)
                if loc < len(row) and row[loc] ==x:
                    found += 1
            if found == len(mat) - 1:
                return x
        return -1