class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 2
        length = 2
        
        for i in range(2,len(nums)):
            if nums[i] == nums[i-1] + nums[i-2]:
                length+=1
                max_len = max(max_len,length)
            else:
                length = 2

        return max_len            


        