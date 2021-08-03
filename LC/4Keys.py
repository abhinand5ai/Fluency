# User function Template for python3
from functools import lru_cache


class Solution:
    def optimalKeys(self, N):
        # code here
        def nextState(currState, operation):
            s, c, v = currState
            if operation == 'A':
                return v, c, v
            elif operation == 'C':
                return s, s, v
            elif operation == 'V':
                return s, c, v + c
            elif operation == 'K':
                return s, c, v + 1
            else:
                raise ValueError("unknown operation")

        def neighbors(currState):
            ne = []
            for op in ['A', 'C', 'V', 'K']:
                nxt = nextState(currState, op)
                if nxt != currState:
                    ne.append(nxt)
            return ne

        qu = [(0, 0, 0)]
        moves = 0
        visited = {(0, 0, 0)}
        while moves < N:
            nxt_qu = []
            mxA, mxC, mxV = 0, 0, 0
            print(len(qu))
            for state in qu:
                for ne in neighbors(state):
                    a, c, v = ne
                    if ne not in visited:
                        visited.add(ne)
                        if mxA < a and mxC < c and mxV < v:
                            mxA, mxC, mxV = a, c, v
                        nxt_qu.append(ne)
            qu = [(a, c, v) for a, c, v in nxt_qu if not (a < mxA and c < mxC and v < mxV)]
            moves += 1

        return max(v for _, _, v in qu)


def main():
    ob = Solution()
    print(ob.optimalKeys(100))


if __name__ == '__main__':
    main()
