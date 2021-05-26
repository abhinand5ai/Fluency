class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stk = []
        i = 0
        curr = 0
        while i < len(S):
            if S[i] == '(':
                stk.append('(')
                i += 1
                continue
            while i < len(S) and S[i] == ')':
                while stk[-1] != '(':
                    curr = stk.pop() + curr
                curr = max(2*curr, 1)
                stk.pop()
                i += 1
            stk.append(curr)
            curr = 0
        return int(sum(stk))


                
sol = Solution()
score = sol.scoreOfParentheses( "(()(())())()()" )
print(score)
                
        
        
            
                
            
            
                
        