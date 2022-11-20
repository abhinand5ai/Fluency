class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        op = 0
        for c in s:
            if c == '(':
                op += 1
            elif c == ')':
                if not op:
                    count += 1
                else:
                    op -= 1
        return count + op