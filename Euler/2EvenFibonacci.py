def fibonacciGenerator():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b


def main():
    fib_sum = 0
    for x in fibonacciGenerator():
        if x > 4000000:
            break
        if x % 2 == 0:
            fib_sum += x
    print(fib_sum)


if __name__ == '__main__':
    main()
