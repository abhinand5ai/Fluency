
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return False
            elif rank[a] > rank[b]:
                parent[b] = a
            elif rank[b] > rank[a]:
                parent[a] = b
            else:
                parent[a] = b
                rank[b] += 1
            return True

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        for a, b in edges:
            # print(parent, rank)
            if not union(a, b):
                return [a, b]
