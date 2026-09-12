class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n = len(nums)
        left_part = [0] * n
        right_part = [0] * n
        for i in range(n):
            j = -i-1
            left_part[i] = left
            right_part[j] = right
            left*=nums[i]
            right*=nums[j]

        return [l*r for l,r in zip(left_part,right_part)]    
        