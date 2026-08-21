class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(0,10**5+1):
            digit  = str(i)
            rev = digit[::-1]
            if i + int(rev)==num:
                return True

        return False        
            
        