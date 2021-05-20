from collections import defaultdict
import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]):
        m = len(heightMap)
        n = len(heightMap[0]) if m != 0 else 0

        def neighbors(x, y):
            moves = [(x + i, y + j) for i in range(-1, 2)
                     for j in range(-1, 2) if (i, j) != (0, 0)]

            def isValid(x, y): return 0 <= x < m and 0 <= y < n

            return [(a, b) for a, b in moves if isValid(a, b)]

        def singleSourceShortestElevationPath(i, j):
            dist = defaultdict(lambda: float('inf'))
            qu = [(heightMap[i][j], i, j)]
            known = set()
            while qu:
                e, x, y = heapq.heappop(qu)
                known.add((x, y))
                dist[(x, y)] = e
                for nx, ny in neighbors(x, y):
                    if (nx, ny) in known:
                        continue
                    u_dst = max(dist[x, y], heightMap[nx][ny])
                    if u_dst < dist[(nx, ny)]:
                        dist[(nx, ny)] = u_dst
                    heapq.heappush(qu, (dist[(nx, ny)], nx, ny))
            return dist

        border = [(x, n - 1) for x in range(m)] \
                 + [(x, 0) for x in range(m)] \
                 + [(m - 1, y) for y in range(n)] \
                 + [(0, y) for y in range(n)]
        water = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                dst = singleSourceShortestElevationPath(i, j)
                water[i][j] = max(0, max([dst[b] for b in border]) - heightMap[i][j])
        print(water)
        return sum(map(sum, water))


def main():
    sol = Solution()
    water = sol.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])
    print(water)


if __name__ == '__main__':
    main()
