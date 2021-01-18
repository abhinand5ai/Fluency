import unittest


class Bit:
    @staticmethod
    def and_product(a, b):
        xor = (a ^ b)
        i = 0
        while (2 ** i) < xor:
            i += 1
        return ~(2 ** i - 1) & a

class BitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Bit()

    def testAndProduct(self):
        self.assertEqual(201326592, Bit.and_product(201326653, 202375190))
        self.assertEqual(0, Bit.and_product(1, 8))
        self.assertEqual(0, Bit.and_product(1, 8))
