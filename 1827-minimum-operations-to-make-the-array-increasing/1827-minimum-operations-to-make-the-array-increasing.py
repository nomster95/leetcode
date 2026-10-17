class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)):
            ops = max(nums[i-1]+1,nums[i])
            count+=(ops-nums[i])
            nums[i] = ops


        return count    
        