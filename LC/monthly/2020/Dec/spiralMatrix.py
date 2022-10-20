class Solution:
    def generateMatrix(self, n:int) -> list[list[int]]:
        matrix = [[0]*n for _ in range(n)]

        def genPerimeter(i:int, j:int, n:int) -> int:
            right = [(i + 0 , j + x) for x in range(n)] 
            down = [(i + x , j + n - 1) for x in range(1,n)] 
            left = [ (i + n - 1 , j + x) for x in reversed(range(n - 1)) ]
            up = [ (i + x , j + 0) for x in reversed(range(1,n - 1)) ]
            return right + down + left + up

        def genSpiral(n:int):
            spiral = []
            i,j = 0,0
            while n > 0:
                spiral += genPerimeter(i,j,n)
                i += 1
                j += 1
                n -= 2
            return spiral

        for loc,val in zip(genSpiral(n),range(n*n)):
            i,j = loc
            matrix[i][j] = val

        return matrix
                

