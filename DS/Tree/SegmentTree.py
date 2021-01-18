from typing import List


class SegmentTree:
    def __init__(self, val:List):
        self.val = val
        self.segment = [None] * (4*len(val))
        self.build()


    def build(self):
        def build(start:int, end:int, i: int):
            print(start,end, i)
            if start == end:
                self.segment[i] = self.val[start]
                return self.segment[i]

            middle =  (start + end)//2
            c1 = build(start, middle,2*i)
            c2 = build(middle + 1, end, 2*i + 1)
            self.segment[i] = c1 + c2
            return self.segment[i]
        build(0,len(self.val) - 1,1)
    
    def update(self, index, newVal):
        def update(node, start, end, i):
            if start == end :
                self.segment[i] = newVal
                return self.segment[i]
    
    def query(self, start, end):
        def query(sStart, sEnd, start, end, i):
            if sStart == start and sEnd == end:
                return self.segment[i]
            
            sMid = (sStart + sEnd) // 2
            if end < sMid:
                return query(sStart, sMid, start, end, 2*i)
            if start > sMid:
                return query(sMid + 1, sEnd, start, end, 2*i + 1)
            else:
                return query(sStart, sMid, start, sMid, 2*i) + query(sMid + 1, sEnd, sMid + 1, end, 2*i + 1)
            

             
        pass
    


segment = SegmentTree([1,3,5,7,9,11])

print(segment.segment)


