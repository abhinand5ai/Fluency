class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        rows = [0] * m
        cols = [0] * n
        r1 = set()
        c1 = set()
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if rows[i] == 1:
                        r1.remove(i)
                    if cols[j] == 1:
                        c1.remove(j)
                    rows[i] += 1
                    cols[j] += 1
                    if rows[i] == 1:
                        r1.add(i)
                    if cols[j] == 1:
                        c1.add(j)
        
        return sum(picture[x][y] == 'B' for x, y in itertools.product(r1, c1))
