from collections import defaultdict
import math


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        leaves = [i for i in range(n) if degree[i] == 1]
        remaining = n
        while remaining > 2:
            newLeaves = []
            for leaf in leaves:
                for ne in graph[leaf]:
                    degree[ne] -= 1
                    if degree[ne] == 1:
                        newLeaves.append(ne)
                remaining -= 1
            leaves = newLeaves
        return leaves
