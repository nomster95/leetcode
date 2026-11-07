class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        sums = 0
        while n>=5:
            n = n//5
            sums = sums + n    


        return sums    


        