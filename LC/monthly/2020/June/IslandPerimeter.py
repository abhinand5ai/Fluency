from type import List

class Island:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        perimeter = [0]
        def dfs(i,j):
            if not(0 <= i < m) or not(0<= j < n) or grid[i][j] == 0:
                perimeter[0] += 1
                return
            if grid[i][j] == -1:
                return
            grid[i][j] = -1
            neighbors = [(i + 1, j), (i - 1, j), (i, j  + 1), (i, j-1)]
            for x,y in neighbors:
                dfs(x,y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return perimeter[0]
        return perimeter[0]




