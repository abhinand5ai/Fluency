from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        ret = []
        n = len(s)
        wordDict = set(wordDict)

        @cache
        def wordBreak(start: int):
            ret = []
            for end in range(start + 1, n):
                if s[start: end + 1] not in wordDict:
                    continue
                pref = s[start:end + 1]
                if end + 1 == n:
                    ret.append(pref)
                    break
                for x in wordBreak(end + 1):
                    ret.append(pref + " " + x)
            return ret

        return wordBreak(0)


def main():
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    sol = Solution()
    ret = sol.wordBreak(s, wordDict)
    print(ret)


if __name__ == "__main__":
    main()
