from collections import deque


# Perform BFS/DFS on graph `g` starting from vertex `v`
# Input parameters: Graph "g"
#                  Source vertex "src"
#                  Destination vertex "dest"
#                  Number of hops allowed "m"
# Output : return number of paths from source to destination
def search(g, src, dest, m):
    # (Your code here)
    paths = []

    def dfs(curr, path):
        if curr == dest and len(path) == m:
            paths.append([x for x in path])
            return
        if curr == dest:
            return
        for c in graph[curr]:
            if c not in path:
                path.append(c)
                dfs(c, path)
                path.pop()
        return

    dfs(src, [src])
    for path in paths:
        print(path)
    return len(paths)


if __name__ == '__main__':
    edges = [
        (0, 1),
        (0, 6),
        (0, 7),
        (1, 2),
        (1, 5),
        (1, 6),
        (2, 3),
        (3, 4),
        (4, 11),
        (5, 4),
        (6, 5),
        (6, 10),
        (6, 9),
        (7, 6),
        (7, 9),
        (7, 8),
        (8, 6),
        (8, 9),
        (9, 10),
        (10, 5),
        (10, 4),
        (10, 11),
    ]
    graph = {}
    for a, b in edges:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
    print(search(graph, 0, 11, m=5))
    # To Do : Insert List of graph edges 
    # To Do : Construct graph 
    # To Do : Search traversal from the source vertex src
