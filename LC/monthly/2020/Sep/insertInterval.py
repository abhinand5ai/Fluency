class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = []
        while intervals:
            s,e = newInterval
            nS,nE = intervals[0]
            if e < nS:
                return inserted + [newInterval] + intervals
            elif nS <= s <= e <= nE:
                return inserted + intervals
            elif nE < s:
                inserted.append(intervals.pop(0))
            else :
                newInterval = [min(s,nS), max(e,nE)]
                intervals.pop(0)
        return inserted + [newInterval]
            


            


