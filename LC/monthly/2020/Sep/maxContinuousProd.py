from typing import List
class Solution:
    def maxProduct(self, A: List[int]) -> int:
        B = A[::-1]
        for i in range(1,len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        
        return max(A + B)
             
                
                

            



sol = Solution()
mx = sol.maxProduct([1,0,-1,3,-2,-2,0,1])
print(mx)

# mx = sol.maxProduct([2,3,-2,4])
# print(mx)
