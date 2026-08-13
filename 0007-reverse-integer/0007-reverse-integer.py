class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x<0
        y = abs(x)
        rev = 0
        while y>0:
            digit = (y)%10
            rev = rev*10+digit
            y = y//10


            if rev>2**31-1:
                return 0

        return rev*-1 if is_neg else rev        

        
        