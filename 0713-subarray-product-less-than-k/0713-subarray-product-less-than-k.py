class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:
            return 0
        l,r = 0,0
        count = 0
        product = 1
        while r<len(nums):
            product = product*nums[r]

            while product>=k:
                product = product//nums[l]
                l+=1

            count+=r-l+1
            r+=1

        return count        
        