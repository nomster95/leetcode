class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0

        commas = 0
        for i in range(1000,n+1):
            commas+=1   

        return commas     


        