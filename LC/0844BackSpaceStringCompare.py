from itertools import zip_longest
from typing import ParamSpec
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compress(a: str):
            i = j = len(a) - 1
            
            while j >= 0:
                if a[j] == '#':
                    while i>=0 and a[i] == '#':
                        i -= 1
                    i -= 1
                else:
                    if i == j:
                        # print(a[i])
                        yield a[i]
                        i -= 1
                j -= 1
                
        return all(x == y for x,y in zip_longest(compress(s), compress(t)))
    
def main():
    
    pass

if __name__ == '__main__':
    main()