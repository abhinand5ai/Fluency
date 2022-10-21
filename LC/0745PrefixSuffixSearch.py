import bisect


class Node:
    def __init__(self, key):
        self.key = key
        self._loc: list = []
        self._children: dict = {}

    def add_location(self, loc):
        bisect.insort(self._loc, loc)

    def get_locations(self):
        return self._loc

    def add_child(self, child):
        self._children[child.key] = child

    def get_child(self, k):
        if k in self._children:
            return self._children[k]
        return None


class Trie:
    def __init__(self):
        self.root = Node(None)

    def find(self, seq) -> Node:
        curr = self.root
        for key in seq:
            curr = curr.get_child(key)
            if curr is None:
                return curr
        return curr

    def insert(self, seq, loc) -> None:
        curr = self.root
        for key in seq:
            nxt = curr.get_child(key)
            if nxt is None:
                nxt = Node(key)
                curr.add_child(nxt)
            curr = nxt
            curr.add_location(loc)


class WordFilter:

    def __init__(self, words: list[str]):
        self.prefixSearch = Trie()
        self.suffixSearch = Trie()
        for i, word in enumerate(words):
            self.prefixSearch.insert(seq=word, loc=i)
            self.suffixSearch.insert(seq=reversed(word), loc=i)

    def f(self, prefix: str, suffix: str) -> int:
        prefixNode = self.prefixSearch.find(prefix)
        prefixLoc = prefixNode.get_locations() if prefixNode else []
        suffixNode = self.suffixSearch.find(reversed(suffix))
        suffixLoc = suffixNode.get_locations() if suffixNode else []
        i = len(prefixLoc) - 1
        j = len(suffixLoc) - 1
        while i >= 0 and j >= 0:
            if prefixLoc[i] == suffixLoc[j]:
                return prefixLoc[i]
            elif prefixLoc[i] < suffixLoc[j]:
                j -= 1
            else:
                i -= 1
        return -1


def main():
    wordlist = ["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa", "accabaccaa", "cabcbbbcca",
                "ababccabcb", "caccbbcbab", "bccbacbcba"]
    wordFilter = WordFilter(wordlist)
    queries = [["bccbacbcba", "a"], ["ab", "abcaccbcaa"], ["a", "aa"], ["cabaaba", "abaaaa"],
               ["cacc", "accbbcbab"], ["ccbcab", "bac"], ["bac", "cba"], ["ac", "accabaccaa"], ["bcbb", "aa"],
               ["ccbca", "cbcababac"]]
    print([wordFilter.f(suf, pref) for suf, pref in queries])
    print(wordFilter.f("ab", "abcaccbcaa"))

    wordlist.sort(key=lambda x: x[1])


if __name__ == '__main__':
    main()
