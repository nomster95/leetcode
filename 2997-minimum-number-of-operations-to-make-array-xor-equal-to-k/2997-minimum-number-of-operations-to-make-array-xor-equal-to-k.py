class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = nums[0]
        for i in range(1,len(nums)):
            ans = ans^nums[i]

        diff = ans^k
        op = 0
        while diff:
            op+=diff&1

            diff = diff>>1

        
        return op        

            
            


        