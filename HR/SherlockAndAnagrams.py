#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n = len(s)
    anagramMap = {}
    pairs = 0
    for anagram_length in range(1,n+1):
        for i in range(n - anagram_length + 1):
            sorted_ang = ''.join(sorted(s[i:i + anagram_length]))
            ang_count = anagramMap.get(sorted_ang, 0)
            anagramMap[sorted_ang] = ang_count + 1

        pairs += sum([x*(x-1)/2 for x in anagramMap.values() if x >= 2])
        anagramMap.clear()
    return int(pairs)




if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(str(result) + '\n')



'''
Input:
2
ifailuhkqq
kkkk


Output:

3
10
'''



