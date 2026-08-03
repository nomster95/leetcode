class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(1,len(s)+1):
            ans = ans + (123-ord(s[i-1]))*i

        return ans    

        