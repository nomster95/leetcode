class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i] = 1
                if nums[i+1]==0:
                    nums[i+1] = 1
                elif nums[i+1]==1:
                    nums[i+1] = 0

                if nums[i+2]==0:
                    nums[i+2]= 1
                elif nums[i+2]==1:
                    nums[i+2] = 0

                ops+=1

        if len(set(nums))!=1:
            return -1 

        return ops               


        