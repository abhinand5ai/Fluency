class Solution:
    def maximumSwap(self, num: int) -> int:
        def digits(num):
            dg = []
            while num:
                dg.append(num % 10)
                num //= 10
            return dg
        def toNum(digits):
            v = 0
            for d in digits:
                v = v * 10 + d
            return v

        ls = digits(num) 
        mxI = len(ls) - 1
        i = len(ls) - 2
        swp = None
        while i >= 0:
            if ls[i] > ls[mxI]:
                mxI = i
            else:
                swp = (i, mxI) if ls[i] != ls[mxI] else swp
            print(ls[swp[0]], ls[swp[1]])
            i -= 1

        if swp:
            a, b = swp
            ls[a], ls[b] = ls[b], ls[a]
        
        return toNum(ls)
        