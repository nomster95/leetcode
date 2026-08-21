class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score  = 0
        n = len(nums)
        
        for i in range(n):
            nums[i].sort()

        for i in zip(*nums):
            score+=max(i)

        return score        

        