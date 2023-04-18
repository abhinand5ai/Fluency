from functools import cache


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        @cache
        def count(i):
            if i == -1:
                return 1
            if i == 0:
                return 2
            prev = i - 1
            while prev >= 0 and s[prev] != s[i]:
                prev -= 1
            return (2 * count(i - 1) - count(prev - 1)) % 1_000_000_007

        return count(len(s) - 1) - 1


'''
a1 a2 a3
""
"" a1 -> 2
"" a1 a2 a1a2 --> "" a aa  -> 3
"" a1 a2 a1a2 a3 a1a3 a2a3 a1a2a3 -> "" a aa aaa -> 4 -> 2 * 3 - 2

'''
