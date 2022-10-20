class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        indx = {}
        mx = 0
        for i, ch in enumerate(s):
            if ch in indx and indx[ch] >= start:
                start = indx[ch] + 1
            indx[ch] = i
            # print(s[start : i + 1])
            mx = max(mx, i - start + 1)
        return mx


def main():
    sol = Solution()
    length = sol.lengthOfLongestSubstring("tmmzuxt")
    print(length == 5)


if __name__ == '__main__':
    main()
