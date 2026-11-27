class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        zeroes = 0
        count = 0
        for i in range(len(s)):
            if s[i]=="1":
                ones+=1
            else:
                count+=ones

        return count        
