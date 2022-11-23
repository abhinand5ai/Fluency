def main():
    n, x = map(int, input().split())
    ps = list(map(int, input().split()))
    ps.sort()
    i = n - 1
    j = 0
    # print(ps)
    cap = x
    cnt = 0
    while i > j:
        cap -= ps[i]
        i -= 1
        if ps[j] <= cap:
            j += 1
        cap = x
        cnt += 1
    if i == j:
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
