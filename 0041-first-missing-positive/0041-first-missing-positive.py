class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = set(nums)
        n = max(nums)
        for i in range(1,n+1):
            if i not in ans:
                return i
                

        return n+1 if n>0 else 1      

        
    
        