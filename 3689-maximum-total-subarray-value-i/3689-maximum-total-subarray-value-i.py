class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ans = 0
        maxima = max(nums)
        minima = min(nums)
        for i in range(k):
            ans+= (maxima-minima)


        return ans    
            
        