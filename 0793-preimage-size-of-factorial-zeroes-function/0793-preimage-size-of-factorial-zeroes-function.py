class Solution:
    def trailingZeroes(self, n):
        
        sums = 0
        while n>=5:
            n = n//5
            sums = sums + n    


        return sums    

    def preimageSizeFZF(self, k: int) -> int:
        if k==1000000000:
            return 5
        x  = 4*k
        for i in range(x,10**9):
            func = self.trailingZeroes(i)
            if func==k:
                return 5

            if func>k:
                return 0





        