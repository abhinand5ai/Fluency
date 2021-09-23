from collections import defaultdict
import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]):
        m = len(heightMap)
        n = len(heightMap[0]) if m != 0 else 0
        GROUND = (m, 0)
        border = [(x, n - 1) for x in range(m)] + [(x, 0) for x in range(m)] + \
                 [(m - 1, y) for y in range(n)] + [(0, y) for y in range(n)]
        minMaxElevationInAPathTo = [100000] * (m * n + 1)
        known = [False] * (m * n + 1)

        def isKnown(loc):
            x, y = loc
            return known[x * n + y]

        def setKnown(loc):
            x, y = loc
            known[x * n + y] = True

        def getElevation(loc):
            x, y = loc
            return minMaxElevationInAPathTo[x * n + y]

        def setElevation(loc, elevation):
            x, y = loc
            minMaxElevationInAPathTo[x * n + y] = elevation

        def neighbors(loc):
            if loc == GROUND:
                return border
            x, y = loc
            dx_dy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            moves = [(x + dx, y + dy) for dx, dy in dx_dy]

            def isValid(a, b): return 0 <= a < m and 0 <= b < n

            return [(a, b) for a, b in moves if isValid(a, b)]

        def height(loc):
            if loc == GROUND:
                return 0
            x, y = loc
            return heightMap[x][y]

        pq = [(height(GROUND), GROUND)]
        water = 0
        level = 0
        while pq:
            h, curr = heapq.heappop(pq)
            if isKnown(curr):
                continue
            setKnown(curr)
            water += max(0, h - height(curr))
            setElevation(curr, h)
            for ne in neighbors(curr):
                if isKnown(ne):
                    continue
                currElevation = getElevation(ne)
                relaxedElevation = max(getElevation(curr), height(ne))
                if currElevation > relaxedElevation:
                    setElevation(ne, relaxedElevation)
                    heapq.heappush(pq, (getElevation(ne), ne))
        return water


def main():
    sol = Solution()
    # water = sol.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])
    # print(water)
    water = sol.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]])
    print(water)


if __name__ == '__main__':
    main()
