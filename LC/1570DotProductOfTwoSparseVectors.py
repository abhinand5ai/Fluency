from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []
        self.n = len(nums)
        acc = []
        zeros = 0
        for num in nums:
            if num != 0:
                if zeros: self.nums.extend([zeros] + [0])
                acc.append(num)
                zeros = 0
            else:
                if acc: self.nums.extend([len(acc)] + acc)
                zeros += 1
                acc.clear()
        if zeros: self.nums.extend([zeros] + [0])
        if acc: self.nums.extend([len(acc)] + acc)

    def dotProduct(self, vec: 'SparseVector') -> int:
        v2 = vec.nums
        v1 = self.nums
        n = self.n

        dotP = 0
        #       i   j   l  v
        itr1 = [-1, -1, 0, v1]
        itr2 = [-1, -1, 0, v2]

        def nextNonZero(itr):
            i, j, l, v = itr

            #print(f"{i=:2} {j=:2} {v[j]=:4} {l=:2}")
            def packItr(): itr[0], itr[1], itr[2], itr[3] = i, j, l, v

            if i == n - 1: return False

            if l == 0:
                j += 1
                l = v[j]
                ##print(i, j, v[j])
                packItr()
                return nextNonZero(itr)
            elif v[j + 1] == 0:
                i += l
                j += 1
                l = 0
                ##print(i, j, v[j])
                packItr()
                return nextNonZero(itr)
            else:
                i += 1
                j += 1
                l -= 1
                packItr()
                #print(f"{i=:2} {j=:2} {v[j]=:4} {l=:2} <--")
                return True

        nextNonZero(itr1)
        nextNonZero(itr2)
        while True:
            if itr1[0] < itr2[0]: 
                if not nextNonZero(itr1): return dotP
            elif itr2[0] < itr1[0]: 
                if not nextNonZero(itr2): return dotP
            else:
                #print(f"{v1[itr1[1]]}, {v2[itr2[1]]}")
                dotP += v1[itr1[1]] * v2[itr2[1]]
                if not nextNonZero(itr1): return dotP
                if not nextNonZero(itr2): return dotP

        return dotP



def main():
    v1 = [1, 2, 3, 4, 0, 0, 0, 5, 0, 6, 0, 0, 7, 0, 0, 0]
    v2 = v1.copy()
    v2.reverse()
    #print(v1)
    #print(v2)
    sv1 = SparseVector(v1)
    sv2 = SparseVector(v2)
    #print(sv1.nums)
    print(sv1.dotProduct(sv2))

if __name__ == '__main__':
    main()
