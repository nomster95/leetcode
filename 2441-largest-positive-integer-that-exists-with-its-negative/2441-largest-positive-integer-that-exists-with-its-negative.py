class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        ans = set(nums)
        k = -1
        for i in range(len(nums)-1,-1,-1):
            if -nums[i] in ans:
                k = nums[i]
                break

        return k        
        
        