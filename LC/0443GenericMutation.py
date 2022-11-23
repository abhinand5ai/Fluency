from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = set()
        visited.add(start)
        q = [start]
        depth = 0

        def neighbors(seq):
            ne = []
            for b in bank:
                if sum(y != x for x, y in zip(b, seq)) == 1:
                    ne.append(b)
            return ne

        while q:
            nq = []
            depth += 1
            for g in q:
                for ne in neighbors(g):
                    if ne == end:
                        return depth
                    if ne not in visited:
                        visited.add(ne)
                        nq.append(ne)
            q = nq

        return -1


def main():
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    sol = Solution()
    v = sol.minMutation(start, end, bank)
    print(v)


if __name__ == "__main__":
    main()
