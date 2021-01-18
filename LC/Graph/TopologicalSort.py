from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        directedGraph = defaultdict(lambda: set())
        color = [-1]*(numCourses)
        for preRequisite in prerequisites:
            curr,prev = preRequisite
            directedGraph[prev].add(curr)
        visited = [0]
        def isDfsCycle(curr: int):
            if color[curr] == 0:
                return False
            if color[curr] == 1:
                return True
            color[curr] = 1
            for child in directedGraph[curr]:
                if isDfsCycle(child):
                    return True
            color[curr] = 0
            visited[0] += 1
            # print(curr)
            return False
     
        return not(any(map(isDfsCycle, range(numCourses)))) and visited[0] == numCourses

        

        
        