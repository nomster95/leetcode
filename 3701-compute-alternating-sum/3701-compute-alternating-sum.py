class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if i%2==0:
                ans = ans + nums[i]
            else:
                ans = ans - nums[i]    

        return ans        