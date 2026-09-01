class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mon_inc = True
        mon_dec = True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                mon_inc = False

            if nums[i]<nums[i+1]:
                mon_dec = False


        return mon_inc or mon_dec            

        