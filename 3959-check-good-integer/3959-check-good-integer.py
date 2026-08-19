class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        squre_sum = 0
        digit_sum = 0
        while n!=0:
            digit = n%10
            squre_sum  = squre_sum+ digit**2
            digit_sum = digit_sum + digit
            n = n//10

        if squre_sum - digit_sum>=50:
            return True
        else:
            return False    

                
        