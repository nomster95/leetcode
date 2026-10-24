class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        ans = 0
        for i in range(len(nums)):
            if minK<=nums[i]<=maxK:
                count+=1
                ans+=count
            else:
                count = 0

        return ans            

        
        
        