class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        l,r = 0,0
        ans = []

        while r<len(nums):
            ans.append(nums[r])

            if nums[r]>maxK or nums[r]<minK:
                l = r+1

            count+= r-l+1

            r+=1

        return count    
            
        
        