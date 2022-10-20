class UglyNumber:
    def nthUglyNumber(self, n: int) -> int:
        two = [2]
        three = [3]
        five =[5] 
        currN = 1
        while n > 0:
            print(currN)
            currN = min(two[0],three[0],five[0])
            if currN == two[0]:
                two.pop(0)
            if currN == three[0]:
                three.pop(0)
            if currN == five[0]:
                five.pop(0)
            two.append(currN*2)
            three.append(currN*3)
            five.append(currN*5)
            n -= 1
        return currN



        

uN = UglyNumber()
uN.nthUglyNumber(10)

            

 