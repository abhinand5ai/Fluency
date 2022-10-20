import unittest
from typing import List


class Solution(object):
    def hamming_weight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hamming_weight = 0;
        while n != 0:
            if n % 2 == 1:
                hamming_weight += 1
            n = n // 2
        return hamming_weight

    def hamming_distance(self, x: int, y: int) -> int:
        hamming_distance = 0
        while x != 0 or y != 0:
            if x % 2 != y % 2:
                hamming_distance += 1
            x = x // 2
            y = y // 2
        return hamming_distance

    def reverse_bits(self, n):
        def binary(n: int):
            while n != 0:
                yield n % 2
                n = n // 2

        i: int = 0
        ret = 0
        bits = list(binary(n))
        bits.extend([0]*(32- len(bits)))
        for bit in reversed(bits):
            ret += (2 ** i) * bit
            i += 1
        return ret


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_hamming_weight(self):
        self.assertEqual(2, self.sol.hamming_weight(3))
        self.assertEqual(3, self.sol.hamming_weight(7))
        self.assertEqual(1, self.sol.hamming_weight(8))
        self.assertEqual(2, self.sol.hamming_weight(9))

    def test_hamming_distance(self):
        self.assertEqual(2, self.sol.hamming_distance(1, 4))

    def test_reverse_bits(self):
        self.assertEqual(3221225471, self.sol.reverse_bits(4294967293))
