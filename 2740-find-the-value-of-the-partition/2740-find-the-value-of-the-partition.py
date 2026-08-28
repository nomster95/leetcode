class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        for i in range(len(nums)-1):
            ans.append(nums[i+1]-nums[i])

        return min(ans)    

