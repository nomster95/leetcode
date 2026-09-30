class Solution:
    def subarray(self,nums,goal):
        l,r,count,sums = 0,0,0,0
        if goal<0:
            return 0
        while r<len(nums):
            sums+=(nums[r]%2)

            while sums>goal:
                sums = sums - (nums[l]%2)
                l+=1

            count += r-l+1
            r+=1

        return count    
        
        
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        return self.subarray(nums,k)-self.subarray(nums,k-1)
        