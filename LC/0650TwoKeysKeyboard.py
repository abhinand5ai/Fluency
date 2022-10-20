class Solution:
    def minSteps(self, n: int) -> int:
        visited = set()
        def nxt(state):
            curr,clip = state
            neighbors = [(curr, curr), (clip + curr, clip)]
            return [n for n in neighbors if n != state]

        qu = [(1,0)]
        visited.add((1,0))
        prev = {(1,0): None}
        state = None
        while qu:
            state = qu.pop()
            curr,clip = state
            if curr > n:
                continue
            if curr == n:
                break
            for next_state in nxt(state):
                if next_state not in visited:
                    prev[next_state] = state
                    qu.insert(0, next_state)
                    visited.add(next_state)


        steps = 0
        path = [state]
        while prev[state] != None:
            steps += 1
            state = prev[state]
            path.append(state)
        print(path)
        return steps


class Solution2:
    def minSteps(self, n: int) -> int:
        i = 2
        steps = 0
        while n > 1:
            if n % i == 0:
                steps += i 
                n = n//i
            else:
                i += 1
        return steps
                

class Solution3:
    def minSteps(self, n: int) -> int:
        def min(content):
            if content < 1:
                return (n + 1)





def main():
    sol = Solution()
    res = sol.minSteps(24)
    print(res)


if __name__ == "__main__":
    main()