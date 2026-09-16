class Solution:
    def averageValue(self, nums: List[int]) -> int:
        n = 0
        value = 0
        for i in nums:
            if i%2==0 and i%3==0:
                n+=1
                value+=i

        if n==0:
            return 0        

        return value//n        
        