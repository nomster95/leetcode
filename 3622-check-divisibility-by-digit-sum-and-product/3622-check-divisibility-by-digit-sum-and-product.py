class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        m = n
        while m!=0:
            digit = m%10
            digit_sum = digit_sum + digit
            digit_product = digit_product*digit

            m = m//10

        if n%(digit_sum + digit_product)==0:
            return True

        return False        


        