import bisect


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    i, j = 0, 0
    count = 0
    while i < n and j < m:
        if abs(b[j] - a[i]) <= k:
            j += 1
            count += 1
            i += 1
        elif a[i] - b[j] > k:
            j += 1
        elif b[j] - a[i] > k:
            i += 1
    print(count)


if __name__ == '__main__':
    main()
