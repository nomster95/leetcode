class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        n = 0
        mod = 10**9 + 7
        r = 0
        while r<len(s):
            l = r
            while l<len(s) and s[l]=="1":
                count = (count + (l-r+1))%mod
                l+=1

            r = l+1    

        return count    



          


       