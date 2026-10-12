class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        max_len = 0
        for i in range(len(nums)):
            rem = nums[i]%k
            sums = 0

            for j in range(i,len(nums)):
                if nums[j]%k!=rem:
                    break

                sums+=nums[j]
                if (sums-nums[i])%k==0:
                    max_len = max(max_len,j-i+1)

        return max_len                
        
        