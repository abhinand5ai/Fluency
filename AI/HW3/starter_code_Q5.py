import numpy as np
import itertools


# Ceating Node
class Node:

    def __init__(self, idx, data=0):  # Constructor
        """
        id : Integer (1, 2, 3, ...)
        """
        self.id = idx
        self.data = data
        self.connectedTo = dict()

    def addNeighbour(self, neighbour, weight=0):
        """
        neighbour : Node Object
        weight : Default Value = 0
        adds the neightbour_id : wt pair into the dictionary
        """
        if neighbour.id not in self.connectedTo.keys():
            self.connectedTo[neighbour.id] = weight


# Creating graph
class Graph:

    def __init__(self):
        """
        allNodes = Dictionary (key:value)
                   idx : Node Object
        """
        self.allNodes = dict()

    def addNode(self, idx):  # adds the node
        self.allNodes[idx] = Node(idx=idx)

    def addEdge(self, src, dst, wt=0):  # Adds edge between 2 nodes
        self.allNodes[src].addNeighbour(self.allNodes[dst])
        self.allNodes[dst].addNeighbour(self.allNodes[src])

    def addNodeData(self, idx, data):  # set node data according to idx
        self.allNodes[idx].data = data


# Your code here


# Managing the graph, Create all the nodes and connect them
class SudokuConnections:
    def __init__(self):  # constructor
        self.graph = self.__generateGraph()
        self.connectEdges()

    def __generateGraph(self):  # Generates nodes with id from 1 to 81.
        graph = Graph()
        for i in range(1, 82):
            graph.addNode(i)
        return graph

    def connectEdges(self):  # Connect nodes according to Sudoku Constraints
        graph = self.graph

        def isSameRow(id1, id2):
            id1 -= 1
            id2 -= 1
            return id1 // 9 == id2 // 9

        def isSameCol(id1, id2):
            id1 -= 1
            id2 -= 1
            return id1 % 9 == id2 % 9

        def isSameGroup(id1, id2):
            id1 -= 1
            id2 -= 1
            x1, y1 = id1 // 9, id1 % 9
            x2, y2 = id2 // 9, id2 % 9
            return x1 // 3 == x2 // 3 and y1 // 3 == y2 // 3

        for i1 in range(1, 82):
            for i2 in range(1, 82):
                if i1 != i2 and (isSameCol(i1, i2) or isSameRow(i1, i2) or isSameGroup(i1, i2)):
                    graph.addEdge(i1, i2)


# Implement Graph graph coloring to complete suduko board
class SudokuBoard:

    def __init__(self, sudoku):
        self.sudokuConnections = SudokuConnections()
        for i, row in enumerate(sudoku):
            for j, val in enumerate(row):
                self.sudokuConnections.graph.addNodeData(i * 9 + j + 1, val)

    def graphColoringInitializeColor(self):
        G = self.sudokuConnections.graph.allNodes
        yet_to_colored_nodes = [node for node in G.values() if node.data == 0]
        N = len(yet_to_colored_nodes)

        def fillColor(yi):
            # print(yi)
            if yi == N:
                return True
            curr = yet_to_colored_nodes[yi]
            neighbor_colors = [G[i].data for i in curr.connectedTo if G[i].data != 0]
            for c in range(1, 10):
                if c not in neighbor_colors:
                    curr.data = c
                    if fillColor(yi + 1):
                        return True
                    curr.data = 0
            return False

        fillColor(0)
        return [[G[i * 9 + j + 1].data for j in range(9)] for i in range(9)]


def printBoard(board):
    for row in board:
        print(row)
    print("----------------------------")


if __name__ == '__main__':
    sudoku = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [4, 0, 9, 0, 0, 6, 8, 7, 0],
        [0, 0, 0, 9, 0, 0, 1, 0, 0],
        [5, 0, 4, 0, 2, 0, 0, 0, 9],
        [0, 7, 0, 8, 0, 4, 0, 6, 0],
        [6, 0, 0, 0, 3, 0, 5, 0, 2],
        [0, 0, 1, 0, 0, 7, 0, 0, 0],
        [0, 4, 3, 2, 0, 0, 6, 0, 5],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
    ]

    board = SudokuBoard(sudoku)
    connections = SudokuConnections()
    # print([x for x in connections.graph.allNodes[2].connectedTo])
    solved = board.graphColoringInitializeColor()
    printBoard(solved)
    # with open("sudokuInput.txt", "r") as file:
    #     sudoku = list(map(lambda x: list(map(int, x.split())), file))
    #     board = SudokuBoard()
    #     board.graphColoringInitializeColor()
