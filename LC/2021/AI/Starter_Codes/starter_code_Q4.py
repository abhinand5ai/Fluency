import numpy as np
import copy
import seaborn as sns
import matplotlib.pyplot as plt
import random
import string

##Define empty grid 
N = 8
grid = np.zeros([N, N], dtype=int)
grid = grid.tolist()


# Is it possible to place a queen into x, y ?
# Output : return True #if and only if every check clears after checking row column and diagonals
def possible(grid, x, y):
    queens = getQueens(grid)
    return isPossible(queens, x, y)


def isPossible(queens, x, y):
    for i, j in queens:
        if i == x or y == j or abs(x - i) == abs(y - j):
            return False
    return True


def getQueens(grid):
    queens = []
    for i, row in grid:
        for j, val in row:
            if val == 1:
                queens.append((i, j))
    return queens


# Place 8 queens into grid. Go through each square
def solve(grid):
    # Your code here
    res = {"placements": []}
    loc = [(i, j) for j in range(len(grid[0])) for i in range(len(grid))]

    def placeQueens(queens):
        if len(queens) == 8:
            res["placements"] = [x for x in queens]
            return True
        next_queens = [(i, j) for i, j in loc if isPossible(queens, i, j)]
        # random.shuffle(next_queens)   # solution depends on the order of the next_queens
        for queen in next_queens:
            queens.append(queen)
            if placeQueens(queens):
                return True
            queens.pop()

    placeQueens([])
    for qi, qj in res["placements"]:
        grid[qi][qj] = 1
    return grid


# Plotting the solution on chess board
def plot(grid):
    copy_grid = copy.deepcopy(grid)
    for i, row in enumerate(copy_grid):
        for j, val in enumerate(row):
            if (i + j) % 2 == 0 and val != 1:
                copy_grid[i][j] = 2

    sns.heatmap(copy_grid)
    plt.show()


# Your code here (Hint: make use of sns heatmap)


if __name__ == '__main__':
    Solution = solve(copy.deepcopy(grid))  # get the solution
    print(np.matrix(Solution))  # Print the solution
    plot(Solution)
