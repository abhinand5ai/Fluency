from collections import defaultdict
from typing import List
import operator
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a1 = [(i,j)  for i,ls in enumerate(A) for j,val in enumerate(ls) if val == 1]
        b1 = [(i,j)  for i,ls in enumerate(B) for j,val in enumerate(ls) if val == 1]
        transformations = defaultdict(int)
        for rA,cA in a1:
            for rB,cB in b1:
                transformations[(rA -rB, cA -cB)] += 1 
        return max(transformations.values())
                
        
A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
sol = Solution()
print(sol.largestOverlap(A,B))
