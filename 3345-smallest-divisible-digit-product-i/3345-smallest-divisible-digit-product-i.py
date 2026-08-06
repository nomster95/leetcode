class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while(True):
            product = 1
            for i in str(n):
                product = product*int(i)

            if product%t==0:
                return n
            n+=1 



        