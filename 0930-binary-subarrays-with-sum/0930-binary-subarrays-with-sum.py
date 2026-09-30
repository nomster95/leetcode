class Solution:
    def subarray(self,nums,goal):
        l,r,count,sums = 0,0,0,0
        if goal<0:
            return 0
        while r<len(nums):
            sums+=nums[r]

            while sums>goal:
                sums = sums - nums[l]
                l+=1

            count += r-l+1
            r+=1

        return count    


    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        return self.subarray(nums,goal)-self.subarray(nums,goal-1)
        
        