import bisect


class Node:
    def __init__(self, val, loc, isEnd):
        self.val = val
        self.loc = loc
        self.isEnd = isEnd

    def __repr__(self):
        return f"Node({self.val},{self.loc},{self.isEnd})"

    def __lt__(self, node):
        return self.loc < node.loc


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        buildings.sort()
        nodeList = [Node(0, float("-inf"), False), Node(0, float("inf"), True)]

        def insertBuilding(building):
            s, e, h = building
            start = Node(h, s, False)
            end = Node(h, e, True)

            bisect.insort(nodeList, start)
            bisect.insort(nodeList, end)

        for building in buildings:
            insertBuilding(building)

        bSet = []
        level = [[-1, 0]]
        for curr, nxt in zip(nodeList[:-1], nodeList[1:]):
            if curr.isEnd:
                loc = bisect.bisect_left(bSet, curr.val)
                tmp = bSet[-1]
                bSet.remove(curr.val)
            else:
                bSet.append(curr.val)

            if curr.loc == nxt.loc:
                continue

            if bSet:
                mH = max(bSet)
                if level[-1][1] != mH:
                    level.append([curr.loc, mH])
            else:
                level.append([curr.loc, 0])

        return level[1:]

def main():
    sol = Solution()
    # skyline = sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
    # skyline = sol.getSkyline([[0, 2, 3], [3, 5, 3]])
    skyline = sol.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
    print(skyline)


if __name__ == '__main__':
    main()
