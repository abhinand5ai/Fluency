class RepeatedSubString:
    def repeatedSubstringPattern(self,s:str) -> bool:
        n = len(s)
        for width in range(1,n//2):
            if n % width !=0:
                continue
            for start in range(width):
                ch = s[start]
                if n//width != sum(ch == s[x] for x in range(start,n,width)):
                    return False
        return True




