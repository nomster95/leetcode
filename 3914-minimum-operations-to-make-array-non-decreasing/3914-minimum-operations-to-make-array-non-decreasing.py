class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                ans += (nums[i-1]-nums[i])

        return ans        
        