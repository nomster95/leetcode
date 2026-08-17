class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        OR = 0
        for i in nums:
            if i%2==0:
                OR = OR | i

        return OR        
        