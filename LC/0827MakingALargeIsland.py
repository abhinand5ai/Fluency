from collections import defaultdict
from typing import List

class Solution:
    def largestIsland(self, grid:List[List[int]]):
        m = len(grid)
        n = len(grid[0])

        def getNeighbors(x):
            i, j = x // n, x % n
            neighbors = [ (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            neighbors = [ (a, b) for a, b in neighbors if 0 <= a < m and 0 <= b < n and grid[a][b] == 1]
            #print((i, j), neighbors)
            return [a * n + b for a, b in neighbors]

        visited = [False] * (m * n)
        parent = list(range(m *n))
        size = defaultdict(int)

        def dfs(x, p):
            #print(p, x)
            visited[x] = True
            parent[x]  = p
            size[p] += 1
            for ne in getNeighbors(x):
                if not visited[ne]:
                    dfs(ne, p)
        zeros = []
        for x in range(m * n):
            
            if grid[x // n][x % n] == 0:
                zeros.append(x)
            elif not visited[x]:
                dfs(x, x)

        mx = max(list(size.values()) + [0])
        
        #print(size)
        for z in zeros:
            groups = set(parent[ne] for ne in getNeighbors(z))
            newIslandSize = sum((size[g] if g in size else 0) for g in groups) + 1
            mx = max(mx, newIslandSize)

        return mx


def main():
    grid = [[1, 0], [0, 1]]
    sol = Solution()
    v = sol.largestIsland(grid)
    print(v)

if __name__ == '__main__':
    main()
