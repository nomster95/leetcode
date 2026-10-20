class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        curr_max = nums[0]
        total = 0
        ans = []
        for i in range(len(nums)):
            curr_max = max(curr_max,nums[i])
            total+= nums[i] + curr_max
            ans.append(total)

        return ans    

       

           

        