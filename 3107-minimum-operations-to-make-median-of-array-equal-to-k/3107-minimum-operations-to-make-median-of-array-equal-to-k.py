class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            if i<n//2:
                if nums[i]>k:
                    ans+=(nums[i]-k)

            elif i==n//2:
                ans+=abs(nums[i]-k)        
                
            else:
                if nums[i]<k:
                    ans+=(k-nums[i])

        return ans                    

        