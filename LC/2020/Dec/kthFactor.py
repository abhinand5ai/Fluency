import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = set()
        for i in range(1,n//2 + 1):
            if  n%i != 0:
                continue
            if n//i < i:
                break
            factors.add(i)
            factors.add(n//i)
        factors = sorted(factors)
        return factors[k-1] if len(factors)>= k else -1
            
            
        
