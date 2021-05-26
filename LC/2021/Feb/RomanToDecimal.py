class Solution:
    def romanToInt(self, s: str) -> int:
        r_d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        acc = 0
        tmp = 0
        for i,r in enumerate(s):
            tmp += r_d[r]
            if i > 0 and r_d[r] > r_d[s[i-1]]:
                tmp = r_d[r] -  tmp
                acc += tmp
                tmp = 0
        acc += tmp



