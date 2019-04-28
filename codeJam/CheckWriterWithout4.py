tests = int(input())
for i in range(tests):
    n = list(
        map(int,
            list(str(input()))
            )
    )
    a = []
    b = []
    for num in n:
        if num == 4:
            a.append(2)
            b.append(2)
        else:
            a.append(num)
            b.append(0)

    A = "".join([str(i) for i in a]).lstrip('0')
    B = "".join([str(i) for i in b]).lstrip('0')

    print(f"Case #{i+1}: {A} {B}")
