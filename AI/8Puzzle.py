import heapq

GAP = "x"
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
M, N = 3, 3


def getNeighbors(state: str):
    gapL = state.find(GAP)
    state = list(state)
    i, j = gapL // M, gapL % N
    neighbors = []
    for di, dj in moves:
        x, y = di + i, dj + j
        if not 0 <= x < M or not 0 <= y < N:
            continue
        swpL = M * x + y
        state[gapL], state[swpL] = state[swpL], state[gapL]
        neighbors.append("".join(state))
        state[gapL], state[swpL] = state[swpL], state[gapL]
    return neighbors


def findPathBFS(start, end):
    q = [start]
    visited = set()
    parent = {}
    isFound = False
    while q:
        if isFound:
            break
        curr = q.pop()
        for ne in getNeighbors(curr):
            if ne not in visited:
                parent[ne] = curr
                visited.add(ne)
                q.insert(0, ne)
                if ne == end:
                    isFound = True
    if not isFound:
        return None
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return reversed(path)


def findPathAStar(start, end):
    open = [start]
    gscore = {}
    fscore = {}
    parent = {}

    def getPath(curr):
        path = [curr]
        while path[-1] != start:
            path.append(parent[path[-1]])
        return reversed(path)

    def getHeuristic(curr):
        # return sum([abs(end.find(x) - i) for i, x in enumerate(curr)])
        return sum([0 if x != y else 0 for x, y in zip(curr, end)])

    gscore[start] = 0
    fscore[start] = getHeuristic(start)
    while open:
        openF = [fscore[s] for s in open]
        loc = openF.index(min(openF))
        curr = open[loc]
        open[-1], open[loc] = open[loc], open[-1]
        open.pop()

        if curr == end:
            return getPath(curr)
        for ne in getNeighbors(curr):
            newG = gscore[curr] + 1
            if ne not in gscore or newG < gscore[ne]:
                gscore[ne] = newG
                parent[ne] = curr
                fscore[ne] = gscore[ne] + getHeuristic(curr)
                if ne not in openF:
                    open.append(ne)
    return None


if __name__ == "__main__":
    finState = "x12345678"
    # initState = "5782314x6"
    initState = "238x46175"
    initState = "328x46175"
    # initState = "16587x324"
    # initState = "61587x324"
    # print("-----------A* starts--------")
    # path = findPathAStar(initState, finState)
    # for p in path:
    #     print(p)
    # print("-----------A* ends--------")

    print("----------- search starts--------")
    # path = findPathAStar(initState, finState)
    path = findPathBFS(initState, finState)
    if not path:
        exit()
    for p in path:
        print(p)

    print("-----------ends--------")
