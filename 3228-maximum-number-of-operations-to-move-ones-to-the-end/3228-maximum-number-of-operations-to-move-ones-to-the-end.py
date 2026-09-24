class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ans = 0
        for i in range(len(s)):
            if s[i]=='1':
                ones+=1
            else:
                if i==len(s)-1 or s[i+1]=='1':
                    ans+=ones
                

        return ans            
        