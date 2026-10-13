class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        l,r = 0,0
        mask = 0
        max_len = 0
        while r<len(nums):

            while mask & nums[r]!=0:
                mask^=nums[l]
                l+=1

            mask |= nums[r]    

            max_len = max(max_len,r-l+1)
            r+=1

        return max_len    



        