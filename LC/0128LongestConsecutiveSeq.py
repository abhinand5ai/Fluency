from collections import defaultdict
from typing import List

from functools import cache

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)

        @cache
        def longest(num):
            if num + 1 in st:
                return 1 + longest(num + 1)
            else:
                return 1

        return max(map(longest, st))
