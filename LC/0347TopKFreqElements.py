import random
from collections import Counter
from typing import List

def swpFunc(arr):
    def swp(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    return swp


def partitionFunc(arr):
    swp = swpFunc(arr)

    def partition(start, end):
        pivot = random.randint(start, end)
        le, gt = start, end
        pv = arr[pivot]
        swp(start, pivot)
        while le < gt:
            if arr[gt] > pv:
                gt -= 1
            else:
                le += 1
                swp(le, gt)
        swp(start, le)
        return le
    return partition


def quickSelect(arr, k):
    start, end = 0, len(arr) - 1
    partition = partitionFunc(arr)
    while True:
        p = partition(start, end)
        if k == p:
            return
        elif k < p:
            end = p - 1
        else:
            start = p + 1


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        arr = [(v, k) for k, v in ct.items()]
        quickSelect(arr, len(arr) - k)
        return [k for v, k in arr[-k:]]
