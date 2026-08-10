class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n^(n>>1)
        if x&(x+1)==0:
            return True

        return False    
        