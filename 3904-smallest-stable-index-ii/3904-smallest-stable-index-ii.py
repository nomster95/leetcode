class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefMax = [0]*len(nums)
        suffMin = [0]*len(nums)
        ans = -1
        suffMin[-1] = nums[-1]
        prefMax[0] = nums[0]
        for i in range(1,len(nums)):
            prefMax[i] = max(prefMax[i-1],nums[i])

        for j in range(len(nums)-2,-1,-1):
            suffMin[j] = min(suffMin[j+1],nums[j])

        for x in range(len(nums)):
            stable = prefMax[x]-suffMin[x]
            if stable<=k:
                ans = x 
                break

        return ans        
                



        