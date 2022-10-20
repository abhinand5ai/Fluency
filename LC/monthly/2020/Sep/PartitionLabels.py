from typing import List
from collections import defaultdict
from itertools import groupby
class Solution:
    def partitionLabels(self, S:str) -> List[int]:
        n = len(S)
        lastC = {c:i for i,c in enumerate(S)}
        maxLastSeen = 0
        prevIndex = -1
        partitions = []
        for i,c in enumerate(S):
            maxLastSeen = max(maxLastSeen,lastC[c])
            if maxLastSeen == i:
                partitions.append(i - prevIndex)
                prevIndex = i
        return partitions

         
sol = Solution()
partitions = sol.partitionLabels("ababcbacadefegdehijhklij")
print(partitions)