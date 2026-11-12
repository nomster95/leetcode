class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = 1
        cnt_inc = 1
        cnt_dec = 1
        n = len(nums)
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                cnt_inc+=1
                cnt_dec = 1
            elif nums[i]>nums[i+1]:
                cnt_inc = 1
                cnt_dec+=1
            else:
                cnt_inc = 1
                cnt_dec = 1

            max_len = max(max_len,max(cnt_inc,cnt_dec))    

        return max_len            







        