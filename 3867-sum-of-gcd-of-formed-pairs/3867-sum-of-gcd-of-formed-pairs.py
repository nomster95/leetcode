import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        gcd_sum = 0
        prefixGcd = [0]*len(nums)
        mx = nums[0]
        for i in range(len(nums)):
            mx = max(mx,nums[i])
            prefixGcd[i] = math.gcd(nums[i],mx)

        prefixGcd.sort()
        i = 0
        j = len(prefixGcd)-1
        while i<len(prefixGcd)//2:
            hcf = math.gcd(prefixGcd[i],prefixGcd[j])
            gcd_sum+=hcf
            i+=1
            j-=1

        return gcd_sum    

        