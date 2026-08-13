class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        harshad = 0
        y = x
        while y!=0:
            digit = y%10
            harshad+=digit
            y = y//10



        if x%harshad==0:
            return harshad

        return -1    

