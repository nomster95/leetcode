import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        max_gcd = 0
        for i in range(n):
            for j in range(i+1,n):
                hcf = math.gcd(nums[i],nums[j])
                strength = (nums[i]*nums[j])//(hcf)**2
                max_gcd = max(max_gcd,strength)

        return max_gcd        
        