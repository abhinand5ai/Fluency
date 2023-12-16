def getDigit(i, line):
    text_to_digit = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    for ch in "0123456789":
        text_to_digit[ch] = int(ch)

    for number in text_to_digit:
        if line[i:i + len(number)] == number:
            return text_to_digit[number]
    return None


def main():
    sm = 0
    with open("day1.input.txt") as file:
        for line in file:
            first = None
            last = None
            for i, _ in enumerate(line):
                digit = getDigit(i, line)
                if digit is None:
                    continue
                first = digit if first is None else first
                last = digit
            sm += 10 * first + last
    print(sm)


if __name__ == '__main__':
    main()
