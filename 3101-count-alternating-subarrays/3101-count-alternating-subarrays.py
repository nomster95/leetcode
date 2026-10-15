class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        count = 0
        alter = 1
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]:
                alter+=1
            else:
                alter = 1

            count+=alter    

        return count+1          
        