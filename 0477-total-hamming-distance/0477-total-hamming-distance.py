class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            ones = 0

            for x in nums:
                if x & (1<<i):
                    ones+=1

            zeroes = len(nums)-ones
            ans+= zeroes*ones

        return ans            
                
        