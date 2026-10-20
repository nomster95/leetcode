class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        prefMax = []
        curr_max = nums[0]
        for i in range(len(nums)):
            curr_max = max(curr_max,nums[i])
            prefMax.append(curr_max)

        conver = [0]*len(nums)
        for i in range(len(nums)):
            conver[i] = nums[i] + prefMax[i]

        ans = [0]*len(nums)
        ans[0] = conver[0]
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] + conver[i]

        return ans       


           

        