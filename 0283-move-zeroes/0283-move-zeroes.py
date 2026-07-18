class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr = 0
        n = len(nums)
        #claasic two pointer
        for i in range(n):
            if(nums[i]!=0):
                nums[i],nums[curr] = nums[curr],nums[i]
                curr+=1
        