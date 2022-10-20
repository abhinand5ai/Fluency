# https://leetcode.com/problems/remove-k-digits/
class RemoveKDigits:
    def removeKdigits(self,num:str, k:int):
        digits=list(num)
        size = [len(digits)]
        j = 0
        while k> 0:
            # print(j)
            while j < size[0] - 1 and digits[j] <= digits[j + 1]:
                print(j)
                j += 1
                
            del digits[min(j,size[0] - 1)]
            size[0] -= 1
            k -= 1
        removedNum =  ''.join(digits).lstrip('0')
        return "0" if removedNum == '' else removedNum
        
rD = RemoveKDigits()
2
print(rD.removeKdigits("1111111",3))
        

