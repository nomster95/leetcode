class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        curr_sum1 = 0
        curr_sum2 = 0
        n = len(nums)
        for i in range(n):
            curr_sum1+=nums[i]
            curr_sum2+=nums[i]

            if curr_sum1>max_sum:
                max_sum = curr_sum1

            if curr_sum2<min_sum:
                min_sum = curr_sum2


            if curr_sum1<0:
                curr_sum1 = 0

            if curr_sum2>0:
                curr_sum2 = 0


        return max(max_sum,abs(min_sum))        


        
        