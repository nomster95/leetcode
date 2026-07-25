class Solution:
    def maxProduct(self, n: int) -> int:
        great1 = 0
        great2 = 0
        while n>0:
            digit = n%10
            n = n//10
            if(digit>=great1):

                great2 = great1
                great1 = digit
            elif(digit<great1 and digit>great2):

                great2 = digit
        return great1*great2        

