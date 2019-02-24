#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = [0] * n
    for i in range(0, len(q) - 1):
        if q[i] > q[i + 1]:
            j = i + 1;
            while j >= 1 and q[j] < q[j - 1]:
                bribes[q[j - 1] - 1] += 1
                q[j], q[j - 1] = q[j - 1], q[j]
                j -= 1
    if any([x > 2 for x in bribes]):
        print("Too chaotic")
    else:
        print(sum(bribes))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
