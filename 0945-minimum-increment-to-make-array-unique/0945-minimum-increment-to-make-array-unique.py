class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        count = 0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                inc = max(nums[i-1]+1,nums[i])
                count+= (inc-nums[i])
                nums[i] = inc

        return count    
        