from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[0])
        remaining = [intervals.pop(0)]
        while intervals:
            p_s,p_e = remaining[-1]
            s,e = intervals.pop(0)
            if p_s < s <= e <= p_e:
                continue
            if p_s == s:
                remaining.pop()
                remaining.append([s, max(e,p_e)])
            else:
                remaining.append([s,e])
        return len(remaining)

