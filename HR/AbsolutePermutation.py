#!/bin/python3


def absolutePermutation(n, k):
    if k == 0:
        return range(1,n+1)
    elif n % k == 0 and (n / k) % 2 == 0:
        return (i + 1 + ((-1) ** (int(i / k)))*k for i in range(0, n))

    else:
        return [-1]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        print(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
