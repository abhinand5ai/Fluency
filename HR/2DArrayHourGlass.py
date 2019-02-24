#!/bin/python3


# Complete the hourglassSum function below.
HOUR_GLASS_LAYOUT = [
    (-1, -1), (-1, 0), (-1, 1),
              (0, 0),
    (1, -1),  (1, 0), (1, 1),
             ]


def hour_glass_sum(arr):
    m = len(arr)
    n = len(arr[0])

    def fits(glass):
        return all(0 <= i < m and 0 <= j < n for i, j in glass)

    def hour_glass(x,y):
        return [(x + i, y + j) for i,j in HOUR_GLASS_LAYOUT]

    max_sum = 0
    for i in range(m):
        for j in range(n):
            glass = hour_glass(i, j)
            if fits(glass):
                max_sum = max(max_sum, sum([arr[x][y] for x, y in glass]))

    return max_sum



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hour_glass_sum(arr)

    print(str(result) + '\n')

    # fptr.close()

'''
Input:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0


Output:
19

'''