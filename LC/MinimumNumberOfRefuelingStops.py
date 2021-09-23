import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        qu = [(startFuel, 0)]
        stations = [(0, 0)] + stations
        n = len(stations)
        steps = 0
        while qu:
            # print(qu)
            nxt_qu = []
            mxLoc, mxNetFuel = 0, 0
            for curr in qu:
                tank, i = curr
                loc, fuel = stations[i]
                farthest = loc + fuel + tank
                if farthest >= target:
                    return steps
                for j in range(i + 1, n):
                    newLoc, newFuel = stations[j]
                    newTank = fuel + tank - newLoc + loc
                    if newLoc > farthest:
                        break
                    nxt_qu.append((newTank, j))
            dct = {}
            for v, l in nxt_qu:
                dct[l] = max(dct.get(l, 0), v)

            qu = [(dct[l], l) for l in dct]
            steps += 1
        return -1




class Solution2:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        curr = startFuel
        stations.append((target, 0))
        hp = []
        stops = 0
        for loc, fuel in stations:
            while curr < loc:
                if hp:
                    curr += -heapq.heappop(hp)
                    stops += 1
                else:
                    return -1
            heapq.heappush(hp, -fuel)
        return stops


def main():
    sol = Solution()
    target = 100
    fuel = 25
    stations = [[25, 25], [50, 25], [75, 25]]
    minStops = sol.minRefuelStops(target, fuel, stations)
    print(minStops)


if __name__ == '__main__':
    main()
