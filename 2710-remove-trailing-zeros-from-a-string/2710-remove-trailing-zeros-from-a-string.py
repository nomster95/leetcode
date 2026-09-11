class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num)-1
        while num[i]=="0":
            i = i-1

        return num[0:i+1]    
        
        