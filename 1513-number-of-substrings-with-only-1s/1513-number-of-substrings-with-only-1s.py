class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        n = 0
        mod = 10**9 + 7

        for i in s:
            if i=="1":
                n+=1
                count = (count+n)%mod
            else:
                n = 0

        return count            


       