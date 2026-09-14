class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        ans = 0
        if len(nums)==1:
            return 0

        if len(nums)==2:
            if nums[0]<nums[1]:
                return 0
            else:
                return 1        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=nums[i+1]:
                ans =  i+1
                break

        return ans        

        