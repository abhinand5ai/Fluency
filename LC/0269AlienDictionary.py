# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
# 
# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
# 
# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.
# 
# A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.
# 
#  
# 
# Example 1:
# 
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:
# 
# Input: words = ["z","x"]
# Output: "zx"
# Example 3:
# 
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
#  
# 
# Constraints:
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return "".join(set(words[0]))
        graph =  defaultdict(set)
        for word in words:
            for c in word:
                graph[c]
            
        for a, b in zip(words[:-1], words[1:]):
            i = 0
            while i < min(len(a),len(b)) and a[i] == b[i]:
                i += 1
            if i == min(len(a), len(b)):
                if len(b) < len(a):
                    return ""
                continue
            graph[a[i]].add(b[i])

        color = defaultdict(lambda:'w')
        top = []

        def dfs(node):
            color[node] = 'g'
            for neighbor in graph[node]:
                if color[neighbor] == 'w':
                    if not dfs(neighbor):
                        return False
                elif color[neighbor] == 'g':
                    print("cycle")
                    return False
            color[node] = 'b'
            top.append(node)
            return True
        
        for c in list(graph.keys()):
            if color[c] == 'b':
                continue
                
            if not dfs(c):
                return ""
        print(top)

        return "".join(reversed(top))

