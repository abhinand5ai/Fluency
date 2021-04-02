from sys import maxsize
from itertools import permutations

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

    # Your code here
    n = len(graph)
    cache = {}
    cache[(1, 0)] = 0
    parent = {}

    #  state without j  and ending at one of the  i belonging to s
    def getPrevStates(s, j):
        s_j = s & ~(1 << j)
        prevStates = [(s_j, i) for i in range(1, n) if s_j & (1 << i)]
        if not prevStates:
            return [(1, 0)]
        return prevStates

    def getMinPath(s, j):
        if (s, j) in cache:
            return cache[(s, j)]
        prevStates = getPrevStates(s, j)
        dist, prev = min(
            (getMinPath(s_j, i) + graph[i][j], (s_j, i)) for s_j, i in prevStates
        )
        cache[(s, j)] = dist
        parent[(s, j)] = prev
        return cache[(s, j)]

    endSet = (1 << n) - 1
    dist, prev = min(
        (getMinPath(endSet, j) + graph[j][0], (endSet, j)) for j in range(1, n)
    )
    parent[(endSet, 0)] = prev

    min_path = [(endSet, 0)]
    while min_path[-1] != (1, 0):
        min_path.append(parent[min_path[-1]])

    return [i for s, i in min_path]  # Minimum cost path covering all 7 wonders


# Driver Code
if __name__ == "__main__":

    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    locations = ["Great Wall","Colosseum", "Chichen Itza", "Machu Picchu", "Christ", "Petra", "Taj Mahal"]
    edges =[
        ["Chichen Itza", "Colosseum"]
    ]
    s = 0
    print(travellingSalesmanProblem(graph, s))