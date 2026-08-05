class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            index = abs(i)-1
            if nums[index]>0:
                nums[index] = -nums[index]
            else:
                ans.append(index+1)
            
        return ans