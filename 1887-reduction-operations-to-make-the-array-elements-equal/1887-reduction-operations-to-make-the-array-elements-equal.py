class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        if len(set(nums))==1:
            return 0

        nums.sort()
        ans = 0
        count = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                count+=1
            ans+=count

        return ans        


        