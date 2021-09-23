from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        @cache
        def dist(i, j):
            if i == m:
                return n - j
            elif j == n:
                return m - i

            if word2[j] == word1[i]:
                return dist(i + 1, j + 1)
            else:
                return 1 + min(dist(i + 1, j), dist(i, j + 1), dist(i + 1, j + 1))

        return dist(0, 0)


def main():
    sol = Solution()
    distance = sol.minDistance("intention", "execution")
    print(distance)


if __name__ == '__main__':
    main()
