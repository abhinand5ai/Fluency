# code
from typing import List


class Solution:
    def kthElement(k: int, array: List[int]):
        def partition():
            pass


testCases = int(input())

for _ in range(testCases):
    sol: Solution = Solution()
    n = int(input())
    array = list(map(int, input().split()))
    k = int(input())
    print(sol.kthElement(k, array))
