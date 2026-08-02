class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        
        for i in nums:
            digit = 0
            for j in str(i):
                
                digit = digit + int(j)
            ans.append(digit)
            
        return min(ans)