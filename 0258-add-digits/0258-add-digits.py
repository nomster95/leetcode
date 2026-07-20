class Solution:
    def addDigits(self, num: int) -> int:
        digit = 0
        
        
        while(num>=10):
            digit = 0
            while(num>0):
                digit+= num%10
                num = num//10
            num = digit 

        return num   

