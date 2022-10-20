from collections import defaultdict
from typing import List

class Grid:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph)
        def dfs(node:int, path:List[int]):
            if node == len(graph) - 1:
                paths.append(path[::])
            for child in graph[node]:
                path.append(child)
                dfs(child, path)
                path.pop()
        dfs(0,[0])
        return pathss
        






