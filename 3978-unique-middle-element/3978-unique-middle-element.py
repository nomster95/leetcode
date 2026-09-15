class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums)//2
        if nums.count(nums[mid])>1:
            return False
        return True    

        

        