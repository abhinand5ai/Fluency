import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        needle_length: int = len(needle)
        haystack_length = len(haystack)
        if haystack_length == 0 and needle_length == 0:
            return 0
        elif haystack_length < needle_length:
            return -1
        for i in range(0, haystack_length - len(needle) + 1):
            needle_temp: str = haystack[i:i + needle_length]
            if needle_temp == needle:
                return i
        return -1


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        self.assertEqual(2, self.sol.strStr("hello", "ll"))
        self.assertEqual(self.sol.strStr("aaaaa", "bba"), -1)
        self.assertEqual(self.sol.strStr("", ""), 0)
        self.assertEqual(self.sol.strStr("a", "a"), 0)
        self.assertEqual(self.sol.strStr("ab", "a"), 0)
        self.assertEqual(self.sol.strStr("a", "ab"), -1)


if __name__ == '__main__':
    unittest.main()
