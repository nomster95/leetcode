class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        ans = target[0]
        if len(target)==1:
            return ans

        
        for i in range(1,len(target)):
            ans+=max(target[i]-target[i-1],0)

        return ans    
        
        