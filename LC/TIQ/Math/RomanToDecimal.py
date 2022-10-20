import unittest


class Solution:
    def romanToInt(self, romanNumber: str) -> int:
        ROMAN_DIGITS = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i: int = 0
        n = len(romanNumber)
        decimal: int = 0
        while i < n:
            if i < n - 1:
                if ROMAN_DIGITS[romanNumber[i + 1]] <= ROMAN_DIGITS[romanNumber[i]]:
                    decimal += ROMAN_DIGITS[romanNumber[i]]
                else:
                    decimal += ROMAN_DIGITS[romanNumber[i + 1]]
                    decimal -= ROMAN_DIGITS[romanNumber[i]]
                    i += 1
            elif i == n - 1:
                decimal += ROMAN_DIGITS[romanNumber[i]]
            i +=1

        return decimal


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        self.assertEqual(self.sol.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(self.sol.romanToInt("LVIII"), 58)
        self.assertEqual(self.sol.romanToInt("IX"), 9)
        self.assertEqual(self.sol.romanToInt("IV"), 4)
        self.assertEqual(self.sol.romanToInt("III"), 3)


if __name__ == '__main__':
    unittest.main()
