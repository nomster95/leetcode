class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        ans = 0
        mod = 10**9+7

        for i in nums:
            num = str(i)
            w = int(num[-1])
            d = num[:len(num)-1]
            x = int(d[:w])
            y = int(d[w:])
            sol = pow(x,y,mod)
            ans = (ans+sol)%mod

        return ans    

            
        
        