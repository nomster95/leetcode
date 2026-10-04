class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0
        maxl = -1
        minl = -1
        last_bad = -1
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                last_bad = i

            
            if nums[i]==minK:
                minl = i

            if nums[i]==maxK:
                maxl = i

            ans+=max(0,min(minl,maxl)-last_bad)

        return ans                
        