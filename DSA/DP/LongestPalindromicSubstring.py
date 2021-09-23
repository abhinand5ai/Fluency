from functools import cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def isPalindrome(i: int, j: int):
            print(i, j)
            if j < i:
                return True
            if s[i] == s[j]:
                return isPalindrome(i + 1, j - 1)
            return False

        n = len(s)
        mx = 0
        max_loc = 0, 0
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    if mx < j - i:
                        mx = j - i
                        max_loc = i, j

        return s[max_loc[0]:(max_loc[1] + 1)]


if __name__ == '__main__':
    sol = Solution()
    input = "vmqjjfnxtyciixhceqyvibhdmivndvxyzzamcrtpywczjmvlodtqbpjayfchpisbiycczpgjdzezzprfyfwiujqbcubohvvyakxfmsyqkysbigwcslofikvurcbjxrccasvyflhwkzlrqowyijfxacvirmyuhtobbpadxvngydlyzudvnyrgnipnpztdyqledweguchivlwfctafeavejkqyxvfqsigjwodxoqeabnhfhuwzgqarehgmhgisqetrhuszoklbywqrtauvsinumhnrmfkbxffkijrbeefjmipocoeddjuemvqqjpzktxecolwzgpdseshzztnvljbntrbkealeemgkapikyleontpwmoltfwfnrtnxcwmvshepsahffekaemmeklzrpmjxjpwqhihkgvnqhysptomfeqsikvnyhnujcgokfddwsqjmqgsqwsggwhxyinfspgukkfowoxaxosmmogxephzhhy"

    palindrome = sol.longestPalindrome(input)
    print(palindrome)
