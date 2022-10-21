class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        op = 0
        while X < Y:
            if Y%2 == 0 :
                Y //= 2
            else:
                Y += 1
            op += 1
        
        return op + X - Y
        