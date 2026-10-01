class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        l,r = 0,0
        count = 0
        sums = 0
        while r<len(nums):
            sums+=nums[r]

            while sums*(r-l+1)>=k:
                sums-=nums[l]
                l+=1

            count+=(r-l+1) 
            r+=1

        return count    



            

        