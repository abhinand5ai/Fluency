class Solution:
    def calculate(self, exp: str) -> int:
        stk = []
        balance = {}
        for i, c in enumerate(exp):
            if c == ')':
                balance[stk.pop()] = i
            elif c == '(':
                stk.append(i)

        def popAcc(acc):
            if len(acc) == 1:
                return acc.pop()
            elif len(acc) == 2:
                b = acc.pop()
                op = acc.pop()
                if op == '-':
                    return -b
                else:
                    return b
            elif len(acc) >= 2:
                b = acc.pop()
                op = acc.pop()
                a = acc.pop()
                if op == '-':
                    return a - b
                elif op == '+':
                    return a + b
            else:
                assert False

        def eval(i, j):
            acc = []
            while i <= j:
                if exp[i] == ' ':
                    i += 1
                    continue
                if exp[i] == '(':
                    acc.append(eval(i + 1, balance[i] - 1))
                    v = popAcc(acc)
                    acc.append(v)
                    i = balance[i] + 1
                    continue
                start = i
                while i < len(exp) and exp[i].isnumeric():
                    i += 1
                if i > start:
                    acc.append(int(exp[start:i]))
                    v = popAcc(acc)
                    acc.append(v)
                else:
                    acc.append(exp[i])
                    i += 1
            return popAcc(acc)
        return eval(0, len(exp) - 1)


def test(exp, e):
    sol = Solution()
    val = sol.calculate(exp)
    print(val == e)


def main():
    # test("1+2", 3)
    # test("1-2", -1)
    # test("(1) + (2 - (1 - 1))", 3)
    test("(7)-(0)+(4)", 11)


if __name__ == "__main__":
    main()
