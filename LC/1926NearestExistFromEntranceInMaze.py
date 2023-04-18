class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = {}

        def neighbors(i, j):
            ne = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            return [(a,  b) for a, b in ne if 0 <= a < m and 0 <= b < n and maze[a][b] != '+' and (a, b) not in visited]

        qu = [entrance]
        dist = 0
        while qu:
            nxt_qu = []
            for x in qu:
                for ne in neighbors(qu):
                    a, b = ne
                    if a == 0 or b == 0:
                        return dist
                    if ne in visited:
                        continue
                    visited.add(ne)
                    nxt_qu.append(ne)
            dist += 1
            qu = nxt_qu
