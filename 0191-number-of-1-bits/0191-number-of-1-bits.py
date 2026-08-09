class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n>1:
            ans+=n&1

            n = n>>1    

        if n==1:
            ans+=1

        return ans        
        