from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        
        tc = Counter(t)
        sc = {k:0 for k in tc}
        res = s
        i, j = 0, 1
        sc[s[0]] = 1
        found =  False
        while i < n:
            while any(sc[k] < tc[k] for k in tc) and j < n:
                if s[j] in sc:
                    sc[s[j]] += 1
                j += 1
            if not any(sc[k] < tc[k] for k in tc):
                #print(s[i:j])
                found = True
                if j - i < len(res):
                    res = s[i:j]
                if s[i] in sc:
                    sc[s[i]] -= 1
                i += 1
            else:
                break
                 
        return res if found else ""



def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    ans = sol.minWindow(s, t)
    print(ans)


if __name__ == '__main__':
    main()
