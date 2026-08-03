class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_length = float("inf")
        current_sum = 0
        for r in range(len(nums)):
            current_sum = current_sum + nums[r]
            
            while current_sum>=target:
                w = r-l+1
                current_sum = current_sum - nums[l]
                min_length = min(min_length,w)
                l+=1
        if min_length== float("inf"):
            return 0 

        return min_length        




        
        