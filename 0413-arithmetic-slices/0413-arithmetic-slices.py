class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums)<3:
            return 0
        count = 0
        slices = 0
        for i in range(len(nums)-2):
            if nums[i+1]-nums[i]==nums[i+2]-nums[i+1]:
                slices+=1
                count+=slices
            else:
                slices = 0

        return count            


        