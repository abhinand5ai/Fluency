import numpy as np


class FlowEdge:
    def __init__(self, v, w, capacity, flow=0):
        self.w = w
        self.v = v
        self.capacity = capacity
        self.flow = flow

    def residual_towards(self, vertex):
        if vertex == self.v:
            return self.flow
        elif vertex == self.w:
            return self.capacity - self.flow
        else:
            raise ValueError("Illegal argument")

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise ValueError("Illegal argument")

    def add_residual_to(self, vertex, residual):
        if vertex == self.w:
            self.flow += residual
        elif vertex == self.v:
            self.flow -= residual
        else:
            raise ValueError("Illegal argument")

    def __repr__(self):
        return "from :{} to:{} capacity:{} flow:{}".format(self.v, self.w, self.capacity, self.flow)


# Implement the flow - graph structure
class FlowGraph:

    # Constructor
    def __init__(self, graph):
        self.graph = graph

    # Your code here

    # method to find the augmenting paths (s — t paths)
    def get_augmenting_path(self):
        q = ["source"]
        parent = {}
        visited = set()

        while q:
            curr = q.pop()
            for edge in self.graph[curr]:
                next = edge.other(curr)
                if next not in visited and edge.residual_towards(next) > 0:
                    parent[next] = edge
                    visited.add(next)
                    q.insert(0, next)

        if "sink" in visited:
            curr = "sink"
            path = []
            while curr != "source":
                e = parent[curr]
                path.append((curr, e))
                curr = e.other(curr)

            return path
        return []

    # Your code here

    # A method to run the Ford-Fulkerson algorithm
    def ford_fulkerson(self):
        while path := self.get_augmenting_path():
            # print("-"*10)
            # print([e for _, e in reversed(path)])
            residual = min(e.residual_towards(v) for v, e in path)
            for v, e in path:
                e.add_residual_to(v, residual)
            # print([e for _, e in reversed(path)])


# Your code here
def getFlowGraph(table, team):
    graph = {}
    num_teams = len(table)
    _, team_wins, _, team_remaining, _ = table[team]
    edges = []
    for id1 in range(num_teams):
        if id1 == team:
            continue
        for id2 in range(id1 + 1, num_teams):
            _, _, _, _, schedule = table[id2]
            c = schedule[id1] * 1.0
            if id2 == team or c == 0:
                continue
            match = "{}vs{}".format(id1, id2)
            edges.append(FlowEdge("source", match, c))
            edges.append(
                FlowEdge(match, "winner_{}".format(id1), float('inf')))
            edges.append(
                FlowEdge(match, "winner_{}".format(id2), float('inf')))
    for id in range(num_teams):
        if id == team:
            continue
        _, wins, _, remaining, _ = table[id]
        edges.append(FlowEdge("winner_{}".format(id), "sink",
                     team_wins + team_remaining - wins))

    for edge in edges:
        if edge.v not in graph:
            graph[edge.v] = []
        if edge.w not in graph:
            graph[edge.w] = []
        graph[edge.v].append(edge)
        graph[edge.w].append(edge)

    return graph


# Use Ford-Fulkerson algorithm  to find which team will be eliminated

if __name__ == '__main__':
    table = {}
    with open("matches3.txt") as file:
        for i, line in enumerate(file):
            team, wins, losses, gamesLeft, *schedule = line.split()
            table[i] = (team, int(wins), int(losses), int(
                gamesLeft), list(map(int, schedule)))

    curr_wins = [tup[1] for tup in table.values()]
    for i in range(len(table)):
        team_name, team_wins, _, team_remaining, _ = table[i]
        if any(curr_win > team_remaining + team_wins for curr_win in curr_wins):
            print("{} is eliminated".format(table[i][0]))
            continue
        graph = getFlowGraph(table, i)
        flow_graph = FlowGraph(graph)
        flow_graph.ford_fulkerson()
        if all(e.flow == e.capacity for e in graph["source"]):
            print("{} have chance of winning".format(table[i][0]))
        else:
            print("{} is eliminated".format(table[i][0]))
