class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        index = 0
        if len(nums)==1:
            return 1
        nums.sort()    
        ans = 1
        for i in range(len(nums)):
            if nums[i]-nums[index]>k:
                ans+=1
                index = i

        return ans        

        