# Given a string s which represents an expression, evaluate this expression and return its value.

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

from functools import reduce
import re


class Solution:
    def calculate(self, s: str) -> int:
        def eval(s, op_i):
            add_sub = []
            acc = []
            for ch in s:
                if ch not in op:
                    acc.append(ch)
                else:
                    eval( ""., op_i + 1)
