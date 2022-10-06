class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank = [0] * n
        parent = [i for i in range(n)]

        def union(v1, v2):
            p1 = find(v1)
            p2 = find(v2)

            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p2] < rank[p1]:
                parent[p2] = p1
            else:
                rank[p1] += 1
                parent[p2] = parent[p1]

            return True

        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]


        for a, b in edges:
            if not union(a, b):
                return False
        
        p = find(0)
        # print(parent)
        return all(find(x) == p for x in range(n))
