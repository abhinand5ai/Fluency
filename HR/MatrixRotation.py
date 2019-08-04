#!/bin/python3


# Complete the matrixRotation function below.
def matrix_rotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])

    def rotate(i, j):
        if i >= m - i or j >= n - j:
            return
        right = [(i, y) for y in range(j, n-j)]
        down = [(x, n-j-1) for x in range(i+1, m-i)]
        left = [(m-i-1, y) for y in range(n-j-2, j-1, -1)]
        up = [(x, j) for x in range(m-i-2, i, -1)]
        layer_path = right + down + left + up
        values = [matrix[x][y] for x, y in layer_path]
        num_values = len(values)
        rotated = values[r % num_values:] + values[:r % num_values]
        for value, (x, y) in zip(rotated, layer_path):
            matrix[x][y] = value
        rotate(i+1, j+1)

    rotate(0, 0)

    for row in matrix:
        print(*row)


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrix_rotation(matrix, r)

'''
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''
