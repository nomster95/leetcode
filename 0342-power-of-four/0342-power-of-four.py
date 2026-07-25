class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #base case
        if n<=0:
            return False
        if n==1:
            return True
        if n%4!=0:
            return False

        #recursive case 
        return self.isPowerOfFour(n//4)            
        