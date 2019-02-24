#!/bin/python3

# Complete the minimumSwaps function below.


def minimum_swaps(a):
    def cycle(init):
        j = init
        while True:
            yield a[j]-1
            j = a[j]-1
            if j == init:
                break
    swaps = 0
    for i in range(len(arr)):
        cycle_path = list(cycle(i))
        swaps += len(cycle_path) - 1
        tmp = a[i]
        for item in cycle_path:
            tmp, a[item] = a[item], tmp
    return swaps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)

    print(str(res) + '\n')


