from typing import List, Tuple


def bestAndWorstSelection(array: List[int]) -> Tuple[int, int]:
    worstDp = [-1] * len(array)
    worst = [-1] * len(array)
    n = len(array)

    def findWorst(a: int, b: int, c: int, index: int):
        if a >= n:
            return 0
        if b >= n:
            return array[a]
        if c >= n:
            return max(array[a], array[b])
        ab = max(array[a], array[b]) + (worstDp[c] if c == index - 1 and worstDp[c]
                                        != -1 else findWorst(c, index, index + 1, index + 2))

        ac = max(array[a], array[c]) + \
            findWorst(b, index, index + 1, index + 2)
        bc = max(array[b], array[c]) + \
            findWorst(a, index, index + 1, index + 2)
        worst = max(ab, ac, bc)
        if a + 1 == b and b + 1 == c and c + 1 == index:
            worstDp[a] = worst
        return worst

    def findBest(a: int, b: int, c: int, index: int):
        # print(a,b,c,index)
        if a >= n:
            return 0
        if b >= n:
            return array[a]
        if c >= n:
            return max(array[a], array[b])
        ab = max(array[a], array[b]) + (worstDp[c] if c == index - 1 and worstDp[c]
                                        != -1 else findBest(c, index, index + 1, index + 2))
        ac = max(array[a], array[c]) + findBest(b, index, index + 1, index + 2)
        bc = max(array[b], array[c]) + findBest(a, index, index + 1, index + 2)
        best = min(ab, ac, bc)
        if a + 1 == b and b + 1 == c and c + 1 == index:
            worstDp[a] = best
        return best

    return findBest(0, 1, 2, 3), findWorst(0, 1, 2, 3)


if __name__ == "__main__":
    print(bestAndWorstSelection(
        [10, 1, 1, 10]))
    print(bestAndWorstSelection([1, 2, 3]))
