class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        ans = [0]*len(nums)
        for i in range(len(nums)):
            left_count = i
            right_count = len(nums)-i-1
            right_sum = total - left_sum - nums[i]

            left = nums[i]*left_count - left_sum
            right = right_sum - nums[i]*right_count
            dist = left + right

            ans[i] = dist
            left_sum+=nums[i]

        return ans    


        