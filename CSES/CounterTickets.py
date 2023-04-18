import bisect


def main():
    n, m = map(int, input().split())
    tp = list(map(int, input().split()))
    mp = list(map(int, input().split()))
    tp.sort()

    tp = [[v, i + 1] for i, v in enumerate(tp)]

    left = [i for i in range(n)]
    right = [i for i in range(n)]

    def getOrNext(i, d):
        acc = []
        while 0 <= i < n and mp[i] is None:
            acc.append(i)
            i = d[i]
        for x in acc:
            d[x] = i

        return i
    
    def getMid(start, end):
        start = getOrNext(start, right)
        end = getOrNext(end, left)

    def delete(i):
        mp[i] = None
        right[i] = getOrNext(i + 1, right)
        left[i] = getOrNext(i - 1, left)

    def binarySearch(i):
        start = getOrNext(0, right)
        end = getOrNext(1, left)

        while start < end:
            mid = (start + end) // 2

