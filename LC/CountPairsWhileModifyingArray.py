def solution(a, b, querries):
    smDict = {}
    iDict = {}
    # a = []
    # b = []
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            smDict[i].add(a[i] + a[j])
            iD

    def modify(q):
        _, i, x = q

    def count(q):
        _, v = q

    for q in querries:
        if len(q) == 2:
            modify(q)
        else:
            res.append(count(q))


def numSetps(n, m, x1, y1, x2, y2):
    def nextMove(i, j, dx, dy):
        return i + dx, j + dy
    
    
    

    


if __name__ == '__main__':
    # steps = numSetps(5, 5, 2, 2, 1, 1)
    # print(steps)

    # steps = numSetps(5, 3, 2, 0, 3, 2)
    # print(steps)

    steps = numSetps(5, 5, 2, 1, 1, 0)
    print(steps)

    steps = numSetps(65, 3, 4, 2, 3, 1)
    print(steps)
