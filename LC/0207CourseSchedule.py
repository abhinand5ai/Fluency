from collections import defaultdict


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        color = ['w'] * n
        top = []

        def dfs(v):
            color[v] = 'g'
            for ne in graph[v]:
                if color[ne] == 'g':
                    return False
                elif color[ne] == 'w':
                    if not dfs(ne):
                        return False
            color[v] = 'b'
            top.append(v)
            return True

        for v in range(n):
            if color[v] != 'w':
                continue
            if not dfs(v):
                return False
        return True
