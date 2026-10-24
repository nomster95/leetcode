class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        flips = 0
        for i in range(len(nums)):
            effect = nums[i]^flips
            if effect==0:
                flips = 1-flips
                ops+=1

        return ops        

        

        