class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        ans = 0
        for i in s:
            if i==c:
                ans+=1

        return ans*(ans+1)//2        
        