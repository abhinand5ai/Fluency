from typing import List
import pdb


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        def nxt(i, j, d):
            print(i, j)
            if i == m - 1 and j == n - 1:
                return None, None, None
            if d == 1:
                i -= 1
                j += 1
                if i < 0 or j > n - 1:
                    d = 0
                    j += 1
            else:
                i += 1
                j -= 1
                if i > m - 1 or j < 0:
                    d = 1
                    j += 1

            return i, j, d

        i, j, d = 0, 0, 1
        ls = []
        while True:
            if 0 <= i < m and 0 <= j < n:
                # print(mat[i][j])
                ls.append(mat[i][j])
            i, j, d = nxt(i, j, d)
            if d == None:
                break;

        return ls


def main():
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ]
    ls = Solution().findDiagonalOrder(mat)
    print(ls)


if __name__ == '__main__':
    main()
