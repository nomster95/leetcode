class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        peak = max(nums)
        n = len(nums)
        l,r = 0,0
        count = 0
        p_count = 0
        while r<len(nums):
            if nums[r]==peak:
                p_count+=1

            while p_count>=k:
                if nums[l]==peak:
                    p_count-=1
                l+=1

            
            count+=r-l+1

            r+=1    

        return n*(n+1)//2-count                    
        