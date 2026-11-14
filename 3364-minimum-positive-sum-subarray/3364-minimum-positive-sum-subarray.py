class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                arr = nums[i:j+1]
                x = sum(arr)
                if l<=len(arr)<=r and x>0:
                    min_sum = min(min_sum,x)

        if min_sum==float('inf'):
            return -1

        return min_sum                
        