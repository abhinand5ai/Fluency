#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(l, queries):
    l = [0] * l
    for a, b, v in queries:
        l[a-1] += v
        if b < len(l):
            l[b] -= v
    h = l[0]
    for i in range(1, len(l)):
        l[i] +=h
        h = l[i]
    return max(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
