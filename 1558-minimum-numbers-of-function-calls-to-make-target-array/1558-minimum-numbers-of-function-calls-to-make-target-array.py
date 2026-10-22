class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ops = 0
        n = len(nums)
        while True:
            for i in range(n):
                if nums[i]%2!=0:
                    nums[i] = nums[i]-1
                    ops+=1

            if sum(nums)==0:
                break        

            for i in range(n):
                nums[i] = nums[i]//2
            ops+=1

        return ops        





                
        