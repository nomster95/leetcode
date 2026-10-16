import math
class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            hcf = 0
            for j in range(i,n):
                hcf = math.gcd(hcf,nums[j])

                if hcf==k:
                    count+=1

        return count            

        