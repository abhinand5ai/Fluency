from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        @cache
        def isMix(i, j):
            if i == len(s1) and j == len(s2):
                return True

            k = i + j
            s1Match = (i < len(s1)) and s1[i] == s3[k]
            s2Match = (j < len(s2)) and s2[j] == s3[k]

            return s1Match and isMix(i + 1, j) or s2Match and isMix(i, j + 1)

        return len(s1) + len(s2) == len(s3) and isMix(0, 0)


def main():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbcbbcac"
    sol = Solution()

    res = sol.isInterleave(s1, s2, s3)
    print(res)


if __name__ == '__main__':
    main()
