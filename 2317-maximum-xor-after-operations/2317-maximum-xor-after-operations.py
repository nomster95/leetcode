class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        OR = 0
        for i in range(len(nums)):
            OR = OR | nums[i]

        return OR    
        
        