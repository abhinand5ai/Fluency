import unittest
from typing import List


class BinarySearch:
    def search_rotated_sorted_array(self, array: List[int]) -> int:
        pass

    def get_rotation_count(self, array: List[int]) -> int:
        def find_rotation(i: int, j: int):
            if i == j:
                return i

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.bSearch = BinarySearch()

    def test_get_rotated_point(self):
        a = [5, 6, 7, 1, 2, 3, 4]
        point = self.bSearch.get_rotated_point(a)
        self.assertEqual(3, point)
        a = [6, 7, 1, 2, 3, 4, 5]
        point = self.bSearch.get_rotated_point(a)
        self.assertEqual(2, point)
