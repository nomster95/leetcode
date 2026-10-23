class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        AND = -1
        n = len(nums)
        for i in range(n):
            if nums[i]!=i:
                AND = AND & nums[i]

        return max(AND,0)        
        