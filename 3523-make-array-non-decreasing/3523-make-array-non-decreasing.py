class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        peak = nums[0]
        for i in range(1,n):
            if nums[i]>=peak:
                peak = nums[i]
            else:
                count+=1

        return n-count            
                  
        