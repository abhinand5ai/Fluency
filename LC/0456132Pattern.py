class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        three = []
        two = float('-inf')
        for one in reversed(nums) :
            if three and one < three[-1] and one < two:
                return True
            while three and one > three[-1]:
                two = three.pop()
            three.append(one)

        return False
        

def main():
    sol = Solution()
    res = sol.find132pattern([3,1,4,2])
    print(res)
    pass

if __name__ == '__main__':
    main()
