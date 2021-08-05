class Binary:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a,b = b,a
        a = [ int(x) for x in a[::-1]]
        b = [ int(x) for x in b[::-1]]
        c = []
        carry = 0
        for x,y in zip(a,b):
            z = x + y + carry
            carry = z/2
            z = z%2
            c.append(z)
        for i in range(len(b),len(a)):
            z = a[i] + carry
            carry = z/2
            z = z%2
        if carry !=0 :
            c.append(carry)
        return ''.join([str(x) for x in c[::-1]])
        


        