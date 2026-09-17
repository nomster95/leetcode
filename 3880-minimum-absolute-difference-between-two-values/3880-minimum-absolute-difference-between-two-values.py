class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==1 and nums[j]==2:
                    ans.append(abs(i-j))

        if len(ans)==0:
            return -1

        return min(ans)                
        