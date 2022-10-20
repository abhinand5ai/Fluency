import unittest
from typing import List


class ThreeWayPartition:

    @staticmethod
    def threeWayPartition(arr, n, a, b):
        def swap(i: int, j: int):
            arr[i], arr[j] = arr[j], arr[i]

        lt, i, gt = 0, 0, n
        while i <= gt:
            if a <= arr[i] <= b:
                i += 1
            elif arr[i] < a:
                swap(lt, i)
                lt += 1
                i += 1
            else:
                swap(i, gt)
                gt -= 1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test(self):
        a = [1, 1, 1, 0, 0, 0, 2, 2, 2, 2]
        ThreeWayPartition.threeWayPartition(a, len(a) - 1, 0, 0)
        self.assertEquals([0, 0, 0, 1, 1, 1, 2, 2, 2, 2], a)

