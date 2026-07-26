class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        greatest_number = float('-inf')
        second_greatest = float('-inf')
        third_greatest = float('-inf')
        for i in range(n):
            if nums[i]==greatest_number or nums[i]==second_greatest or nums[i]==third_greatest:
                continue
    
            if(nums[i]>greatest_number):
                third_greatest = second_greatest #always update from bottom
                second_greatest = greatest_number
                greatest_number = nums[i]
            elif(nums[i]<greatest_number and nums[i]>second_greatest):
                third_greatest = second_greatest
                second_greatest = nums[i]
            elif(nums[i]<second_greatest and nums[i]>third_greatest):
                third_greatest = nums[i]    

        if third_greatest==float('-inf'):
            return greatest_number

        return third_greatest    

        

        