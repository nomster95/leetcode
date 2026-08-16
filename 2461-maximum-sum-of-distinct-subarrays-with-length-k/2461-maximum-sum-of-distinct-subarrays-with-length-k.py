class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        window_sum = sum(nums[0:k])    

        if k == len(freq):
            max_sum = window_sum
        else:
            max_sum = 0  

        l,r = 0,k    

        while r<len(nums):
            window_sum = window_sum + nums[r] - nums[l]
            freq[nums[r]] = freq.get(nums[r],0)+1
            freq[nums[l]]-=1
            if freq[nums[l]]==0:
                del freq[nums[l]]

            if len(freq)==k:
                max_sum = max(max_sum,window_sum)

            l+=1
            r+=1    

        return max_sum        

        

    

        