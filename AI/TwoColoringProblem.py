from typing import List
from collections import defaultdict


class GraphColoring:
    def isTwoColorable(self, edges, numVertices):
        graph = defaultdict(list)
        for a, b in edges:
            a = a - 1
            b = b - 1
            na = graph[a]
            nb = graph[b]
            na.append(b)
            nb.append(a)
            graph[a] = na
            graph[b] = nb
        visited = [None] * numVertices
        for v in range(numVertices):
            if visited[v] is not None:
                continue
            q = [v]
            visited[v] = True
            while q:
                curr = q.pop()
                for ne in graph[curr]:
                    if visited[ne] is not None:
                        if visited[ne] == visited[curr]:
                            return False, []
                    else:
                        visited[ne] = not visited[curr]
                        q.append(ne)
        directions = [max(visited[a - 1] - visited[b - 1], 0) for a, b in edges]
        return True, directions


if __name__ == '__main__':
    n, m, *_ = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, *_ = map(int, input().split())
        edges.append([a, b])
    gc = GraphColoring()
    isTwoC, coloring = gc.isTwoColorable(edges, n)
    if isTwoC:
        print("YES")
        print("".join(map(str, map(int, coloring))))
    else:
        print("NO")
