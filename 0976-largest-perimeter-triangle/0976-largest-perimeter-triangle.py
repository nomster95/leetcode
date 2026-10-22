class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        max_p = 0
        for i in range(n-1,1,-1):
            if nums[i-1]+nums[i-2]>nums[i]:
                max_p = max(max_p,nums[i]+nums[i-1]+nums[i-2])

        return max_p        
        