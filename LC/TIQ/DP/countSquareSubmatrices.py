class Matrix:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        def getNumMatrices(i,j):
            if matrix[i][j] == 0:
                return 0
            else:
                prevRow = max(i-1,0)
                prevCol = max(j-1,0)
                return min(dp[prevRow][j], dp[i][prevCol], dp[prevRow][prevCol]) + 1
            
        for i in range(m):
            for j in range(n):
                dp[i][j] = getNumMatrices(i,j)
        
        return sum(sum(row) for row in dp)
        

        


                
        