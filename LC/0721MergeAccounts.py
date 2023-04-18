from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        en = {}
        p = {}
        r = defaultdict(int)

        def find(e):
            if e not in p:
                p[e] = e
            if p[e] == e:
                return e
            p[e] = find(p[e])
            return p[e]

        def union(e1, e2):
            e1 = find(e1)
            e2 = find(e2)

            if e1 == e2:
                return False
            elif r[e1] > r[e2]:
                p[e2] = e1
            elif r[e1] < r[e2]:
                p[e1] = e2
            else:
                r[e1] += 1
                p[e2] = e1
            return False

        for name, primary, *emails in accounts:
            en[primary] = name
            find(primary)
            for email in emails:
                union(primary, email)

        merge = defaultdict(list)
        for e in p:
            merge[find(p[e])].append(e)
        return [[en[e], *sorted(merge[e])] for e in merge]


def main():
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com",
                                                                          "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
    accounts = [["David", "David0@m.co", "David1@m.co"],
                ["David", "David3@m.co", "David4@m.co"],
                ["David", "David4@m.co", "David5@m.co"],
                ["David", "David2@m.co", "David3@m.co"],
                ["David", "David1@m.co", "David2@m.co"]]
    sol = Solution()
    merge = sol.accountsMerge(accounts=accounts)
    print(merge)


if __name__ == "__main__":
    main()
