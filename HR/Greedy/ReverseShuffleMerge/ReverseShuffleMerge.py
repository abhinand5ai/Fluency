#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


def list_group_by(ls):
    fq = defaultdict(int)
    for w in ls:
        fq[w] += 1
    return fq


# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    l_dict = list_group_by(s)



if __name__ == '__main__':
    s = input()

    result = reverseShuffleMerge(s)

    print(result + '\n')

'''
Input:
eggegg

Output:
egg

Input:
abcdefgabcdefg

Output:
agfedcb

'''
