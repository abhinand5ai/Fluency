class LCS:
    def maxUncrossedLines(self,A:List[int], B:List[int]):
        m = len(A)
        n = len(B)
        dp = [[0] * n for _ in range(m)]
        def getDp(i,j):
            if i < 0 or j < 0:
                return 0
            else:
                return dp[i][j]
        for i in range(m):
            for j in range(n):
                bestSub = max(getDp(i-1,j),getDp(i,j-1))
                dp[i][j] = 1  + bestSub if A[i] == B[j] else bestSub
        return dp[m-1][n-1]
