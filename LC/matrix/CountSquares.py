import bisect


def countSquares(points):
    points.sort()
    n = len(points)
    count = 0

    def contains(p):
        i = bisect.bisect_left(points, p)
        return i < n and points[i] == p

    for i, p1 in enumerate(points):
        for j in range(i + 1, n):
            p2 = points[j]
            if p2[0] != p1[0]:
                break
            side = p2[1] - p1[1]
            p3 = (p1[0] + side, p1[1])
            p4 = (p1[0] + side, p1[1] + side)
            p5, p6 = (-500, -500), (-500, -500)

            if (p2[1] + p1[1]) % 2 == 0:
                y = (p2[1] + p1[1]) // 2
                x = p1[0]
                s_h = side // 2
                p5 = (x - s_h, y)
                p6 = (x + s_h, y)

            if contains(p3) and contains(p4):
#                print(p1, p2, p3, p4, True)
                count += 1
            elif contains(p5) and contains(p6):
#                print(p1, p2, p5, p6, True)
                count += 1
#            else:
#                print(p1, p2, p3, p4, False)

    return count


def main():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    return countSquares(points)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        v = main()
        print(v)

