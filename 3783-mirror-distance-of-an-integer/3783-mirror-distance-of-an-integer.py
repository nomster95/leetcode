class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        m = n
        while m!=0:
            digit = m%10
            rev = rev*10+digit
            m = m//10


        return abs(n-rev)   

       

        
    
        