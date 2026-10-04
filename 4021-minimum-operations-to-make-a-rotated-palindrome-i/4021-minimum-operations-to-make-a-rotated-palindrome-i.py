class Solution:
    def minOperations(self, s: str) -> int:
        sol = float('inf')
        n = len(s)
        for k in range(n):
            ch = s[k:] + s[:k]
            ans = 0
            for i in range(n//2):
                a = ch[i]
                b = ch[n-i-1]
                d = abs(ord(a)-ord(b))

                ans+= min(d,26-d)


            ans+=k    
            sol = min(sol,ans)





        return sol 
        