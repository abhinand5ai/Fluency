#!/bin/python3

import math
import os
import random
import re
import sys


def list_group_by(l):
    l_dict = {}
    for item in set(l):
        item_count = l_dict.get(item, 0)
        item_count += 1
        l_dict[item] = item_count
    return l_dict


# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    l_dict = list_group_by(s)
    shuffled_string = ""
    for item in l_dict:
        shuffled_string += item * (l_dict[item] / 2)
    pass


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
