from collections import deque

class MonotonicQueue:
    def __init__(self) -> None:
        self.queue = deque()



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        qu = deque()
        for i in range(k):
            if qu and qu[-1] > 

    