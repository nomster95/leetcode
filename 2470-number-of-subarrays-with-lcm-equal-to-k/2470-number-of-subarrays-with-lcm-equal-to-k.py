import math
class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            lcm = 1
            for j in range(i,n):
                lcm = (lcm*nums[j])//(math.gcd(lcm,nums[j]))
                if k%nums[j]!=0:
                    break
                    
                if lcm==k:
                    count+=1
                

                
        return count              
                

        