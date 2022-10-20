from typing import List

class Scheduler:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        tradeOffSorted = sorted(range(n), key=lambda x: -abs(costs[x][0] - costs[x][1]))
        a = n//2
        b = n//2
        cost = 0
        for i in tradeOffSorted:
            if a > 0 and b > 0:
                if costs[i][0] < costs[i][1]:
                    cost += costs[i][0]
                    a -= 1
                else:
                    cost += costs[i][1]
                    b -= 1
            elif a > 0:
                cost += costs[i][0]
            else:
                cost += costs[i][1]
        return cost


             




sch = Scheduler()
sch.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])

