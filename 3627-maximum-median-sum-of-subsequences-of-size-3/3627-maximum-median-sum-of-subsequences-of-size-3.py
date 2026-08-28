class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        median = 0
        l = 0
        r = len(nums)-2
        while l!=n//3:
            median+=nums[r]
            l+=1
            r-=2

        return median   
        