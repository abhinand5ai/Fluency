from queue import PriorityQueue as pq
from copy import deepcopy

# Create a class called Node
class Node(object):
    # Constructor
    def __init__(self, board: list[list[int]], move, parent=None):
        self.board = [
            [x for x in row] for row in board
        ]  # 2D matrix representing checker baord
        self.move = move
        self.parent = parent
        self.f = move + self.manhattan_distance() if move else self.manhattan_distance()

    # Returns the position of the empty block
    def zero_position(self):
        # Your code here
        board = self.board
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == 0:
                    return (i, j)
        return None

    # Returns the manhattan distance (You can implement any other alternative too)
    def manhattan_distance(self):
        # Your code here
        board = self.board
        n = len(board)
        manhattan = 0
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                ei, ej = val // n, val % n
                manhattan += abs(i - ei) + abs(j - ej)
        return manhattan

    # This function will generate and return nodes.
    def generate_nodes(self):
        allnodes = []  # an array that will store nodes.
        zero_position = self.zero_position()
        board = self.board
        zi, zj = self.zero_position()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in moves:
            si, sj = zi + di, zj + dj
            if 0 <= si < len(board) and 0 <= sj < len(board):
                board[zi][zj], board[si][sj] = board[si][sj], board[zi][zj]
                allnodes.append(Node(board, self.move + 1, self))
                board[zi][zj], board[si][sj] = board[si][sj], board[zi][zj]
        return allnodes

    # Store all the parents "traceback" of a node.
    def traceback(self):
        path = []
        curr = self
        while curr:
            path.append(curr)
            curr = curr.parent
        path.reverse()
        return path  # returns a list of objects.

    def __lt__(self, value):
        return self.f < value.f


def is_end(board):
    n = len(board)
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val != n * i + j:
                return False
    return True


def invert_random_pair(board):
    board = [[x for x in row] for row in board]
    i1, j1 = None, None
    i2, j2 = None, None

    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val != 0:
                if i1 is not None:
                    i1, j1 = i, j
                else:
                    i2, j2 = i, j
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]
    return board


# A-star implementation
def Astar(initial_node):
    q1 = pq()
    q1.put(initial_node)
    while not q1.empty():
        curr = q1.get()
        if is_end(curr.board):
            return curr.traceback()
        for ne in curr.generate_nodes():
            q1.put(ne)
    return None


# Prints the board
def draw_board(board):
    # Your code here
    print("\n".join([" ".join(map(str, row)) for row in board]))


# initial_node = Node([[5, 7, 8], [2, 3, 1], [4, 0, 6]], 0)  # Initial state 1
initial_node = Node([[2, 3, 8], [4, 0, 6], [1, 7, 5]], 0)  # Initial state 1

path = Astar(initial_node)
print("num of moves :" + str(len(path)))
for p in path:
    print("----------------")
    draw_board(p.board)

# draw_board(initial_node.board)
# for ne in initial_node.generate_nodes():
#     print("-------------------")
#     print("manhattan: " + str(ne.manhattan_distance()))
#     print("zero_position: " + str(ne.zero_position()))
#     draw_board(ne.board)
