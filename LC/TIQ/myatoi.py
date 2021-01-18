import unittest

'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
'''


class Solution:
    # INT_MAX (2**31 − 1) or INT_MIN (−2**31)
    def myAtoi(self, strng: str) -> int:
        strng = strng.strip()
        int_max = (2 ** 31) - 1
        int_min = (-2) ** 31
        if len(strng) == 0:
            return 0
        res = 0
        sign: int = 1
        start_index: int = 0
        if not strng[0].isdigit():
            sign = -1 if strng[0] == '-' else (1 if strng[0] == '+' else 0)
            start_index = 1
        digit_list: list = []
        for x in strng[start_index:]:
            if x.isdigit():
                digit_list.append(int(x))
            else:
                break;
        for i, digit in enumerate(reversed(digit_list)):
            res += (10 ** i) * digit

        res = res * sign
        if res > int_max:
            return int_max
        elif res < int_min:
            return int_min
        else:
            return res


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        self.assertEqual(self.sol.myAtoi("42"), 42)
        self.assertEqual(self.sol.myAtoi("-42"), -42)
        self.assertEqual(self.sol.myAtoi("4193 with words"), 4193)
        self.assertEqual(self.sol.myAtoi("words and 987"), 0)
        self.assertEqual(self.sol.myAtoi("-91283472332"), -2147483648)
        self.assertEqual(self.sol.myAtoi("  -91283472332"), -2147483648)
        self.assertEqual(self.sol.myAtoi("  +42"), 42)
        self.assertEqual(self.sol.myAtoi("  .42"), 0)
        self.assertEqual(self.sol.myAtoi("  b42"), 0)


if __name__ == '__main__':
    unittest.main()
