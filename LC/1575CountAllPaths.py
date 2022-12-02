from functools import cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        
        @cache
        def ways(i: int, f: int):
            # print(i,locations[i], f)
            if f  < 0:
                return 0
            sm = 0
            if i == finish:
                sm += 1
            for j in range(n):
                if i == j:
                    continue
                sm += ways(j, f - abs(locations[i] - locations[j]))
                sm = sm % 1000000007

            return sm 
        
        return ways(start, fuel)
                