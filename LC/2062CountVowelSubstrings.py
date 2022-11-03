class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"
        vf = {k: 0 for k in vowels}
        prev_c = -1
        count = 0
        start = None
        for i, c in enumerate(word):
            if c not in vowels:
                vf = {k: 0 for k in vowels}
                prev_c = i
                start = None
            else:
                vf[c] += 1
                start = i if start is None else start
                if not all(vf[x] > 0 for x in "aeiou"):
                    continue

                while vf[word[start]] > 1:
                    vf[word[start]] -= 1
                    start += 1

                count += (start - prev_c)

        return count
