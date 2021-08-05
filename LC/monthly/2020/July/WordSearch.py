from typing import List,Set,Tuple

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        def wordSearch(i:int, j: int, index: int, visited:Set[Tuple[int, int]] = set()) -> bool:
            if len(word) ==  index:
                return True
            if (i,j) in visited or not(0 <= i < m and 0 <= j < n) or word[i] != board[i][j]:
                return False
            index += 1
            visited.add((i,j))
            neighbours = [(i + 1,j), (i - 1, j), (i, j + 1), (i, j -1)]
            exists = any((wordSearch(x,y,index,visited) for x,y in neighbours))
            visited.remove((i,j))
            return exists

        for x in range(m):
            for y in range(n):
                if wordSearch(x,y, 0):
                    return True
        return False


            
            
            

