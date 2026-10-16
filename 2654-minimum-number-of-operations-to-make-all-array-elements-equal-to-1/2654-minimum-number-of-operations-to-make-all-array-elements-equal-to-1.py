class Solution:
    def hcf(self,a,b):
        while b!=0:
            a , b = b , a%b

        return a    
        
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones>0:
            return n-ones

        min_length = float('inf')
        for i in range(n):
            hcf = nums[i]
            for j in range(i+1,n):
                hcf = self.hcf(hcf,nums[j])
                if hcf==1:
                    min_length = min(min_length,j-i+1)

        if min_length==float('inf'):
            return -1

        return min_length-1 + n - 1    




        
        