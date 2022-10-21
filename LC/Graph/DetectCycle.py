from collections import defaultdict
from typing import Optional


def findCycle(G: dict[int, list[int]]) -> Optional[list[int]]:
    n: int = len(G)
    color = [0] * n
    parent = [None] * n

    def detectCycle(v) -> Optional[tuple[int, int]]:
        color[v] = 1
        for w in G[v]:
            if color[w] == 0:
                parent[w] = v
                cycle = detectCycle(w)
                if cycle != None:
                    return cycle
            elif w != parent[v]:
                return v, w
        return None

    c1, c2 = None, None
    cycle = None
    for i in range(n):
        if color[i] == 0:
            cycle = detectCycle(i)
            if cycle is not None:
                c1, c2 = cycle
                break
    if cycle is None:
        return None
    
    path = []
    while c1 != c2:
        path.append(c1)
        c1 = parent[c1]
    path.append(c1)
    return  path




def buildGraph(edges: list[list[int]]) -> dict[int, list[int]]:
    graph: dict[int, list] = defaultdict(list)
    for v, w in edges:
        graph[v].append(w)
        graph[w].append(v)
    return graph


def main():
    edges = [
        [0, 11],
        [11, 12],
        [12, 10],
        # [10, 0],
        [10, 1],
        [10, 2],
        [1, 3],
        [2, 4],
        [3, 5],
        [4, 6],
        [5, 7],
        [6, 7],
        [7, 8],
        [8, 9]
    ]
    graph = buildGraph(edges)
    cycle = findCycle(graph)
    print(cycle)


if __name__ == "__main__":
    main()
