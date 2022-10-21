class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        dp = [[None] * n for _ in range(m)]

        def getDp(x, y):
            if x < 0 or y < 0:
                return 0
            else:
                return dp[x][y]

        mx = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(getDp(i - 1, j), getDp(i, j - 1), getDp(i - 1, j - 1))
                    mx = max(dp[i][j], mx)

        return mx * mx


def main():
    sol = Solution()
    maximal_square = sol.maximalSquare([[0, 1], [1, 0]])
    print(maximal_square)


if __name__ == '__main__':
    main()
