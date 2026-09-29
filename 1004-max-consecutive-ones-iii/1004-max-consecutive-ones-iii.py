class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l,r = 0,0
        n = len(nums)
        max_len = 0
        zeroes = 0
        while r<n:
            if nums[r]==0:
                zeroes+=1

            while zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1

            if zeroes<=k:
                max_len = max(max_len,r-l+1)

            r+=1

        return max_len                    
        