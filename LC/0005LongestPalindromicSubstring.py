from functools import cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def palindromeFrom(i: int, j: int):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return j - i - 1

        mx = 0
        st, en = 0, 0
        for i in range(n):
            l1 = palindromeFrom(i, i)
            l2 = palindromeFrom(i, i + 1)
            ln = max(l1, l2)
            if mx < ln:
                st = i - ((ln - 1) // 2)
                en = i + (ln // 2)
        return s[st:en + 1]


def main():
    input = "vmqjjfnxtyciixhceqyvibhdmivndvxyzzamcrtpywczjmvlodtqbpjayfchpisbiycczpgjdzezzprfyfwiujqbcubohvvyakxfmsyqkysbigwcslofikvurcbjxrccasvyflhwkzlrqowyijfxacvirmyuhtobbpadxvngydlyzudvnyrgnipnpztdyqledweguchivlwfctafeavejkqyxvfqsigjwodxoqeabnhfhuwzgqarehgmhgisqetrhuszoklbywqrtauvsinumhnrmfkbxffkijrbeefjmipocoeddjuemvqqjpzktxecolwzgpdseshzztnvljbntrbkealeemgkapikyleontpwmoltfwfnrtnxcwmvshepsahffekaemmeklzrpmjxjpwqhihkgvnqhysptomfeqsikvnyhnujcgokfddwsqjmqgsqwsggwhxyinfspgukkfowoxaxosmmogxephzhhy"
    sol = Solution()
    palindrome = sol.longestPalindrome(input)
    print(palindrome)


if __name__ == '__main__':
    main()
