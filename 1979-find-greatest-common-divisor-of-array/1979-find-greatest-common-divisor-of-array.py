class Solution:
    def findGCD(self, nums: List[int]) -> int:
        large = max(nums)
        small = min(nums)
        for i in range(1,small+1):
            if large%i==0 and small%i==0:
                gcd = i

        return gcd        
        