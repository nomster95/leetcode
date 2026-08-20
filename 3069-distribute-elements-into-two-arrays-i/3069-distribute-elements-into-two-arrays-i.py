class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        last_arr1 = nums[0]
        arr2 = [nums[1]]
        last_arr2 = nums[1]
        for i in range(2,len(nums)):
            if last_arr1>last_arr2:
                arr1.append(nums[i])
                last_arr1 = nums[i]
            else:
                arr2.append(nums[i])
                last_arr2 = nums[i]    

                
        return arr1+arr2    

        
        