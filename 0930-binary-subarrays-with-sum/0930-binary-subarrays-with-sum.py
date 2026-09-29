class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        freq = {0:1}
        prefix = 0
        count = 0
        for i in range(len(nums)):
            prefix+=nums[i]

            needed = prefix - goal
            if needed in freq:
                count+=freq[needed]

            freq[prefix] = freq.get(prefix,0)+1

        return count        
        