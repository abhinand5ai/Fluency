from collections import defaultdict
import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]):
        m = len(heightMap)
        n = len(heightMap[0]) if m != 0 else 0
        maxH = max(map(max, heightMap))

        def neighbors(x, y):
            dx_dy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            moves = [(x + dx, y + dy) for dx, dy in dx_dy]

            def isValid(a, b): return 0 <= a < m and 0 <= b < n

            return [(a, b) for a, b in moves if isValid(a, b)]

        def singleSourceShortestElevationPath(i, j):
            pathWithMinMaxElevation = defaultdict(lambda: maxH)
            qu = [(heightMap[i][j], i, j)]
            known = set()
            while qu:
                e, x, y = heapq.heappop(qu)
                known.add((x, y))
                pathWithMinMaxElevation[(x, y)] = e
                ns = neighbors(x, y)
                for nx, ny in ns:
                    if (nx, ny) in known:
                        continue
                    updatedMaxElevation = max(pathWithMinMaxElevation[x, y], heightMap[nx][ny])
                    if updatedMaxElevation < pathWithMinMaxElevation[(nx, ny)]:
                        pathWithMinMaxElevation[(nx, ny)] = updatedMaxElevation
                    heapq.heappush(qu, (pathWithMinMaxElevation[(nx, ny)], nx, ny))
            return pathWithMinMaxElevation

        border = [(x, n - 1) for x in range(m)] \
                 + [(x, 0) for x in range(m)] \
                 + [(m - 1, y) for y in range(n)] \
                 + [(0, y) for y in range(n)]
        water = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                dst = singleSourceShortestElevationPath(i, j)
                minElevationToABorder = min([dst[b] for b in border])
                water[i][j] = max(0, minElevationToABorder - heightMap[i][j])
        # printListOfLists(heightMap)
        # print("-" * 10)
        # printListOfLists(water)
        return sum(map(sum, water))


def printListOfLists(listOfList: list[list]):
    rep = "\n".join([" ".join(map(str, lst)) for lst in listOfList])
    print(rep)


def main():
    sol = Solution()
    water = sol.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])
    print(water)
    water = sol.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]])
    print(water)


if __name__ == '__main__':
    main()
