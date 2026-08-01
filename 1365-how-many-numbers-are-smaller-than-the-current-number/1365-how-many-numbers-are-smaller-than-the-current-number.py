class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j]<nums[i]:
                    count+=1
            ans.append(count)    

        return ans        
        
