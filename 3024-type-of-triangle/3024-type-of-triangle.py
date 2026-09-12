class Solution:
    def triangleType(self, nums: List[int]) -> str:
        is_valid = False
        if nums[0]+nums[1]>nums[2] and nums[0]+nums[2]>nums[1] and nums[1] + nums[2]>nums[0]:
            is_valid = True

        if is_valid:
            if len(set(nums))==3:
                return "scalene"
            elif len(set(nums))==2:
                return "isosceles"
            else:
                return "equilateral"    

        return "none"                



        