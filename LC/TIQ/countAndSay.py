import unittest


class Solution:
    def countAndSay(self, n: int) -> str:
        curr = [1]
        for i in range(2, n + 1):
            freq = 0
            num = curr[0]
            tmp = []
            for i in curr:
                if num == i:
                    freq += 1
                else:
                    tmp += [freq, num]
                    num = i
                    freq = 1
            tmp += [freq, num]
            curr = tmp
        return "".join(map(str,curr))


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        # self.assertEqual("1", self.sol.countAndSay(1))
        self.assertEqual("1211", self.sol.countAndSay(4))
        self.assertEqual("111221", self.sol.countAndSay(5))
        self.assertEqual("312211", self.sol.countAndSay(6))
        self.assertEqual("13112221", self.sol.countAndSay(7))
