import random
from typing import List


class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        random.shuffle(arr)

        def swp(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def partition(start, end):
            # print(arr[start: end + 1])
            if start >= end:
                return
            pivot = random.randint(start, end)
            pv = arr[pivot]
            lt, eq, gt = start - 1, start - 1, end
            while eq < gt:
                if arr[gt] == pv:
                    eq += 1
                    swp(eq, gt)
                elif arr[gt] < pv:
                    eq += 1
                    swp(eq, gt)
                    lt += 1
                    swp(eq, lt)
                else:
                    gt -= 1

            partition(start, lt)
            partition(gt, end)

        partition(0, len(arr) - 1)

        return arr
