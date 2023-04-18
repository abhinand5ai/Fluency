'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.


Example 1:

Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]


Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

'''

def captureTheRegion(matrix):
    m = len(matrix)
    n = len(matrix[0]) 
    border = [(i, 0) for i in range(m)] +\
             [(0, j) for j in range(n)] +\
             [(i, n - 1) for i in range(m)] +\
             [(m - 1, j) for j in range(n)] 
      
    boarder_zeros = [(i, j) for i, j in border if matrix[i][j] == 'O']
    
    def isValid(i, j): return 0 <= i < m and 0 <= j < n and matrix[i][j] == 'O'
    def markUnConquerable(i, j):
        matrix[i][j] = '#'
        neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        neighbors = [(x, y) for x, y in neighbors if isValid(x, y)]
        for x, y in neighbors:
            markUnConquerable(x, y)
        
    
    for i, j in boarder_zeros:
        if matrix[i][j] != '#':
            markUnConquerable(i, j)
    
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'O':
                matrix[i][j] = 'X'
            elif matrix[i][j] == '#':
                matrix[i][j] = 'O'

def printBoard(board):
    for row in board:
        print(row)
    print("*"*10)
board = [
["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"]]

captureTheRegion(board)

printBoard(board)


board = [["O","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

captureTheRegion(board)

printBoard(board)

allZero = [['O'] * 4,['O'] * 4,['O'] * 4,['O'] * 4]

captureTheRegion(allZero)

printBoard(allZero)



board = [["O","O","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

captureTheRegion(board)

printBoard(board)
    
    