class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        total = 0
        nums.sort()
        for i in range(k):
            index = len(nums)-1-i
            if mul>0:
                total+=nums[index]*mul
            else:
                total+=nums[index]

            mul-=1    
                
        return total        



        