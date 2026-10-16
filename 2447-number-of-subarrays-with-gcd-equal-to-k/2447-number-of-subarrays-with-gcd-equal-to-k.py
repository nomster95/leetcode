
class Solution:
    def hcf(self,a,b):
        while b:
            a , b = b , a%b
        return a

    def subarrayGCD(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            hcf = 0
            for j in range(i,n):
                hcf = self.hcf(hcf,nums[j])

                if hcf==k:
                    count+=1

        return count            

        