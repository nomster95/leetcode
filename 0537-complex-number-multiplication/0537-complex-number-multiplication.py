class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        #basic formula for complex multiplication
        # a1a2-b1b2 + (a1b2+a2b1)*i
        a1,b1 = num1.split("+")
        a2,b2 = num2.split("+")
        a1,b1 = int(a1),int(b1[:-1])
        a2,b2 = int(a2),int(b2[:-1])
         

            
        
        real = a1*a2 - b1*b2
        imaginary = a1*b2 + a2*b1

        return f"{real}+{imaginary}i"
