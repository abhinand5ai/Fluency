import random
import unittest


def swpFunc(arr):
    def swp(i, j): arr[i], arr[j] = arr[j], arr[i]
    return swp


def partitonTwoWayFunction(arr):
    swp = swpFunc(arr)

    def partition(start, end):
        assert start <= end
        pivot = start  # random.randint(start, end)
        pv = arr[pivot]
        swp(start, pivot)
        le = start
        gt = end
        while le < gt:
            if arr[gt] <= pv:
                le += 1
                swp(le, gt)
            else:
                gt -= 1

        swp(start, le)
        return le
    return partition


def quickSelect(arr, kth):
    partiton = partitonTwoWayFunction(arr)
    start, end = 0, len(arr) - 1
    while True:
        p = partiton(start, end)
        if p < kth:
            start = p + 1
        elif p > kth:
            end = p - 1
        else:
            return


def findKthLargest(arr, k):
    n = len(arr)
    quickSelect(arr, n - k)
    return arr[-k]


def findKthSmallest(arr, k):
    quickSelect(arr, k - 1)
    return arr[k]


# class TestQuickSelect(unittest.TestCase):
#     def test_findKthLargest(self):
if __name__ == '__main__':
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # arr = [1, 1]

    k = 2
    test = arr.copy()
    kthLargest = findKthLargest(test, k)
    print(kthLargest)
    assert kthLargest == 5
