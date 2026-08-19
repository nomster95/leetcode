class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2!=0:
            ans = "a"*n
        else:
            ans = "a"*(n-1)+"b"  
        
        return ans